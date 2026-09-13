---
title: Interface Gráfica de Usuário
author: Oséias Farias

---

<style>
        .tab {
            display: inline-block;
            margin-left: 40px;
        }
        .tab1 {
            display: inline-block;
            margin-left: 80px;
        }
</style>


<center>
<div class="figure" >
  <img src="https://github.com/Oseiasdfarias/lab-virtual/blob/main/brand/png/icone-256.png?raw=true"
       width="80">  
</div>
</center>

<center>
<div class="figure" >
  <img src="https://github.com/Oseiasdfarias/lab-virtual/blob/main/utils/demo_interface_light.png?raw=true"
       width="900">  
  <p>Figura 1 - Interface Gráfica de Usuário.</p>
</div>
</center>

<br/>

## O que é

A interface gráfica é composta por um menu com opções de controle e visualização, e um
conjunto de gráficos dinâmicos que mostram os estados do sistema em tempo real. Por trás da
parte visual existe uma camada de aquisição e tratamento de dados: uma classe cuida da
leitura e do pré-processamento dos dados vindos da porta serial, e outra detecta
automaticamente o microcontrolador conectado à USB.

Para realizar ensaios, ajustar parâmetros do sinal de referência e coletar dados, o
microcontrolador precisa estar rodando o [firmware](firmware.md)
correspondente — é ele que fornece à interface os dados a serem pré-processados e plotados.

## Como executar

Para rodar a interface gráfica junto com o Gêmeo Digital:

```bash
python rungui.py -simular sim
```

Para rodar só a interface gráfica, sem o simulador 3D:

```bash
python rungui.py
```

## Bibliotecas utilizadas

- **CustomTkinter** — estrutura de tela, botões e entradas de texto. Segundo a
  [documentação oficial](https://customtkinter.tomschimansky.com/), é "uma biblioteca de UI
  de desktop Python baseada em Tkinter, que fornece widgets de aparência moderna e
  totalmente personalizáveis", com aparência consistente em Windows, macOS e Linux.
- **Matplotlib** (`pyplot` e `animation`) — geração de gráficos em tempo real integrados à
  interface.
- **PySerial** — comunicação serial entre o computador e o microcontrolador via USB.
- **NumPy** — montagem das matrizes com os dados lidos pela porta serial.
- **Pandas** — persistência dos dados de ensaio em arquivos CSV.

## Partes da interface

1. **Sinal de referência** — configura amplitude, frequência e offset (ponto de equilíbrio)
   do sinal aplicado à entrada do sistema em malha fechada.
2. **Seleção do sinal de referência** — onda dente de serra, quadrada ou senoidal, com os
   parâmetros do item 1.
3. **Gráficos** — plotagem dos estados do sistema em tempo real.
4. **Informações** — mostra amplitude, frequência, offset e o sinal de erro atuais.
5. **Executar** — inicia o ensaio (requer o microcontrolador conectado).
6. **MA/MF** — alterna entre malha aberta e malha fechada.
7. **Salvar dados** — grava os dados em CSV, nomeado com data e hora do ensaio, para não
   sobrescrever coletas anteriores.
8. **Selecionar dispositivo** — lista os microcontroladores conectados e permite escolher
   qual usar no ensaio.
9. **Selecionar tema** — alterna entre tema claro e escuro.
10. **Quit** — encerra a aplicação.

<br/>