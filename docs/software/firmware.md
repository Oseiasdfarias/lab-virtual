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

## Um ciclo do laço principal

Enquanto a interface não envia o comando de execução, o `loop()` só verifica se chegaram
dados pela serial. Depois do comando, cada iteração segue o caminho abaixo — o ramo de malha
fechada ou o de malha aberta, conforme a configuração recebida da interface:

```mermaid
flowchart TD
  A{"executar?"}
  A -- não --> R["lê a serial, se houver dados"] --> A
  A -- sim --> B["analogRead: tensão do potenciômetro"]
  B --> C["converte_escala: ângulo θ em graus"]
  C --> D{"malha fechada?"}
  D -- sim --> E["gera a referência<br/>quadrada · seno · dente de serra"]
  E --> F["erro = referência − (θ − 31)"]
  F --> G["PID: u = P + I + D"]
  G --> H["ciclo PWM ← u + offset"]
  D -- não --> I["entrada = PRBS"]
  I --> J["ciclo PWM ← PRBS"]
  H --> K["ledcWrite: aplica o PWM ao motor"]
  J --> K
  K --> L["envia 7 valores pela serial"]
  L --> M["delay(1000 · Ts)"]
  M --> N["lê a serial, se houver dados"]
  N --> O["t += Ts"]
  O --> A
```

O intervalo entre iterações é imposto pelo `delay(1000 · Ts)` no fim do laço, com
`Ts = 0,02` s; o tempo `t` enviado à interface avança de `Ts` em `Ts`.

## Protocolo serial

A comunicação usa 115200 baud. No sentido interface → firmware, cada comando é um único
número, lido com `Serial.parseFloat()` e interpretado pela faixa em que cai: três faixas
carregam valores contínuos (amplitude, frequência e offset, reescalados no firmware) e os
demais são códigos fixos. No sentido firmware → interface, cada iteração envia uma linha com
7 valores separados por vírgula — a mesma ordem das colunas descrita em
[Excitação e Aquisição](../identificacao/excitacao.md#formato-dos-dados-coletados).

```mermaid
%%{init: {"themeVariables": {"actorLineColor": "#8e8e90", "signalColor": "#8e8e90", "labelBoxBorderColor": "#8e8e90"}}}%%
sequenceDiagram
  participant GUI as Interface gráfica
  participant ESP as Firmware (ESP32)
  Note over GUI,ESP: Configuração — um número por comando, em qualquer ordem
  GUI->>ESP: entre 1000 e 2001 · amplitude
  GUI->>ESP: entre 2001 e 3001 · frequência
  GUI->>ESP: entre 3001 e 4001 · offset
  GUI->>ESP: 7000 / 8000 / 9000 · dente de serra / seno / quadrada
  GUI->>ESP: 10000 / 11000 · malha fechada / malha aberta
  GUI->>ESP: 12000 · executar
  loop a cada iteração do laço
    ESP->>GUI: referência + 31, ângulo, erro, controle, entrada, entrada, t
    opt se houver dados na serial
      GUI->>ESP: novo parâmetro (mesma codificação)
    end
  end
```

Não existe código de parada: uma vez recebido o `12000`, o firmware continua executando o
laço até ser reiniciado. Os ganhos do PID também não fazem parte do protocolo — são fixos
no código (ver [Controlador PID](../controle/pid.md#ganhos)).

<br>