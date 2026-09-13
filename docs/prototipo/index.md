---
title: Desenvolvimento do Protótipo
author: Oséias Farias

---

<figure markdown="span">
  ![Protótipo do Aeropêndulo](img/prototipo-aeropendulo.jpg)
  <figcaption>Figura 1 — Protótipo do Aeropêndulo.</figcaption>
</figure>

## Lista de materiais

| Item | Especificação | Função |
| --- | --- | --- |
| Estrutura | Chapas de compensado | Base e colunas desmontáveis |
| Braço | Tubo de fibra de carbono 3×3×2 mm | Haste leve entre o pivô e o motor |
| Sensor de ângulo | Potenciômetro de 50 kΩ | Mede o ângulo do braço no pivô |
| Microcontrolador | Placa de desenvolvimento ESP32 (TTGO T1) | Leitura do sensor, controle e comunicação serial |
| Driver de potência | Módulo driver L298N (ponte H) | Aplica ao motor a tensão comandada pelo PWM |
| Conjunto de propulsão | Suporte, motor e hélice para drones FPV racing | Gera o empuxo na ponta do braço |
| Alimentação | Fonte chaveada de 5 V, 25 W | Alimenta o driver e o motor |
| Filtro do sensor | Resistor e capacitor (filtro RC série) | Reduz o ruído do sinal do potenciômetro |

A monografia não informa os valores do resistor e do capacitor do filtro RC. Sobre a fonte, o
título da figura fala em 2 A e o texto em 5 A; os 25 W correspondem a 5 V × 5 A.

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

## Ligações elétricas

<figure markdown="span">
  ![Diagrama de comunicação do aeropêndulo](img/diagrama-comunicacao.png)
  <figcaption>Figura 2 — Diagrama de comunicação do aeropêndulo (monografia, 2023).</figcaption>
</figure>

<figure markdown="span">
  ![Esquema de conexões elétricas do aeropêndulo](img/esquema-eletrico.png)
  <figcaption>Figura 3 — Esquema de conexões elétricas (monografia, 2023).</figcaption>
</figure>

### Pinagem usada pelo firmware

Pinos definidos em `PlatformIo/Esp32_ttgo_modulos/src/main.cpp`, a variante documentada do
[firmware](../software/firmware.md):

| Pino do ESP32 | Constante no firmware | Ligação |
| --- | --- | --- |
| GPIO 2 | `pinAD_POT` | Sinal do potenciômetro (após o filtro RC), lido pelo conversor A/D |
| GPIO 25 | `pinPWM` | ENA do L298N — PWM de 500 Hz, 8 bits |
| GPIO 32 | `pinSentido1` | IN1 do L298N (nível alto: sentido de giro fixo) |
| GPIO 33 | `pinSentido2` | IN2 do L298N (nível baixo) |
| 3,3 V e GND | — | Alimentação do potenciômetro |

!!! warning "Divergência entre o esquema e o firmware"
    No esquema elétrico da Figura 3, o sinal filtrado do potenciômetro chega ao **GPIO 12**;
    no firmware, a leitura é feita no **GPIO 2**. Os pinos do driver (25, 32 e 33) coincidem
    nos dois. Antes de montar um novo protótipo, confirme no hardware qual pino está em uso e
    ajuste o esquema ou a constante `pinAD_POT`.

