---
title: Python 3.11 no Ubuntu
author: Oséias Farias
---

# Python 3.11 no Ubuntu

O projeto roda em **Python 3.10 ou 3.11**. O Ubuntu 22.04 já traz o 3.10, e o 24.04 traz o
3.12, que ainda não é suportado. Este guia instala o 3.11 ao lado do Python do sistema, sem
substituí-lo.

A interface gráfica usa o CustomTkinter, que depende do **Tkinter**. Por isso, o pacote
`python3.11-tk` faz parte da instalação.

## Opção 1: pacotes do PPA *deadsnakes*

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-tk
```

## Opção 2: uv

O [uv](https://docs.astral.sh/uv/) baixa um Python já compilado (com Tkinter) para a pasta do
usuário, sem `sudo`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.11
```

## Verificando

```bash
python3.11 --version
python3.11 -c "import tkinter; print('Tkinter', tkinter.TkVersion)"
```

Com o uv, use `uv run --python 3.11 python --version` se o `python3.11` não estiver no `PATH`.

Os dois comandos devem responder sem erro. Em seguida, siga para as
[dependências do projeto](../dependencias.md); com Poetry, aponte o ambiente para essa versão
com `poetry env use python3.11`.
