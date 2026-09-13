---
title: Estimação por Mínimos Quadrados
---

# Estimação por Mínimos Quadrados

Com os dados de [excitação e aquisição](excitacao.md) em mãos, o próximo passo é ajustar
os parâmetros de um modelo discreto que reproduza a relação entrada/saída observada.

## Por que um modelo discreto (não o modelo analítico)

O modelo obtido na [Modelagem Matemática](../modelagem/index.md) é contínuo e linearizado —
uma aproximação válida numa vizinhança do ponto de operação, deduzida a partir das leis da
física. O modelo identificado aqui é outra coisa: é discreto, o que é natural já que os
dados de ensaio são amostrados a um período de amostragem fixo, e não depende de conhecer
de antemão nenhum parâmetro físico do sistema. Em vez de partir de torques, massas e
constantes do motor, o modelo discreto "aprende" a dinâmica direto dos dados — o que inclui,
de quebra, efeitos que o modelo analítico não captura, como atrito seco e folga mecânica no
pivô do braço.

## Primeira tentativa: modelo de 2ª ordem

O candidato natural para a ordem do modelo discreto é a mesma ordem do modelo analítico:
segunda ordem, com dois coeficientes no numerador e dois no denominador. Ajustando esses
coeficientes pelo método dos mínimos quadrados aos dados de identificação, chega-se à
função de transferência discreta:

$$
Hz = \frac{-0{,}002602z^2+0{,}004962z+0{,}0163}{z^2-1{,}176z+0{,}1849}
$$

Na prática, porém, esse modelo não aproximou bem a dinâmica real do Aeropêndulo — ver
[Validação do Modelo](validacao.md) para o motivo qualitativo. O grau escolhido, embora
coerente com a física do sistema, não é suficiente para descrever o comportamento
observado nos dados, o que motivou tentar uma ordem mais alta.

## Estrutura ARX de 10ª ordem

Depois de alguns testes, uma estrutura de décima ordem se mostrou capaz de aproximar bem a
dinâmica real. Em forma simbólica, a função de transferência discreta é:

$$
H(z) = \frac{b_1z^{-1}+b_2z^{-2}+b_3z^{-3}+b_4z^{-4}}{1+a_1z^{-1}+a_2z^{-2}+a_3z^{-3}+a_4z^{-4}+a_5z^{-5}+a_6z^{-6}+a_7z^{-7}+a_8z^{-8}+a_9z^{-9}+a_{10}z^{-10}}
$$

O numerador tem 4 coeficientes ($b_1$ a $b_4$) e o denominador tem 10 ($a_1$ a $a_{10}$) —
daí a estrutura ser chamada de décima ordem. Cada termo $z^{-n}$ representa um atraso de
$n$ amostras: $z^{-1}$ é o valor da amostra anterior, $z^{-2}$ o de duas amostras atrás, e
assim por diante. Ao todo, são 14 coeficientes a determinar a partir dos dados.

## Montando o problema de mínimos quadrados

Para encontrar esses 14 coeficientes, o problema é reescrito como uma regressão linear.
Cada linha de uma matriz $M$ de regressores reúne amostras passadas da saída ($y[k-1]$ até
$y[k-10]$, correspondendo aos termos do denominador) e da entrada ($u[k]$ até $u[k-3]$,
correspondendo aos termos do numerador). O vetor de coeficientes $\theta$ — os mesmos
$b_1..b_4$ e $a_1..a_{10}$ da estrutura acima — é aquele que minimiza o erro quadrático
entre a saída prevista por essa regressão e a saída real observada nos dados de
identificação. Essa solução tem forma fechada, dada pela equação normal dos mínimos
quadrados ordinários (sem nenhuma regularização):

$$
\theta = (M^TM)^{-1}M^Ty
$$

em que $y$ é o vetor com as amostras reais da saída. Resolver esse sistema é uma operação
de álgebra linear direta, sem iteração nem ajuste manual de hiperparâmetros.

## Resultado

Aplicando a equação normal aos dados de identificação, com período de amostragem
$dt = 0{,}02$ s, obtém-se a função de transferência discreta numérica:

$$
Hz = \frac{-0{,}0029z^3+0{,}0023z^2+0{,}0016z+0{,}0097}{z^{10}-0{,}9z^9-0{,}3z^8-0{,}014z^7+0{,}13z^6+0{,}15z^5+0{,}012z^4-0{,}05z^3-0{,}12z^2-0{,}02z+0{,}15}
$$

Esses 14 números — 4 do numerador e 10 do denominador — são o modelo que de fato foi usado
para [projetar o controlador](../controle/pid.md). A confirmação de que essa escolha de
ordem foi a certa vem da comparação entre a saída simulada por esse modelo e a saída real
do sistema, documentada em [Validação do Modelo](validacao.md).
