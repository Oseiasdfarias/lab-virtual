---
title: Dependências do projeto
---

# Dependências do projeto

As dependências Python ficam em `softwares_aeropendulo/pyproject.toml` e são fixadas no
`poetry.lock`. O `requirements.txt` da mesma pasta é gerado a partir desse lock, então os
dois caminhos abaixo instalam as mesmas versões.

## Com Poetry (recomendado)

Com o [Poetry](https://python-poetry.org/docs/#installation) instalado e o Python 3.10 ou
3.11 disponível:

```bash
git clone https://github.com/Oseiasdfarias/lab-virtual.git
cd lab-virtual/softwares_aeropendulo
poetry install
```

Os comandos do projeto passam a rodar com `poetry run`:

```bash
poetry run python rungui.py               # interface gráfica
poetry run python rungui.py -simular sim  # interface + gêmeo digital
```

## Com pip

Sem Poetry, crie um ambiente virtual e instale a partir do `requirements.txt`:

```bash
git clone https://github.com/Oseiasdfarias/lab-virtual.git
cd lab-virtual/softwares_aeropendulo
python3.11 -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
python rungui.py
```

Em ambos os casos, execute os comandos a partir da pasta `softwares_aeropendulo`: a coleta de
dados usa caminhos relativos a ela.

## Conferindo a instalação

A suíte de testes não precisa do protótipo: confere o protocolo serial, a gravação dos
ensaios, a importação dos módulos e a reprodução das métricas publicadas nesta documentação.

```bash
poetry install --with test
poetry run pytest
```
