---
fonte: revisao_tcc/Template_TCC_FEE/Capitulos/3_hardware_softwares/3_0_simulador_e_prototipo_do_Aeropendulo.tex, revisao_tcc/Template_TCC_FEE/Capitulos/3_hardware_softwares/3_0_0_dev_software.tex, revisao_tcc/Template_TCC_FEE/Capitulos/3_hardware_softwares/3_1_prototipagem.tex, revisao_tcc/Template_TCC_FEE/Capitulos/3_hardware_softwares/3_2_1_python.tex, revisao_tcc/Template_TCC_FEE/Capitulos/3_hardware_softwares/3_2_simulador_usando_python.tex, revisao_tcc/Template_TCC_FEE/Capitulos/3_hardware_softwares/3_3_interface_grafica.tex, revisao_tcc/Template_TCC_FEE/Capitulos/3_hardware_softwares/3_4_firmware.tex, revisao_tcc/Template_TCC_FEE/Capitulos/3_hardware_softwares/3_5_ecossistema.tex
gerado_em: 2026-09-12
---

Todos os 8 arquivos deste subcapítulo estão incluídos no PDF final (via `Cap_2_Desenvolvimento.tex`) e são de conteúdo completo (nenhum placeholder encontrado).

## Arquitetura geral do sistema (síntese)

```
[Interface Gráfica (PC, Python/CustomTkinter)] <--USB serial (PySerial)--> [Firmware ESP32 (C/C++, PlatformIO)] --PWM/L298N--> [Motor CC série + hélice] --empuxo--> [Braço do Aeropêndulo]
        |                                                                                                                              |
        |--> dados salvos em CSV (Pandas)                                                                    [Potenciômetro 50kΩ] <----+ (sensor de ângulo)
        |
        `--> alimenta em tempo real o [Gêmeo Digital / Simulador 3D (VPython)]
