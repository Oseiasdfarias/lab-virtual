---
title: Validação do Modelo
---

# Validação do Modelo

Depois de estimar os coeficientes (ver [Estimação por Mínimos Quadrados](estimacao.md)), é
preciso confirmar que o modelo reproduz a dinâmica real. O teste usado aqui é a validação
por simulação livre: a entrada $u(n)$ do ensaio inteiro é aplicada à função de
transferência discreta obtida, gerando uma saída simulada que é então sobreposta à saída
real $y(n)$. Como os coeficientes foram estimados só com as primeiras 60% das amostras, o
trecho final de 40% — marcado como "Dados de Validação" nos gráficos — mostra o modelo
diante de dados que a estimação não usou.

## Modelo de 2ª ordem: insuficiente

![Validação do modelo de segundo grau](img/validacao-2grau-1.png)

O gráfico superior mostra a entrada PRBS aplicada; o inferior compara a saída real (azul,
mais grossa) com a saída simulada pelo modelo de 2ª ordem (preta). O modelo acompanha o
período das oscilações, mas não a sua forma: onde a saída real tem picos mais arredondados
e, em vários trechos, um duplo lóbulo por ciclo, a saída simulada produz picos mais agudos e
de amplitude maior — por exemplo, perto de $t \approx 6\,$s e $t \approx 12,5\,$s, o modelo
chega a quase 0,13 enquanto a saída real fica em torno de 0,09-0,10. Essa divergência de
forma e amplitude, repetida ao longo de todo o ensaio, foi a evidência visual que motivou
subir a ordem do modelo.

## Modelo de 10ª ordem: aceitável

![Validação do modelo de décima ordem](img/validacao-10grau-1.png)

Com a estrutura de 10ª ordem, a saída simulada acompanha de forma bem mais próxima a saída
real ao longo de todo o intervalo mostrado: os picos e vales coincidem em amplitude e em
instante de tempo, inclusive nos trechos em que o modelo de 2ª ordem havia divergido mais.
O modelo identificado ainda não reproduz a pequena ondulação de alta frequência presente na
saída real (visível como um leve serrilhado sobre a curva azul), mas captura bem a dinâmica
dominante do sistema, o que a monografia considerou suficiente para encerrar a etapa de
identificação.

## Métricas de ajuste

A monografia apresenta esta validação de forma **qualitativa**, pela comparação visual dos
gráficos. O notebook de identificação, porém, já calculava o ajuste NRMSE sobre o trecho de
validação, e os números abaixo foram reproduzidos a partir do mesmo arquivo de ensaio
(`arquivo_9_9_2023_13_33_24.csv`) — os coeficientes recalculados coincidem com os do
notebook:

$$
\text{NRMSE} = \left(1 - \frac{\lVert y - \hat{y} \rVert}{\lVert y - \bar{y} \rVert}\right) \times 100\,\%
$$

em que $y$ é a saída real, $\hat{y}$ a saída simulada e $\bar{y}$ a média da saída real, tudo
restrito às 40% de amostras de validação. O RMSE está em graus, sobre o sinal sem o offset.

| Modelo | NRMSE | RMSE |
| --- | --- | --- |
| 2ª ordem | 51,35 % | 1,62° |
| 10ª ordem, montada como na monografia | 55,97 % | 1,47° |
| 10ª ordem, montada como a equação de diferenças estimada | 78,30 % | 0,72° |

A segunda linha corresponde à função de transferência publicada, que inclui o atraso de 7
amostras descrito em [Estimação por Mínimos Quadrados](estimacao.md#resultado); a figura de
10ª ordem acima também foi gerada com ela. Com o numerador completado com zeros — ou seja,
simulando exatamente o modelo que os mínimos quadrados ajustaram —, o ajuste sobe para
78,30 % e o erro médio cai pela metade.

Essas métricas são uma análise posterior à defesa e não fazem parte da monografia. O script
que as reproduz está em
[`metricas_validacao.py`](https://github.com/Oseiasdfarias/lab-virtual/blob/main/materiais_complementares/Identificacao_de_Sistemas/identificacao_aeropendulo/ident_up/metricas_validacao.py).
