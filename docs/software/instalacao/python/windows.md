---
title: Python 3.11 no Windows
author: Oséias Farias
---

# Python 3.11 no Windows

O projeto roda em **Python 3.10 ou 3.11**; versões 3.12 ou mais novas ainda não são suportadas
pelas dependências.

## Instalação

1. Em [python.org/downloads/windows](https://www.python.org/downloads/windows/), baixe o
   instalador de 64 bits (*Windows installer (64-bit)*) da versão 3.11 mais recente.
2. Na primeira tela do instalador, marque **Add python.exe to PATH** e clique em
   **Install Now**. A instalação padrão já inclui o pip e o Tkinter, usado pela interface
   gráfica.

Se você usa o `winget`, o mesmo resultado sai de:

```powershell
winget install Python.Python.3.11
```

## Verificando

Abra um novo terminal (PowerShell ou Prompt de Comando):

```powershell
py -3.11 --version
py -3.11 -c "import tkinter; print('Tkinter', tkinter.TkVersion)"
```

O lançador `py` escolhe a versão certa mesmo com outros Pythons instalados. Em seguida, siga
para as [dependências do projeto](../dependencias.md); com Poetry, aponte o ambiente para essa
versão com `poetry env use (py -3.11 -c "import sys; print(sys.executable)")` no PowerShell.

!!! note "Porta serial"
    No Windows, o ESP32 aparece como `COM3`, `COM4` etc. Se ele não aparecer no Gerenciador de
    Dispositivos, instale o driver do conversor USB-serial da placa (CP210x ou CH340).

!!! warning "Interface testada só no Linux"
    A lista de portas da interface é atualizada com o `pyudev`, que depende do `libudev` do
    Linux. Nesse sistema a interface nunca foi testada e deve falhar ao abrir; os scripts de análise
    (identificação e métricas) não dependem disso.
