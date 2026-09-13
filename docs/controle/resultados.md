---
title: Resultados em Malha Fechada
---

# Resultados em Malha Fechada

![Estrutura do controlador PID em malha fechada](img/estrutura-pid-1.png)

O diagrama acima resume a malha: a referência $\theta'$ é comparada com o ângulo medido
$\theta$, gerando o erro $e(t)$ que alimenta em paralelo os três termos do
[controlador PID](pid.md) ($K_p$, $K_i$ e $K_d$); a soma dos três é o sinal de controle
aplicado ao Aeropêndulo, cuja saída realimenta a malha.

## O que foi testado

Com o [modelo identificado](../identificacao/validacao.md) validado e o controlador PID
implementado no firmware, a interface gráfica foi usada para fechar a malha e aplicar dois
sinais de referência ao Aeropêndulo: uma onda quadrada (frequência de 0,5 Hz, amplitude de
15° e offset de 1V) e uma onda dente de serra. Em ambos os ensaios, o ângulo real do braço
-- medido pelo potenciômetro -- foi comparado com o sinal de referência, enquanto o gêmeo
digital consumia esse mesmo sinal angular em tempo real para exibir a dinâmica do sistema
graficamente.

## O que funcionou

Nos dois ensaios, a saída rastreia a referência: o ângulo medido acompanha tanto a onda
quadrada quanto a dente de serra, com o erro tendendo a zero graças ao termo integral do
controlador -- consistente com o que a teoria de controle prevê para um PID bem ajustado, e
com o requisito de projeto do controlador, que era justamente erro nulo em regime para uma
entrada do tipo degrau. Um detalhe honesto observado nos dois sinais: aparece um transitório
nas extremidades da forma de onda (visível como um aumento do sinal de erro nesses pontos),
análogo ao que se espera de uma resposta a um degrau.

## Métricas a partir dos ensaios gravados

A monografia avaliou a malha fechada de forma **qualitativa**, pela inspeção dos gráficos.
Entre os [dados de ensaio](https://github.com/Oseiasdfarias/lab-virtual/tree/main/softwares_aeropendulo/src_interface/dados_de_ensaio)
há dois ensaios completos em malha fechada, ambos com referência em onda quadrada entre 0° e
10°: `arquivo_13_9_2023_23_48_56.csv` (troca a cada 2,5 s) e
`arquivo_14_9_2023_20_31_13.csv` (troca a cada 3,3 s). Os parâmetros desses arquivos não são
os citados no texto da monografia (0,5 Hz e 15°), e não há ensaio com dente de serra
gravado; as métricas abaixo valem, portanto, para esses dois ensaios.

Cada troca de nível foi tratada como um degrau de ±10°. Os valores são a **mediana** dos
degraus de cada ensaio:

| Ensaio | Degrau | Sobressinal | Tempo de subida (10–90 %) | Acomodação (±5 %) | Erro em regime |
| --- | --- | :---: | :---: | :---: | :---: |
| 13/09/2023 (42 degraus) | subida | 5,8 % | 0,64 s | 1,36 s | 0,27° |
| 13/09/2023 | descida | 25,5 % | 0,40 s | 1,40 s | 0,91° |
| 14/09/2023 (25 degraus) | subida | 5,9 % | 0,44 s | 2,66 s | 0,29° |
| 14/09/2023 | descida | 26,9 % | 0,34 s | 1,76 s | 0,51° |

O comportamento é assimétrico: ao erguer o braço, o sobressinal fica perto de 6 %; ao
baixá-lo, com a gravidade a favor, passa de 25 %. O erro residual fica abaixo de 1°, medido
nos últimos 20 % de cada janela de 2,5 a 3,3 s entre trocas.

Essas métricas são uma análise posterior à defesa, com os ganhos e o termo derivativo da
época dos ensaios. O script que as reproduz está em
[`metricas_malha_fechada.py`](https://github.com/Oseiasdfarias/lab-virtual/blob/main/materiais_complementares/analise_malha_fechada/metricas_malha_fechada.py),
e as definições de cada métrica estão no cabeçalho do arquivo.

## Trabalhos futuros sugeridos

O Cap. 4 da monografia aponta como próximos passos imediatos a documentação online (este
próprio site) e vídeos explicativos, mantendo o projeto como código aberto. Como
possibilidades de pesquisa a partir da plataforma já validada, o texto sugere explorar
outros métodos de identificação de sistemas, projetar controladores por abordagens
clássicas ou por inteligência artificial -- incluindo aprendizagem por reforço e deep
Q-learning -- e expandir o laboratório virtual com novas funcionalidades tanto na interface
gráfica quanto no protótipo físico.
