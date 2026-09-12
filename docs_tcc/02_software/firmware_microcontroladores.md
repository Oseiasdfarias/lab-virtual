---
fonte: softwares_aeropendulo/firmwares_microcontroladores/Arduino_IDE/Arduino_Nano/src/main.cpp, softwares_aeropendulo/firmwares_microcontroladores/Arduino_IDE/arduino_uno/teste_aeropendulo_malha_aberta.ino, softwares_aeropendulo/firmwares_microcontroladores/PlatformIo/Esp32_ttgo/src/main.cpp, softwares_aeropendulo/firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos/src/main.cpp, softwares_aeropendulo/firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos/lib/*/src/*, softwares_aeropendulo/firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos_freertos/src/main.cpp, softwares_aeropendulo/firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos_freertos/lib/*/src/*, softwares_aeropendulo/firmwares_microcontroladores/PlatformIo/Arduino_Nano/src/main.cpp, softwares_aeropendulo/firmwares_microcontroladores/PlatformIo/arduino_uno/src/main.cpp
gerado_em: 2026-09-12
---

# Firmwares dos Microcontroladores

## Visão geral das variantes

Há duas árvores paralelas (`Arduino_IDE/` e `PlatformIo/`) para os mesmos alvos de hardware — aparentam ser o mesmo firmware portado/mantido em dois ambientes de build diferentes, não necessariamente sincronizados entre si (o Arduino Nano em `Arduino_IDE/` e o de `PlatformIo/` têm código bem diferente entre si, por exemplo).

| Variante | Alvo | Nível de sofisticação |
|---|---|---|
| `Arduino_IDE/Arduino_Nano` | Arduino Nano (ATmega328) | Malha aberta/fechada simples, sinal fixo, tudo em um `main.cpp` |
| `Arduino_IDE/arduino_uno` (`.ino`) | Arduino Uno | Mínimo: só leitura de potenciômetro + PWM fixo, sem protocolo serial estruturado |
| `PlatformIo/Arduino_Nano` | Arduino Nano | Idêntico em espírito ao Arduino Uno mínimo (leitura + PWM fixo) |
| `PlatformIo/arduino_uno` | Arduino Uno | Idem, versão ESP32-style de pinos mas alvo AVR |
| `PlatformIo/Esp32_ttgo` | ESP32 TTGO, sem módulos | Igual ao Arduino Nano da Arduino_IDE, mas com PWM via `ledcSetup`/`ledcWrite` (API ESP32) |
| `PlatformIo/Esp32_ttgo_modulos` | ESP32 TTGO, com libs customizadas | **Mais completa**: PID, geração de referência (quadrada/seno/dente-de-serra/PRBS), malha aberta/fechada selecionável via serial |
| `PlatformIo/Esp32_ttgo_modulos_freertos` | ESP32 TTGO | Apesar do nome, **não usa nenhuma API de FreeRTOS** (`xTaskCreate` etc. não aparecem em nenhum arquivo da árvore de firmwares) nem o controlador PID; é uma versão **mais simples/antiga** que `Esp32_ttgo_modulos`, só com os módulos `referencia` e `ler_escrever_serial` (e o `referencia.cpp` desse variante não usa nem a classe `SinaisRefs`/`OndaPrbs` no `main.cpp`) |

**Conclusão**: a variante mais completa e funcionalmente mais avançada é `PlatformIo/Esp32_ttgo_modulos` — é a única com controlador PID fechado, geração de múltiplas formas de onda de referência (incluindo PRBS para identificação de sistema) e alternância malha aberta/fechada via protocolo serial. A variante `_freertos` parece um estágio intermediário/anterior de refatoração, cujo nome sugere trabalho futuro (portar para tasks FreeRTOS) que não foi implementado.

## Protocolo de comunicação serial com o PC

Comum a todas as variantes "completas" (Arduino Nano/ESP32 sem/com módulos): **baud rate 115200**, texto ASCII, CSV terminado em `\n`.

**Envio (microcontrolador → PC)**, uma linha por ciclo, valores separados por vírgula:
```
referencia, angulo(theta), erro, sinal_de_controle, ampl_ou_entrada_ma, ampl_ou_entrada_ma(repetido), tempo
```
Isso bate exatamente com o buffer de 7 colunas usado em `ColetaDados` (`self.fila = np.array([[], [], [], [], [], [], []])`) e com os CSVs de ensaio (7 colunas, ver `dados_ensaios.md`).

**Recepção (PC → microcontrolador)**, valor numérico único por escrita, decodificado por **faixa de valor** (não por delimitador):
| Faixa recebida | Significado | Fórmula de decodificação (firmware `Esp32_ttgo_modulos`) |
|---|---|---|
| 1000–2000 | Amplitude | `(rlen*30/1000) - 30` |
| 2001–3000 | Frequência | `(rlen*5/1000) - 10` |
| 3001–4000 | Offset | `(rlen*120/1000) - 360` |
| 7000 | Selecionar onda dente de serra | — |
| 8000 | Selecionar onda senoidal | — |
| 9000 | Selecionar onda quadrada | — |
| 10000 | Ativa malha fechada (`conf_sistema=true`) | — |
| 11000 | Ativa malha aberta (`conf_sistema=false`) | — |
| 12000 | Inicia execução (`executar=true`) | — |

Esse protocolo é implementado em `lib/ler_escrever_serial/ler_escrever_serial.cpp` e é consumido do lado PC em `src_interface/coleta_dados.py` (`set_amplitude`, `set_frequencia`, `set_offset`, `set_sinal`) — ver `interface_grafica.md`. As variantes mais simples (Arduino Nano/Uno "mínimos", Arduino_IDE) usam só as 3 primeiras faixas (amplitude/frequência/offset), sem seleção de onda nem malha aberta/fechada.

## Controle PID no firmware

Implementado em `PlatformIo/Esp32_ttgo_modulos/lib/controlador_pid/src/controlador_pid.cpp`, classe `PID`:

```cpp
PID mypid(0.02, 0.055, 0.35);  // Kp, Ki, Kd (instanciado em main.cpp)
float PID::atualiza_pid(float erro, float theta, float Ts) {
    P = erro * Kp;
    I += (erro * Ki) * Ts;
    D = Kd * erro * (lastTheta - theta) * Ts;   // nota: forma não usual (multiplica erro, não delta_erro/Ts)
    lastTheta = theta;
    return P + I + D;
}
```

- PID incremental simples, sem anti-windup explícito, chamado a cada iteração do `loop()` com `Ts = 0.02` s.
- **Observação de possível bug**: o termo derivativo usa `erro * (lastTheta - theta) * Ts`, que não corresponde à forma clássica `Kd * d(erro)/dt` — multiplica pelo erro atual e por `Ts` (ao invés de dividir), o que é atipicamente dimensionado. Vale conferir na dissertação se esse comportamento foi intencional/calibrado empiricamente.
- Existe também uma classe alternativa `Controladores::controlador_1()` (`lib/controladores/src/controladores.cpp`) — um controlador digital de 2ª ordem por equação a diferenças com coeficientes fixos (`u0 = 1.724*u1 - 0.7241*u2 + 19.09*erro - 35.66*e1 + 16.68*e2`, saturado em ±1), aparentemente um controlador projetado via LGR/discretização (ver `simulador_aeropendulo/docs/projeto_de_controladores/`), mas **não é chamado no `main.cpp` atual** (a linha está comentada: `// sinal_controle = controle.controlador_1(...)`) — só o PID está ativo.

### Geração de sinal de referência (`lib/referencia/src/referencia.cpp`)

- `SinaisRefs::referencia_onda_quadrada/seno/onda_dente_serra` — formas de onda clássicas para excitar o sistema em malha fechada.
- `OndaPrbs::onda_prbs()` — gerador de sinal **PRBS** (Pseudo-Random Binary Sequence, com período sorteado entre 4 valores pseudoaleatórios), usado como sinal de excitação em **malha aberta** — típico de ensaios de **identificação de sistemas**.

### Conversões (`lib/conversor/src/conversor.cpp`)

- `converte_escala()` — mapeamento linear genérico com correção de offset (usado para converter leitura ADC do potenciômetro em ângulo).
- `converte_tensao_ciclo()` — converte tensão de controle (0–3.3V) para ciclo de trabalho PWM (0–255). **Bug notado**: a condição `if (0.0 <= sinal_controle <= 3.3)` em C++ não faz o que parece — `0.0 <= sinal_controle` avalia para `bool` (0 ou 1), que é então comparado com `<= 3.3` (sempre verdadeiro); ou seja, o `else if` para saturar em 255 quando `sinal_controle > 3.3` é código mortos na prática (a primeira condição sempre entra). Efeito prático provavelmente pequeno (o `ciclo_trabalho` calculado por `sinal_controle*255/3.3` já estoura o range de PWM para valores >3.3V, sem clamping — possível fonte de comportamento errático em saturação).

## Loop principal (`Esp32_ttgo_modulos/src/main.cpp`)

Estrutura do `loop()`:
1. Só executa se `executar==true` (setado remotamente pelo código 12000).
2. Lê potenciômetro (ADC), converte para ângulo (`conv.converte_escala`).
3. Se `conf_sistema==true` (malha fechada): gera referência (quadrada/seno/dente-de-serra conforme `selecionar_onda`), calcula erro, chama PID, converte para ciclo PWM.
4. Senão (malha aberta): gera sinal PRBS como entrada direta, zera referência/erro/controle.
5. Escreve PWM (`ledcWrite`), envia telemetria via serial, processa comandos recebidos, incrementa `t += Ts` (`Ts=0.02s`, ou seja ~50 Hz).

## Diferenças de hardware entre variantes

- **Arduino Nano/Uno (AVR)**: leitura ADC em pino analógico (`A0`-`A3`), PWM via `analogWrite` padrão (resolução 8-bit fixa do AVR), controle de sentido do motor via 2 pinos digitais (ponte H).
- **ESP32 TTGO**: ADC em GPIO numérico (`pin 2`), PWM via `ledcSetup`/`ledcWrite` (canal, frequência 500 Hz ou 30 kHz, resolução 8-bit configurável), mesma lógica de ponte H em GPIOs diferentes (32/33 ou 37/38 dependendo da variante).
- O mapeamento ADC→ângulo (`map()`/`converte_escala`) usa faixas calibradas empiricamente e diferem por variante (ex.: `map(valorAD_POT, 528, 3235, 0, 180)` no Arduino Nano/ESP32 simples vs `converte_escala(valorAD_POT, 0, 4095, 0, 270, 528)` no ESP32 modular) — indício de recalibração/potenciômetro trocado entre versões.

## Arquivos com problemas identificados

- `PlatformIo/Arduino_Nano/src/main.cpp`: **contém um erro de sintaxe** — caractere solto `k` na última linha do arquivo, após o `}` de fechamento do `loop()`. Não compila como está.
- `PlatformIo/Esp32_ttgo/lib/ler_escrever_serial/src/ler_escrever_serial.cpp` e `.h`: **arquivos vazios** (0 linhas) — resíduo de biblioteca não utilizada (o `main.cpp` dessa variante implementa `enviar_dados_serial`/`ler_dados_serial` diretamente inline, sem usar essa lib).
- `PlatformIo/Esp32_ttgo_modulos_freertos`: nome sugere uso de FreeRTOS/multitarefa mas o código não usa nenhuma API de tasks/filas do FreeRTOS; e tem menos funcionalidade que `Esp32_ttgo_modulos` (sem PID, sem seleção de forma de onda, sem malha aberta/fechada) — parece uma versão desatualizada/protótipo abandonado, não a mais avançada.
