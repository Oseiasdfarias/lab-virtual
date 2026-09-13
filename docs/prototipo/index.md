---
title: Desenvolvimento do Protótipo
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
  <img src="https://github.com/Oseiasdfarias/lab-virtual/blob/main/utils/img_aeropendulo.png?raw=true"
       width="900">  
  <p>Figura 1 - Protótipo do Aeropêndulo.</p>
</div>
</center>

<br/>

## Parte estrutural

O material escolhido para a estrutura foi o compensado — chapas fabricadas a partir de
finas lâminas de madeira coladas com fibras perpendiculares, o que confere maior
estabilidade e resistência mecânica ao produto final.

Já para o braço do Aeropêndulo foi usado um tubo de fibra de carbono de 3×3×2 mm, material
que se destaca pela leveza e resistência física. Na extremidade do braço fica o conjunto
motor/hélice responsável por impulsionar a dinâmica do sistema — por isso é essencial
minimizar a massa do braço: quanto menor a massa, menores as forças de resistência que o
empuxo precisa vencer, resultando numa dinâmica mais ágil e eficiente.

## Parte elétrica

Componentes eletrônicos empregados no projeto: um potenciômetro de 50 kΩ, uma placa de
desenvolvimento ESP32, um módulo driver L298N, um conjunto suporte/motor/hélice (originado
de drones FPV racing quadcopter) e componentes passivos (resistor, capacitor).

**Potenciômetro 50 kΩ** — funciona como *encoder*, obtendo o ângulo de inclinação do braço.
Conforme o braço se movimenta, a resistência do potenciômetro muda, o que altera a tensão
em seus terminais — essa tensão é correlacionada ao ângulo de inclinação do braço.

**Placa de desenvolvimento ESP32** — integra o microcontrolador ESP32 (Espressif), com
processador dual-core de 32 bits, Wi-Fi, Bluetooth e interfaces GPIO/I2C/SPI/UART. É o
centro do sistema: implementa o controlador discreto, lê o sensor de ângulo, calcula o
sinal de erro e gera o sinal de referência.

**Fonte chaveada 5 V/5 A** — alimenta o motor CC série.

**Módulo driver L298N** — regula a velocidade do eixo do motor CC série a partir de um sinal
PWM aplicado à sua entrada, permitindo controlar de forma precisa a tensão entregue ao motor.

**Conjunto suporte/motor/hélice** — a força de empuxo na extremidade do braço vem de um
conjunto originalmente projetado para drones FPV racing quadcopter, escolhido pela
eficiência e desempenho em ambientes dinâmicos.

**Componentes resistivos e capacitivos** — um filtro RC série melhora a qualidade do sinal
do sensor (potenciômetro) antes da leitura pelo microcontrolador.

## Montagem do protótipo

**Parte física** — o protótipo foi projetado para ser desmontável, facilitando o transporte:
a estrutura tem três componentes com pontos de conexão estratégicos, e o braço pode ser
desacoplado no ponto de pivô, onde se conecta ao eixo do potenciômetro. A estrutura montada
se mostrou estável, com rigidez suficiente para evitar vibrações indesejadas no braço
durante o acionamento.

**Parte elétrica** — o microcontrolador gera o sinal de controle PWM, lê o sinal filtrado do
potenciômetro e se comunica com o computador via porta serial. O driver L298N é alimentado
pela fonte de 5 V e amplifica o sinal de controle aplicado ao motor CC série, gerando a
variação angular do braço por meio do empuxo das hélices — o que, por sua vez, altera a
leitura do potenciômetro, fechando a malha.

<br/>