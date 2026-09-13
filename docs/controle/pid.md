---
title: Controlador PID
---

# Controlador PID

Com o [modelo identificado](../identificacao/validacao.md) validado, o próximo passo é
projetar um controlador que leve o ângulo do Aeropêndulo até a referência desejada e o
mantenha lá, rejeitando perturbações.

## Por que PID

O PID é a escolha natural para essa planta: o termo proporcional reage ao erro atual,
empurrando o ângulo na direção da referência; o termo integral elimina o erro em regime
permanente, compensando efeitos como o peso da haste que um termo puramente proporcional
não zera; e o termo derivativo antecipa a tendência do movimento, amortecendo a resposta e
reduzindo oscilação. Além disso, rodar um PID em um microcontrolador de baixo custo com
atualização a cada 20 ms é barato computacionalmente, o que o torna viável para um sistema
embarcado como o do Aeropêndulo.

## Implementação no firmware

A cada iteração, o controlador calcula os três termos e os soma para obter o sinal de
controle:

$$
P = K_p \cdot e[k] \qquad
I \mathrel{+}= K_i \cdot e[k] \cdot T_s \qquad
D = K_d \cdot \frac{\theta[k-1] - \theta[k]}{T_s}
$$

$$
u[k] = P + I + D
$$

Onde $e[k]$ é o erro (referência − ângulo medido), $\theta[k]$ o ângulo medido na amostra
atual, $T_s=0,02$s o período de amostragem.

Um detalhe importante: a derivada usa a diferença de **ângulo medido** ($\theta[k-1] -
\theta[k]$) entre duas amostras, não a diferença do erro. Derivar o erro amplificaria
mudanças bruscas de referência — um "degrau" na referência viraria um pico artificial no
termo derivativo, o chamado *derivative kick*. Como o termo D deriva a medida em vez do
erro, uma mudança repentina na referência não afeta diretamente o termo derivativo.

## Ganhos

| Ganho | Valor |
| ----- | ----- |
| $K_p$ | 0,02  |
| $K_i$ | 0,055 |
| $K_d$ | 0,35  |

Esses ganhos são fixos em tempo de compilação (`PID mypid(0.02, 0.055, 0.35);` em
`main.cpp`) — mudar um ganho exige recompilar e regravar o microcontrolador. A
[Interface Gráfica](../software/interface-grafica.md) configura outros parâmetros em tempo
real — amplitude, frequência, offset, forma de onda de referência, malha aberta/fechada —
mas não os ganhos do PID.

## Onde está o código

O controlador está implementado em
[`controlador_pid.cpp`](https://github.com/Oseiasdfarias/lab-virtual/blob/main/softwares_aeropendulo/firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos/lib/controlador_pid/src/controlador_pid.cpp)
e é chamado a cada iteração do loop principal do [firmware](../software/firmware.md).

---

**Ver também:** [← Validação do Modelo](../identificacao/validacao.md) ·
[Resultados em Malha Fechada →](resultados.md)