```

- **Protótipo físico**: estrutura de compensado + braço em tubo de fibra de vidro/carbono, motor CC série + hélice (kit de drone FPV racing) na ponta do braço, potenciômetro 50kΩ como sensor de ângulo (encoder), driver L298N para PWM, ESP32 como controlador central, fonte chaveada 5V/5A, filtro RC na leitura do sensor.
- **Firmware (ESP32, C/C++, PlatformIO)**: bibliotecas modulares — `ler_escrever_serial` (I/O serial), `referencia` (geração de onda quadrada/senoidal/dente de serra com amplitude/frequência/offset configuráveis), `conversor` (potenciômetro→ângulo, sinal de controle→PWM, grau↔radiano), `controlador_pid` (classe C++ do PID). Lógica principal em `main.cpp`.
- **Interface gráfica (Python)**: front-end com CustomTkinter (widgets) + Matplotlib (gráficos em tempo real); back-end com PySerial (comunicação serial), NumPy (arrays), Pandas (salvamento em CSV). Permite: configurar amplitude/frequência/offset do sinal de referência; escolher forma de onda (serra, quadrada, senoidal); alternar malha aberta/fechada; salvar dados; selecionar dispositivo USB; tema claro/escuro.
- **Gêmeo digital (simulador 3D, VPython)**: biblioteca VPython para renderização 3D navegável no navegador; classe `Simulador` recebe módulos de animação 3D e gráficos de linha; consome em tempo real o ângulo do braço via comunicação serial (mesmos dados que alimentam a interface gráfica) e replica a dinâmica do protótipo físico.
- **Linguagens**: Python (interface, gêmeo digital, análise/identificação), C/C++ (firmware embarcado, framework Arduino).

## 3.0 Simulador e protótipo (visão geral) — `3_0_simulador_e_prototipo_do_Aeropendulo.tex`

Parágrafo curto introdutório mostrando a figura do protótipo finalizado (estrutura + parte elétrica montadas).

## 3.0.0 Desenvolvimento de software (visão geral) — `3_0_0_dev_software.tex`

Parágrafo introdutório: conjunto de softwares (firmware, simulador 3D/gêmeo digital, interface gráfica) permite ao usuário manipular o sinal de referência e visualizar os estados do sistema em tempo real.

## 3.1 Prototipagem — `3_1_prototipagem.tex`

- **Estrutura**: compensado de madeira (chapas laminadas coladas com fibras perpendiculares).
- **Braço**: tubo de fibra de vidro de carbono 3x3x2mm — escolhido por leveza (reduz a resistência à força de empuxo).
- **Componentes elétricos**: potenciômetro 50kΩ (sensor de ângulo/encoder), placa ESP32 (dual-core, Wi-Fi, Bluetooth, GPIO/I2C/SPI/UART), fonte chaveada 5V/5A (alimentação do motor), driver L298N (PWM → tensão controlada no motor), conjunto motor/hélice de drone FPV racing (geração do empuxo), componentes RC (filtro na leitura do potenciômetro).
- **Montagem física**: estrutura desmontável em 3 partes com pontos de conexão; braço desacoplável no pivô/eixo do potenciômetro; resultado descrito como estável, sem vibrações indesejadas.
- **Montagem elétrica**: ESP32 gera PWM de controle, lê sinal filtrado do potenciômetro, comunica-se via serial com o PC; driver alimentado em 5V amplifica o sinal para o motor.

## 3.2.1 Linguagens (Python, C, C++) — `3_2_1_python.tex`

- Python escolhido para visualização de dados e simulador (versatilidade, popularidade em ciência de dados/IA, sintaxe simples).
- C/C++ escolhidos para o microcontrolador (eficiência, portabilidade, padrão em sistemas embarcados). Breve histórico: C (Dennis Ritchie, 1972, Unix), C++ (Bjarne Stroustrup, 1983, extensão OO de C).

## 3.2 Gêmeo digital / Simulador usando Python — `3_2_simulador_usando_python.tex`

- Biblioteca **VPython**: criação de objetos 3D com movimento rotacional/translacional, gráficos em tempo real, renderizado no navegador.
- Arquitetura: módulo de gráficos de linha + módulo de animação 3D, integrados por um módulo `Simulador` (classe Python orientada a objetos) que recebe os dois como dependências (injeção de dependência simples via `__init__`).
- Classe `Simulador` (código-fonte incluído no TCC): métodos `grau2rad`, `rotate`, `atualizar_estados` (recebe tempo, ângulo, referência; calcula velocidade angular por diferença finita `dtheta_rad = Δθ/Δt`; atualiza rotação do objeto 3D e os dois gráficos de linha via `plot1`/`plot2`).
- Import de módulos: `.interfaces.graficos_aeropendulo.GraficosInterface`, `.interfaces.animacao_aeropendulo.AnimacaoAeropenduloInterface`, `.interfaces.simulador.SimuladorInterface` — indica uso de interfaces/abstrações (padrão de design com classes abstratas).
- O gêmeo digital é importado dentro do software da interface gráfica (integração single-process).

## 3.3 Interface gráfica — `3_3_interface_grafica.tex`

- Front-end (CustomTkinter) + gráficos dinâmicos (Matplotlib) + back-end de aquisição/tratamento de dados + classe de detecção automática de microcontrolador na porta USB.
- Bibliotecas: **CustomTkinter** (UI moderna cross-platform sobre Tkinter), **Matplotlib** (`pyplot`/`animation` para gráficos em tempo real), **PySerial** (comunicação serial USB), **NumPy** (matrizes de dados), **Pandas** (salvamento em CSV).
- Execução: `python rungui.py -simular sim` (com gêmeo digital) ou `python rungui.py` (só interface).
- Código de exemplo mostra classe `RunInterface` com `argparse` para habilitar/desabilitar o simulador.
- Partes da interface (numeradas na figura, 10 itens): configuração de amplitude/frequência/offset; seleção de forma de onda (serra/quadrada/senoidal); área de gráficos; painel de informações (amplitude, frequência, offset, sinal de erro em tempo real); botão executar; toggle malha aberta/fechada; toggle salvar dados (CSV com timestamp); seleção de dispositivo USB; seleção de tema claro/escuro; botão sair.

## 3.4 Firmware — `3_4_firmware.tex`

- Desenvolvido com **PlatformIO** (multi-plataforma: ESP32, família Arduino, STM32, etc.).
- Estrutura modular em bibliotecas:
  - `ler_escrever_serial`: I/O serial (recebe configurações, envia estados do sistema).
  - `referencia` (`referencia.h`): implementa 3 sinais de referência (onda quadrada, senoidal, dente de serra) com amplitude/frequência/offset configuráveis; extensível.
  - `conversor`: classe C++ com conversões — potenciômetro→ângulo, sinal de controle→ciclos PWM, grau↔radiano.
  - `controlador_pid`: classe C++ do controlador PID, usado quando a interface seleciona malha fechada.
  - `main.cpp`: orquestra as bibliotecas.
- Gravação no ESP32 via PlatformIO (compilação + upload via porta serial).

## 3.5 Ecossistema / fluxograma do laboratório virtual — `3_5_ecossistema.tex`

Parágrafo curto: diagrama de blocos (figura) consolidando a interação entre todos os subsistemas (protótipo, firmware, interface, gêmeo digital), apresentado como recurso para pesquisadores futuros entenderem o sistema como um todo.
