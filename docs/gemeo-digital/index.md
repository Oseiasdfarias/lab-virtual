---
title: Gêmeo Digital
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
<b>Universidade Federal do Pará</b>
</center>
<center>
<b>Campus Universitário de Tucuruí</b>
</center>
<center>
<b>Faculdade de Engenharia Elétrica</b>
</center>

<br>


<center>
<div class="figure" >
  <img src="https://github.com/Oseiasdfarias/lab-virtual/blob/main/utils/gemeo_digital.png?raw=true"
       width="900">  
  <p>Figura 1 - Gêmeo Digital.</p>
</div>
</center>

<br/>

## O que é

O Gêmeo Digital é um sistema gráfico computacional que reproduz em tempo real a dinâmica do
protótipo físico. Isso permite virtualizar o Aeropêndulo — observar a mesma dinâmica do
sistema real, agora num ambiente gráfico 3D — obtendo o estado atual do braço por meio da
comunicação serial com o microcontrolador.

## Biblioteca VPython

O simulador foi desenvolvido com a biblioteca [VPython](https://vpython.org/), que oferece
funções para criar objetos 3D com movimentos rotacionais e translacionais, além de plotagem
de gráficos em tempo real. A interface final é composta de duas partes: o ambiente 3D com o
Aeropêndulo e os gráficos do sinal de referência e de saída.

Sendo desenvolvido em Python, o VPython é fácil de aprender mesmo para quem tem pouca
experiência em programação, mas também oferece recursos avançados para uso mais experiente.
Ao rodar uma simulação, ela é renderizada no navegador padrão do sistema operacional.

## Arquitetura

O simulador é dividido em três módulos:

- **Módulo de gráficos de linha** — plota os sinais em tempo real (posição angular,
  referência, erro, sinal de controle).
- **Módulo de animação 3D** — desenha e movimenta a estrutura do Aeropêndulo.
- **Módulo Simulador** — integra os dois anteriores e atualiza seus estados a partir dos
  dados recebidos da [Interface Gráfica de Usuário](../software/interface-grafica.md), que
  fornece o ângulo real do protótipo; a velocidade angular é calculada internamente pelo
  próprio módulo, por diferença finita entre amostras consecutivas do ângulo. É essa
  integração que faz o Gêmeo Digital reproduzir a dinâmica do protótipo físico.

A classe principal (`Simulador`, em
[`simulador_aeropendulo/simulador.py`](https://github.com/Oseiasdfarias/lab-virtual/blob/main/softwares_aeropendulo/simulador_aeropendulo/simulador.py))
recebe como parâmetros uma instância de gráficos e uma de animação, e expõe métodos para
rotacionar o braço e atualizar os estados do sistema (ângulo, referência e tempo) a cada
novo dado recebido do protótipo — veja a
[referência dos módulos](../referencia/animacao-aeropendulo.md)
para os detalhes de cada classe.

Para reproduzir a dinâmica no Gêmeo Digital, a classe `Simulador` é importada pelo software
que implementa a comunicação com o protótipo real — ver
[Interface Gráfica de Usuário](../software/interface-grafica.md).

<br/>