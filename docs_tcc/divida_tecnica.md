---
fonte: softwares_aeropendulo/firmwares_microcontroladores/, softwares_aeropendulo/src_interface/, softwares_aeropendulo/pyproject.toml, figura esquema_eletrico_aerop.png da monografia
gerado_em: 2026-09-13
---

# Dívida técnica

Itens que **não dá para fechar sem o protótipo real** ou que dependem de terceiros. Tudo o que
podia ser resolvido sem hardware foi feito em 2026-09-13 (ver
[`05_plano_publicacoes/pendencias_documentacao.md`](05_plano_publicacoes/pendencias_documentacao.md)).

Cada item diz o estado atual, o risco e como verificar. Ao fechar um item, marque-o com a data
e o resultado do teste.

## Resumo

| ID | Item | Depende de | Prioridade |
| --- | --- | --- | --- |
| DT-01 | Validar a correção do termo derivativo do PID e reajustar os ganhos | Protótipo | Alta |
| DT-02 | Confirmar o pino do sensor de ângulo (GPIO 2 × GPIO 12) | Protótipo | Alta |
| DT-03 | Validar a correção da saturação do sinal de controle | Protótipo | Média |
| DT-04 | Validar interface e gêmeo digital com as dependências atualizadas | Protótipo | Média |
| DT-05 | Validar a gravação de ensaios e a detecção de USB corrigidas | Protótipo | Média |
| DT-06 | Variantes de firmware não validadas: testar, documentar ou arquivar | Protótipo | Baixa |
| DT-07 | Alerta de segurança do `setuptools` | Nova versão do `vpython` | Baixa |

## DT-01 — Termo derivativo do PID

- **Onde:** `PlatformIo/Esp32_ttgo_modulos/lib/controlador_pid/src/controlador_pid.cpp`.
- **Estado:** o termo derivativo foi corrigido para `Kd * (lastTheta - theta) / Ts`. Antes, ele
  multiplicava pelo erro e por `Ts`.
- **Risco:** os ganhos `Kp = 0,02`, `Ki = 0,055` e `Kd = 0,35` foram sintonizados por tentativa e
  erro com a fórmula antiga. Com a derivada correta, o termo D fica muito maior; com o mesmo
  `Kd`, a malha pode oscilar ou saturar.
- **Como verificar:** gravar o firmware, repetir o ensaio de onda quadrada 0°↔10° e comparar com
  as métricas de `docs/controle/resultados.md` (`metricas_malha_fechada.py`); se piorar,
  reduzir `Kd` e registrar os novos ganhos na documentação e no `main.cpp`.

## DT-02 — Pino do sensor de ângulo

- **Onde:** `PlatformIo/Esp32_ttgo_modulos/src/main.cpp` (`pinAD_POT = 2`) × esquema elétrico da
  monografia (sinal filtrado no GPIO 12).
- **Estado:** os pinos do driver (25, 32, 33) coincidem; o do sensor diverge. Sinalizado em
  `docs/prototipo/index.md`.
- **Risco:** quem montar o protótipo pelo esquema terá leitura errada do ângulo com o firmware
  atual. No ESP32, os GPIO 2 e 12 pertencem ao ADC2 e são pinos de *strapping*, o que também
  merece atenção na escolha.
- **Como verificar:** conferir no protótipo em qual pino o potenciômetro está ligado e corrigir o
  esquema ou a constante; atualizar a tabela de pinagem do site.

## DT-03 — Saturação do sinal de controle

- **Onde:** `PlatformIo/Esp32_ttgo_modulos/lib/conversor/src/conversor.cpp`
  (`converte_tensao_ciclo`).
- **Estado:** a comparação encadeada `0.0 <= x <= 3.3`, sempre verdadeira em C++, virou
  `if/else if/else`; o ciclo de trabalho agora satura em 0 e 255.
- **Risco:** baixo, mas muda o comportamento em saturação (antes, valores fora da faixa passavam
  sem limite ao PWM).
- **Como verificar:** forçar sinal de controle alto (degrau grande) e confirmar no gráfico da
  interface que o motor não apresenta comportamento errático.

## DT-04 — Interface e gêmeo digital com as dependências novas

- **Estado:** Python 3.10–3.11, `customtkinter` 5.2.2, `matplotlib` 3.10, `vpython` 7.6.5 com
  `setuptools` 81. Validado sem hardware: instalação limpa, importação de todos os módulos,
  testes (`poetry run pytest`) e scripts de métricas.
- **Risco:** a interface nunca foi aberta com essas versões conectada ao protótipo: animação dos
  gráficos (`FuncAnimation` com `blit`), tema do CustomTkinter, detecção de porta via `pyudev` e
  a cena 3D do VPython no navegador.
