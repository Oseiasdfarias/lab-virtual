---
fonte: softwares_aeropendulo/rungui.py, softwares_aeropendulo/pyproject.toml, softwares_aeropendulo/requirements.txt, softwares_aeropendulo/README.md, softwares_aeropendulo/simulador_aeropendulo/__init__.py, softwares_aeropendulo/src_interface/__init__.py
gerado_em: 2026-09-12
atualizado_em: 2026-09-13
---

# Visão Geral do Software — Aeropêndulo

## Estrutura do pacote

`softwares_aeropendulo/` é um único projeto Python (Poetry) com dois subpacotes principais:

- `simulador_aeropendulo/` — "Gêmeo digital": simulação 3D (VPython) do aeropêndulo, animação e gráficos.
- `src_interface/` — Interface gráfica (customtkinter) que fala com o hardware real via serial/USB, plota sinais em tempo real e grava ensaios em CSV.

Ambos têm o mesmo padrão interno: uma pasta `interfaces/` com **classes abstratas (ABC)** que definem o contrato de cada módulo, e os arquivos na raiz do pacote com a **implementação concreta** que herda dessas interfaces (ex.: `ColetaDadosInterface` → `ColetaDados`). Isso é um Dependency Inversion simples: `interface_grafica.py` e `rungui.py` importam pelas interfaces/implementações concretas dos dois pacotes, permitindo rodar a GUI com ou sem o simulador acoplado.

## Pontos de entrada

| Arquivo | Função | Observação |
|---|---|---|
| `rungui.py` | Ponto de entrada oficial da interface gráfica. Aceita `-simular sim` (via `argparse`) para instanciar também o `Simulador` (gêmeo digital) em paralelo à GUI real. | É o script documentado/atual. |

Fluxo de `rungui.py`:
1. Lê `-simular sim/nada` via CLI.
2. Se `simular`, cria `Simulador(Graficos(), AnimacaoAeropendulo())` (gêmeo digital VPython).
3. Sempre cria `InterfaceAeropendulo(GraficosSinais, simulador, baud_rate=115200, amostras=80.0, tela_fixa=True)` — essa é a GUI principal (customtkinter + matplotlib) que conecta na porta serial do microcontrolador.
4. Dentro de `InterfaceAeropendulo`, a cada frame de animação (`FuncAnimation`), se houver simulador, `atualizar_simulador()` empurra os dados reais lidos da serial para dentro do gêmeo digital 3D, sincronizando a animação VPython com o hardware físico.

## Dependências principais (pyproject.toml)

Python `>=3.10,<3.12` (versão do pacote: 1.0.0, licença MIT). Poetry, com grupo `test` (pytest). As ferramentas da documentação saíram do Poetry e ficam em `requirements-docs.txt` na raiz.

- `matplotlib` — gráficos em tempo real (embutidos no Tkinter via `FigureCanvasTkAgg`).
- `numpy`, `pandas` — manipulação de arrays e persistência de ensaios em CSV.
- `pyserial` — comunicação serial com o microcontrolador.
- `customtkinter` — biblioteca de GUI (skin moderna sobre Tkinter).
- `pyudev` — monitoramento de conexão/desconexão de dispositivos USB (Linux, via netlink).
- `vpython` — motor 3D usado no simulador/gêmeo digital.
- `scienceplots`, `mplfonts` — estilo científico dos gráficos matplotlib.
- `control`, `scikit-learn`, `sympy` — usados nos notebooks e scripts de análise (identificação e métricas), não no runtime da GUI.
- `setuptools` fixado em `<82`: o `vpython` 7.6.5 ainda importa `pkg_resources`.

`requirements.txt` é gerado com `poetry export` a partir do `poetry.lock` (as dependências Jupyter vêm de fato do `vpython`), então `pip install -r requirements.txt` instala as mesmas versões.

## Como rodar

A partir de `softwares_aeropendulo/` (a coleta usa caminhos relativos a essa pasta):

```bash
poetry install
poetry run python rungui.py                 # só interface real (sem gêmeo digital)
poetry run python rungui.py -simular sim     # interface real + gêmeo digital 3D sincronizado
poetry install --with test && poetry run pytest   # testes, sem hardware
```

`main_aeropendulo.py` e `interface_interativa.py` foram removidos em 2026-09-13 (código morto).

## Testes

`softwares_aeropendulo/tests/`: protocolo serial conferido contra a decodificação do firmware,
regressão da gravação de ensaios, importação dos módulos e reprodutibilidade das métricas
publicadas. Rodam no CI em `.github/workflows/testes.yml`.

## Diretórios auxiliares

- `design_interface/` — mockups/imagens de design da interface (PDF/Xopp + PNGs), referenciados pelo `README.md` da raiz.
- `firmwares_microcontroladores/` — firmwares C++/Arduino para os microcontroladores que rodam o controle embarcado e enviam dados via serial (ver `docs_tcc/02_software/firmware_microcontroladores.md`).
