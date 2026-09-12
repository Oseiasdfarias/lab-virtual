---
fonte: softwares_aeropendulo/main_aeropendulo.py, softwares_aeropendulo/rungui.py, softwares_aeropendulo/pyproject.toml, softwares_aeropendulo/requirements.txt, softwares_aeropendulo/README.md, softwares_aeropendulo/simulador_aeropendulo/__init__.py, softwares_aeropendulo/src_interface/__init__.py
gerado_em: 2026-09-12
---

# Visão Geral do Software — Aeropêndulo

## Estrutura do pacote

`softwares_aeropendulo/` é um único projeto Python (Poetry) com dois subpacotes principais:

- `simulador_aeropendulo/` — "Gêmeo digital": simulação 3D (VPython) do aeropêndulo, animação e gráficos.
- `src_interface/` — Interface gráfica (customtkinter) que fala com o hardware real via serial/USB, plota sinais em tempo real e grava ensaios em CSV.

Ambos têm o mesmo padrão interno: uma pasta `interfaces/` com **classes abstratas (ABC)** que definem o contrato de cada módulo, e os arquivos na raiz do pacote com a **implementação concreta** que herda dessas interfaces (ex.: `ColetaDadosInterface` → `ColetaDados`). Isso é um Dependency Inversion simples: `interface_grafica.py` e `main_aeropendulo.py` importam pelas interfaces/implementações concretas dos dois pacotes, permitindo rodar a GUI com ou sem o simulador acoplado.

## Pontos de entrada

| Arquivo | Função | Observação |
|---|---|---|
| `rungui.py` | Ponto de entrada oficial da interface gráfica. Aceita `-simular sim` (via `argparse`) para instanciar também o `Simulador` (gêmeo digital) em paralelo à GUI real. | É o script documentado/atual. |
| `main_aeropendulo.py` | Roda **apenas** o simulador standalone (sem GUI), com loop físico próprio (integração de Euler) e animação VPython. | **Quebrado**: importa `ModeloMatAeropendulo` e `ControladorDiscreto` de `simulador_aeropendulo`, mas nenhuma dessas classes existe no pacote atual (`simulador_aeropendulo/__init__.py` só exporta `Graficos`, `AnimacaoAeropendulo`, `Simulador`). Parece um script legado de uma versão anterior do simulador (antes da refatoração para `Simulador` guiado externamente por dados reais/seriais). Não executa como está. |

Fluxo de `rungui.py`:
1. Lê `-simular sim/nada` via CLI.
2. Se `simular`, cria `Simulador(Graficos(), AnimacaoAeropendulo())` (gêmeo digital VPython).
3. Sempre cria `InterfaceAeropendulo(GraficosSinais, simulador, baud_rate=115200, amostras=80.0, tela_fixa=True)` — essa é a GUI principal (customtkinter + matplotlib) que conecta na porta serial do microcontrolador.
4. Dentro de `InterfaceAeropendulo`, a cada frame de animação (`FuncAnimation`), se houver simulador, `atualizar_simulador()` empurra os dados reais lidos da serial para dentro do gêmeo digital 3D, sincronizando a animação VPython com o hardware físico.

## Dependências principais (pyproject.toml)

Python `>=3.8,<3.12`. Poetry, com grupo `dev` só para mkdocs (docs).

- `matplotlib` — gráficos em tempo real (embutidos no Tkinter via `FigureCanvasTkAgg`).
- `numpy`, `pandas` — manipulação de arrays e persistência de ensaios em CSV.
- `pyserial` — comunicação serial com o microcontrolador.
- `customtkinter` — biblioteca de GUI (skin moderna sobre Tkinter).
- `pyudev` — monitoramento de conexão/desconexão de dispositivos USB (Linux, via netlink).
- `vpython` — motor 3D usado no simulador/gêmeo digital.
- `scienceplots`, `mplfonts` — estilo científico dos gráficos matplotlib.
- `control`, `scikit-learn`, `sympy` — provavelmente usados nos notebooks de modelagem/projeto de controladores (`simulador_aeropendulo/docs/`), não no runtime da GUI.

`requirements.txt` é um artefato separado/mais antigo (pip freeze de um ambiente Jupyter — traz `jupyter*`, `mypy`, etc., que não aparecem no `pyproject.toml`); não deve ser a fonte de verdade para reproduzir o ambiente — usar `pyproject.toml`/`poetry.lock`.

## Como rodar

Não há seção "instalação/uso" explícita no `README.md` da raiz (ele só descreve a interface com imagens). Pela leitura do código:

```bash
poetry install
poetry run python rungui.py                 # só interface real (sem gêmeo digital)
poetry run python rungui.py -simular sim     # interface real + gêmeo digital 3D sincronizado
```

`main_aeropendulo.py` (simulador standalone) não deve ser usado no estado atual — precisa de correção/recuperação das classes `ModeloMatAeropendulo`/`ControladorDiscreto` (provavelmente existiam em uma versão anterior de `simulador.py`, ou precisam ser reimplementadas a partir da modelagem em `simulador_aeropendulo/docs/Modelagem_matematica_do_aeropendulo.ipynb` e do README do simulador, que documenta a equação de movimento do aeropêndulo).

## Diretórios auxiliares

- `design_interface/` — mockups/imagens de design da interface (PDF/Xopp + PNGs), referenciados pelo `README.md` da raiz.
- `firmwares_microcontroladores/` — firmwares C++/Arduino para os microcontroladores que rodam o controle embarcado e enviam dados via serial (ver `docs_tcc/02_software/firmware_microcontroladores.md`).
