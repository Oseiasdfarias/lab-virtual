---
title: Desenvolvimento do Firmaware para ESP32
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
  <img src="https://github.com/Oseiasdfarias/lab-virtual/blob/main/utils/arquitetura_firmware-1.png?raw=true"
       width="900">  
  <p>Figura 1 - Diagrama de blocos do Sistema em Malha Fechada.</p>
</div>
</center>

</br>

## O que é

O firmware do Aeropêndulo foi desenvolvido em bibliotecas separadas por funcionalidade,
tornando o projeto mais flexível — cada parte pode ser atualizada ou substituída sem
interferir na lógica do arquivo principal (`main.cpp`).

O desenvolvimento usa o [PlatformIO](https://platformio.org/), ferramenta multiplataforma
que centraliza a programação de diferentes microcontroladores (ESP32, família Arduino,
STM32, entre outros), tornando o projeto mais portável.

## Bibliotecas

- **`ler_escrever_serial`** — configura os parâmetros do sinal de referência em tempo real e
  envia os estados do sistema pela porta serial, centralizando a comunicação com o
  computador sem misturar essa lógica ao `main.cpp`.
- **`referencia`** — implementa os sinais de referência que o controlador rastreia em malha
  fechada: onda quadrada, onda senoidal e onda dente de serra, cada um configurável em
  amplitude, frequência e offset. Novos sinais podem ser adicionados como módulos
  independentes.
- **`conversor`** — reúne as conversões de grandezas usadas no firmware: sinal do
  potenciômetro para ângulo, sinal de controle para ciclo PWM, grau para radiano e radiano
  para grau.
- **`controlador_pid`** — implementa o controlador PID usado quando a interface gráfica está
  configurada para malha fechada.

## Arquivo principal (`main.cpp`)

O PlatformIO organiza o projeto em bibliotecas mais um arquivo `main.cpp`, que importa essas
bibliotecas e implementa o algoritmo principal. No caso do Aeropêndulo, o `main.cpp` reúne:
geração do sinal de referência, leitura do sensor (potenciômetro), envio e recebimento de
dados pela porta serial, e execução do controlador.

Com o firmware pronto, a gravação no ESP32 é feita pelo próprio PlatformIO, que compila o
código e grava no microcontrolador via porta serial.

<br>