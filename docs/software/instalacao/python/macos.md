---
title: Python 3.11 no macOS
author: Oséias Farias
---

# Python 3.11 no macOS

O projeto roda em **Python 3.10 ou 3.11**; versões 3.12 ou mais novas ainda não são suportadas
pelas dependências.

## Opção 1: Homebrew

Se o [Homebrew](https://brew.sh/) ainda não estiver instalado, siga as instruções do site.
Depois, instale o Python e o Tkinter, usado pela interface gráfica:

```bash
brew update
brew install python@3.11 python-tk@3.11
```

O Homebrew coloca o comando `python3.11` em `/opt/homebrew/bin` (Apple Silicon) ou
`/usr/local/bin` (Intel), que já estão no `PATH` depois da instalação do Homebrew.

## Opção 2: instalador oficial

Em [python.org/downloads/macos](https://www.python.org/downloads/macos/), baixe o instalador
*universal2* da versão 3.11 mais recente e execute-o. Ele já inclui o Tkinter.

## Verificando

```bash
python3.11 --version
python3.11 -c "import tkinter; print('Tkinter', tkinter.TkVersion)"
```

Em seguida, siga para as [dependências do projeto](../dependencias.md); com Poetry, aponte o
ambiente para essa versão com `poetry env use python3.11`.

!!! warning "Interface testada só no Linux"
    A lista de portas da interface é atualizada com o `pyudev`, que depende do `libudev` do
    Linux. Nesse sistema a interface nunca foi testada e deve falhar ao abrir; os scripts de análise
    (identificação e métricas) não dependem disso.