- **Como verificar:** `poetry run python rungui.py -simular sim` com o protótipo conectado,
  executar um ensaio completo e observar gráficos, gêmeo digital e gravação.

## DT-05 — Gravação de ensaios e detecção de USB

- **Onde:** `src_interface/coleta_dados.py` e `src_interface/lista_portas_usb.py`.
- **Estado:** `salvar_dados_colhidos()` agora esvazia o buffer depois de gravar (antes, uma
  segunda gravação na mesma sessão incluiria a anterior); a checagem de eventos USB deixou de
  ser sempre verdadeira. A lógica da gravação é coberta por teste (`tests/test_protocolo_serial.py`).
- **Como verificar:** numa mesma sessão, gravar dois ensaios seguidos e confirmar que o segundo
  CSV começa do zero; conectar e desconectar o ESP32 e ver o menu de portas atualizar.

## DT-06 — Variantes de firmware não validadas

Só `PlatformIo/Esp32_ttgo_modulos` corresponde ao que a documentação descreve e ao protocolo que
a interface espera. As demais foram levantadas lendo o código em 2026-09-13. A compilação com PlatformIO não foi
concluída (faltou espaço em disco para a toolchain do ESP32) e **nenhuma foi gravada nem testada
no protótipo**. A variante `PlatformIo/Arduino_Nano` provavelmente nem compila, pois chama
funções do ESP32 com alvo AVR.

| Variante | Placa (`platformio.ini`) | O que o código faz | Compatível com a interface? | Compilação |
| --- | --- | --- | --- | --- |
| `PlatformIo/Esp32_ttgo` | ESP32 TTGO T1 | Protótipo inicial: mesmos pinos da variante documentada, aplica o PWM e envia 6 valores (referência, ângulo, erro, tensão, frequência, amplitude); sem PID nem geração de referência; ângulo por `map(528–3235 → 0–180°)`; decodifica a amplitude recebida na variável `erro`, com escalas diferentes das da interface | Não (6 colunas sem tempo; comandos decodificados com outras escalas) | Não verificada |
| `PlatformIo/Esp32_ttgo_modulos_freertos` | ESP32 TTGO T1 | Versão anterior da modular, só com `referencia` e `ler_escrever_serial`; sem PID e sem malha aberta/fechada. Não usa FreeRTOS | Não verificado | Não verificada |
| `PlatformIo/Arduino_Nano` | Arduino Nano (ATmega328) | Código escrito para ESP32 (`ledcSetup`, GPIO 33/37/38) com alvo AVR; telemetria em texto legível (`valor \| θ° \| Sinal Controle`) | Não (não é CSV) | Não verificada |
| `PlatformIo/arduino_uno` | Arduino Uno | Leitura do potenciômetro e PWM fixo; telemetria em texto legível | Não (não é CSV) | Não verificada |
| `Arduino_IDE/Arduino_Nano` | Arduino Nano (tem `platformio.ini`) | Estrutura parecida com a `Esp32_ttgo` (6 valores por linha), com potenciômetro em A2, entrada em A3, PWM no pino 9 e sentido em 7/8 | Não verificado em detalhe; provavelmente não (mesmo formato da `Esp32_ttgo`) | Não verificada |
| `Arduino_IDE/arduino_uno` | Arduino Uno (`.ino`) | Teste de malha aberta: potenciômetro e PWM; serial a **9600 baud** | Não (a interface usa 115200) | Não compilado (sketch do Arduino IDE) |
| `Arduino_IDE/Esp32_ttgo` | — | Pasta sem código, só o diagrama de pinos | — | — |

**Decisão pendente:** para cada variante, escolher entre (a) testar no protótipo e documentar,
ou (b) mover para uma pasta `firmwares_microcontroladores/legado/` com um README dizendo que não
é mantida. A recomendação é (b) para todas, exceto se houver interesse didático em manter uma
versão para Arduino — nesse caso, portar o protocolo CSV de 7 colunas para que funcione com a
interface.

Observação: `Arduino_IDE/arduino_uno/` contém uma cópia do rascunho de artigo COBENGE 2023 que
não pertence ao firmware.

## DT-07 — Alerta do `setuptools`

- **Estado:** 3 alertas de gravidade média do Dependabot (`setuptools < 83`). O projeto fixa
  `setuptools < 82` porque o `vpython` 7.6.5 importa `pkg_resources`, removido na versão 82.
- **Como fechar:** acompanhar novas versões do `vpython`; quando uma deixar de usar
  `pkg_resources`, remover a restrição do `pyproject.toml`, rodar `poetry lock` e os testes.
