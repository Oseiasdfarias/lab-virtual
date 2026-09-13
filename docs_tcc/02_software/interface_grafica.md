---
fonte: softwares_aeropendulo/src_interface/interface_grafica.py, softwares_aeropendulo/src_interface/coleta_dados.py, softwares_aeropendulo/src_interface/graficos_sinais.py, softwares_aeropendulo/src_interface/lista_portas_usb.py, softwares_aeropendulo/src_interface/test_serial.py, softwares_aeropendulo/src_interface/__init__.py, softwares_aeropendulo/src_interface/interfaces/
gerado_em: 2026-09-12
atualizado_em: 2026-09-13
---

# Interface Gráfica (`src_interface`)

## Nota sobre `interfaces/`

Assim como em `simulador_aeropendulo`, `src_interface/interfaces/` contém apenas as **classes abstratas** (`ColetaDadosInterface`, `GraficosSinaisInterface`) com métodos `@abstractmethod`, e um `ListaPortasUsb` abstrato incompleto (só o método `listar_portas_usb`). Os arquivos na raiz (`coleta_dados.py`, `graficos_sinais.py`, `lista_portas_usb.py`) contêm a implementação real — não há duplicação de lógica.

## Tecnologia de GUI

- **customtkinter** (`ctk`) — wrapper moderno sobre Tkinter (tema "Dark"/"Light" alternável, cor padrão "green"). Janela fixa de 1270×700.
- **matplotlib** embutido via `FigureCanvasTkAgg`, com animação em tempo real via `matplotlib.animation.FuncAnimation` (intervalo de 20 ms, `blit=True`).

## Comunicação com o hardware (serial/USB)

### `lista_portas_usb.py` — classe `ListaPortasUsb`

- Usa `serial.tools.list_ports` para listar portas disponíveis (`listar_portas_usb()`).
- Usa **pyudev** (`Context`, `Monitor.from_netlink`, filtro `subsystem='usb'`) rodando em uma **thread separada** para detectar hot-plug/unplug de dispositivos USB em tempo real (Linux-only — dependência de `pyudev`/netlink não é portável para Windows/Mac).
- Ao detectar mudança, atualiza automaticamente o menu dropdown da GUI (`atualiza_menu.configure(...)`) e a porta selecionada. (A checagem `device.action == 'add' or 'remove'`, sempre verdadeira, virou `in ('add', 'remove')` em 2026-09-13.)

### `coleta_dados.py` — classe `ColetaDados`

Responsável por toda a I/O serial com o microcontrolador, em **thread daemon separada** (`Thread(target=self.__coleta_dados)`).

```python
class ColetaDados(ColetaDadosInterface):
    def __init__(self, amostras: int = 50, porta: str = "/dev/ttyUSB0", baud_rate: int = 115200) -> None: ...
```

- Abre `serial.Serial(porta, baud_rate, timeout=0.005)`.
- Loop de leitura: `readline()` → decodifica UTF-8 → `split(",")` → converte para `np.array(dados1, dtype="float64")` → acumula em `self.fila` (buffer circular de 7 sinais, mantém só as últimas `amostras` leituras, descarta a mais antiga via `np.delete`).
- Se `flag_salvar_dados=True`, também acumula tudo (sem limite) em `self.salvar_dados`, que depois é salvo em CSV (`salvar_dados_colhidos()`, via `pandas.DataFrame.to_csv`, com cabeçalho e índice) na pasta `dados_de_ensaio/` (criada automaticamente se não existir), com nome `arquivo_<dia>_<mes>_<ano>_<hora>_<min>_<seg>.csv`.
- **Corrigido em 2026-09-13:** `salvar_dados_colhidos()` agora esvazia o buffer depois de gravar. Antes, a interface zerava um atributo próprio, e uma segunda gravação na mesma sessão incluiria as amostras da anterior (os 9 CSVs existentes não foram afetados: cada um veio de uma sessão separada). Coberto por teste; falta ensaio no protótipo — ver `divida_tecnica.md`.
- Reconexão automática em caso de `serial.SerialException` (`reconectar()`), com `sleep(2)` e reenvio do comando de sinal atual.
- **Protocolo de envio para o microcontrolador** — escreve strings numéricas ASCII codificadas (não binário) que o firmware decodifica por faixa de valor:
  - `set_amplitude(amplitude)`: `((ampl*1000)/30) + 1000` → faixa ~1000-2000.
  - `set_frequencia(frequencia)`: `((freq*1000)/5) + 2000` → faixa ~2000-3000.
  - `set_offset(offset)`: `((offset*1000)/120) + 3000` → faixa ~3000-4000.
  - `set_sinal(sinal)`: envia código bruto (`"7000"`..`"12000"`) para selecionar forma de onda (dente de serra/seno/quadrada), malha aberta/fechada (10000/11000) e "executar" (12000).
  - Esses códigos batem exatamente com o `ler_dados_serial()` dos firmwares ESP32 modulares (ver `firmware_microcontroladores.md`).
