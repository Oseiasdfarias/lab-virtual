---
title: Arquitetura do Sistema
---

# Arquitetura do Sistema

O sistema é composto por quatro subsistemas que operam de forma integrada: protótipo
físico, firmware, interface gráfica e gêmeo digital.

![Diagrama do ecossistema do Aeropêndulo](img/diagrama-ecossistema-1.png)

## Como os dados fluem

O laço de controle roda inteiramente dentro do firmware, a cada período de amostragem: o
microcontrolador lê a tensão do potenciômetro pelo conversor A/D, converte essa leitura
para o ângulo da haste, calcula o sinal de referência (onda quadrada, senoidal ou dente de
serra, conforme o modo selecionado), obtém o erro em relação ao ângulo medido, executa o
controlador PID e converte o sinal de controle resultante em ciclo de trabalho do sinal
PWM que aciona o motor CC. Esse laço fechado — sensor, PID e atuação — não depende da
comunicação serial para funcionar.

A cada iteração, o firmware também envia pela porta serial os sinais do ciclo — referência,
ângulo, erro, sinal de controle e tempo — para a interface gráfica, que os usa para
atualizar os gráficos em tempo real. Quando o gêmeo digital está habilitado, a interface
repassa esses mesmos dados para a classe `Simulador`, dentro do mesmo processo Python, que
atualiza a animação 3D e os gráficos do gêmeo digital.

O caminho de volta carrega apenas dados de configuração: a interface envia ao firmware os
parâmetros do sinal de referência (amplitude, frequência, offset), a forma de onda
selecionada, o modo de operação (malha aberta ou malha fechada) e o comando de
início/parada do ensaio. Os ganhos do controlador PID não trafegam pela porta serial —
permanecem fixos no firmware.

## Por que essa divisão

O controle roda no firmware, e não no computador, porque o laço fechado — leitura do
potenciômetro, cálculo do erro, PID e atuação por PWM — precisa executar em um período de
amostragem curto e regular, sem ficar sujeito à latência e às variações de tempo da
comunicação serial ou do sistema operacional do computador; por isso a porta serial carrega
apenas leituras de estado e comandos de configuração, nunca a atuação em si. Já a interface
gráfica e o gêmeo digital são dois módulos Python que rodam no mesmo processo, e não em
processos separados que trocam mensagens pela rede: a classe `Simulador` é instanciada
junto com a interface e passada a ela como parâmetro, que passa a chamar os métodos dessa
classe diretamente a cada novo dado recebido do protótipo — uma chamada de método dentro do
mesmo programa, mais simples e mais rápida do que uma comunicação via rede entre processos
independentes.