- `os.chdir("src_interface")` no `__init__` é uma dependência frágil do diretório de trabalho — só funciona corretamente se o processo for iniciado a partir da raiz de `softwares_aeropendulo/`.

### `test_serial.py`

Script utilitário isolado (não integrado à GUI) para testar a porta serial manualmente: escreve um float incremental, lê de volta, com lógica de reconexão simples. Usado para depuração/bring-up de hardware, fora do fluxo principal do app.

## Funcionalidades da GUI (`interface_grafica.py` — classe `InterfaceAeropendulo`)

```python
InterfaceAeropendulo(graficos_sinais, simulador, baud_rate=115200, amostras=50, Ts=0.02, tela_fixa=False)
```

- **Plotagem em tempo real**: 4 subplots (matplotlib) atualizados a cada 20 ms via `FuncAnimation` — Referência+Ângulo, Erro, Sinal de Controle, Sinal de entrada em malha aberta (RMS).
- **Seleção de porta USB**: dropdown alimentado por `ListaPortasUsb`.
- **Botão "Executar"**: instancia `ColetaDados` na porta escolhida e inicia a animação.
- **Switch MA/MF**: alterna malha aberta/malha fechada (envia códigos 10000/11000 ao firmware).
- **Switches de forma de onda de referência**: Dente de Serra / Quadrada / Senoidal (mutuamente exclusivos, desmarcam-se entre si).
- **Campos de entrada**: Amplitude (0–30°), Frequência (0–5 rad/s), Offset (0–120°), com validação numérica simples (`isdigit`).
- **Switch "Salvar Dados"**: liga/desliga gravação contínua para CSV; ao desligar, dispara `salvar_dados_colhidos()`.
- **Botão "Quit"**: fecha a janela e limpa o terminal (`cls`/`clear` conforme SO).
- **Integração com o gêmeo digital**: se `simulador` foi passado (modo `-simular sim` em `rungui.py`), cada frame também chama `simulador.atualizar_estados(t, theta, ref)` e `simulador.animacao_aeropendulo.pause_giro()`, sincronizando a cena 3D VPython com os dados reais.

## `graficos_sinais.py` — classe `GraficosSinais`

Configura a figura matplotlib com estilo científico (`scienceplots` + `mplfonts` fonte "Fira Code", backend `TkAgg`):
- 4 subplots em grid 2x2: Referência+Ângulo (graus), Erro (graus), Sinal de Controle (Volts), Sinal de Entrada Malha Aberta (Volts RMS).
- Cada eixo pré-configurado com limites de eixo Y fixos e grid customizado.
- Retorna `(fig, ax, ln)` — `ln` é a lista de `Line2D` usada pelo `FuncAnimation` para atualizar dados sem redesenhar o eixo inteiro (`blit=True`).

## Resumo do fluxo de dados

```
Microcontrolador --serial(115200,ASCII CSV)--> ColetaDados (thread) --fila(np.array)--> InterfaceAeropendulo.update()
                                                                                          ├─> matplotlib (4 gráficos 2D)
                                                                                          ├─> Simulador (opcional, cena 3D VPython)
                                                                                          └─> CSV em dados_de_ensaio/ (se habilitado)
InterfaceAeropendulo --serial(ASCII codificado por faixa)--> Microcontrolador (setpoints/config)
```
