---
fonte: revisao_tcc/Template_TCC_FEE/Capitulos/2_aeropendulo/2_1_descricao.tex, revisao_tcc/Template_TCC_FEE/Capitulos/2_aeropendulo/2_2_fundamentacao_teorica.tex, revisao_tcc/Template_TCC_FEE/Capitulos/2_aeropendulo/2_3_modelagem_analitica.tex, revisao_tcc/Template_TCC_FEE/Capitulos/2_aeropendulo/2_4_modelagem_identificacao_sistemas.tex, revisao_tcc/Template_TCC_FEE/Capitulos/Cap_2_Desenvolvimento.tex
gerado_em: 2026-09-12
---

## Status de inclusão no documento final

`Cap_2_Desenvolvimento.tex` só faz `\input` de **2_2 (fundamentação teórica)** e **2_3 (modelagem analítica)**. Os arquivos **2_1 (descrição)** e **2_4 (identificação de sistemas)** estão com o `\input` comentado, ou seja, **não aparecem no PDF final**. Resumidos abaixo por completude, mas sinalizados como não usados.

## 2.1 Descrição do sistema — `2_1_descricao.tex`

**Conteúdo real do arquivo: apenas o texto `teste` repetido 4 vezes.** É um placeholder nunca escrito. Não incluído no PDF.

## 2.2 Fundamentação teórica — `2_2_fundamentacao_teorica.tex` (incluído no PDF)

- Descreve o Aeropêndulo como sistema de 1 grau de liberdade (ângulo θ do braço), controlado pelo empuxo das hélices, que depende da velocidade angular do motor CC série acoplado ao braço.
- Sistema tratado como entrada (tensão no motor) → saída (ângulo θ).
- Fundamentação teórica geral sobre modelagem matemática de sistemas dinâmicos, citando Ogata (5ª ed.): modelo matemático = conjunto de equações que representa a dinâmica do sistema com razoável precisão; menciona que sistemas mecânicos/elétricos/térmicos/econômicos/biológicos seguem leis físicas específicas (Newton, Kirchhoff etc).
- **Este arquivo é curto** — praticamente uma introdução de 2 parágrafos; não desenvolve a fundamentação em profundidade nem cobre identificação de sistemas.

## 2.3 Modelagem analítica — `2_3_modelagem_analitica.tex` (incluído no PDF)

Modelagem via decomposição em subsistemas: **braço do Aeropêndulo** + **motor CC série**, depois unidos.

### Modelo do braço (baseado em Mohammadbagheri & Yaghoobi, "amin" no .bib)

- Equação de Newton/momento angular: `F_e = J_b θ'' + c θ' + m g d sin(θ)`, onde F_e = empuxo da hélice, J_b = momento de inércia do braço, c = amortecimento viscoso, m = massa, d = distância centro de massa–pivô.
- Relação não linear empuxo-velocidade angular da hélice `F_e = K_m ω²`, aproximada linearmente por `F_e = K_m ω`.
- Linearização em torno de pequenas variações (`sin θ ≈ θ`).
- Aplicação de Laplace → função de transferência do braço: `θ(s)/F_e(s) = 1/(J_b s² + c s + m g d)`.
- Combinando com a relação linear do empuxo: `H(s) = θ(s)/ω(s) = (K_m/J_b) / (s² + (c/J_b)s + (mgd/J_b))`.

### Modelo do motor CC série (baseado em Liceaga-Castro et al., "jesus" no .bib)

- Motor CC série: enrolamento de campo em série com o de armadura (`i = i_f = i_a`); alto torque de partida, regulação de velocidade ruim (cita Umans 2014, p. 410).
- Parte mecânica: `J_m ω' = T_e - b ω - T_c` (torque eletromagnético, amortecimento viscoso, torque de carga).
- Relações de fluxo/torque: `E_a = ω Φ(i)`, `T_e = i Φ(i)`, com aproximação linear `Φ(i) = K_0 i` → torque não linear `T_e = K_0 i²`.
- Parte elétrica (Kirchhoff): `V = (R_a+R_f) i + (L_a+L_f) di/dt + E_a`, com `R = R_a+R_f`, `L = L_a+L_f`.
- Modelo não linear final: acoplamento das equações mecânica (`K_0 i² = J_m ω' + b ω + T_c`) e elétrica (`V = R i + L di/dt + ω' K_0 i`).
- **Linearização**: variáveis de estado `x1 = ω`, `x2 = i`; representação em espaço de estados não linear `ẋ1 = a1 x2² - a2 x1 - a3 Tc`, `ẋ2 = -b1 x2 - b2 x1 x2 + b3 V`.
- Ponto de equilíbrio encontrado zerando as derivadas; jacobiano calculado para obter matrizes A, B, C linearizadas (`ẋ = Ax+Bu`, `y = Cx`).
- Caso particular com torque de carga nulo (`T_c=0`) simplifica as expressões.
- Função de transferência final linearizada: `G(s) = ω'(s)/V(s) = C(sI-A)^{-1}B`, resultando em uma expressão de 2ª ordem em função dos parâmetros físicos do motor (K_0, J_m, L, R, b, x1⁰).

### Junção dos subsistemas

- Combinação do modelo do motor (entrada: tensão V; saída: velocidade angular ω) com o modelo do braço (entrada: ω; saída: θ) → modelo completo tensão→ângulo.
- O texto reconhece a **dificuldade prática de obter numericamente parâmetros físicos** como o momento de inércia do eixo do motor (J_m) e o coeficiente de amortecimento viscoso do pivô (c) — esse é o gancho de transição/justificativa para o método de identificação de sistemas usado no Capítulo 3.

## 2.4 Modelagem por identificação de sistemas — `2_4_modelagem_identificacao_sistemas.tex` (NÃO incluído no PDF)

Conteúdo integral do arquivo (2 linhas):

> "Segundo Aguirre (2004), a identificação de sistemas se propõe a obter um modelo matemático que explique, pelo menos em parte e de forma aproximada, a relação de causa e efeito presente nos dados... CONTINUA ..."

Arquivo abandonado/incompleto. **O método de identificação de sistemas efetivamente usado no trabalho (mínimos quadrados, sinal PRBS, função de transferência discreta) está descrito de forma completa no Capítulo 3 (Resultados e Discussões)**, não neste capítulo teórico — ver `cap3_resultados.md`.

## Métodos de identificação de sistemas usados (resumo, detalhado em cap3_resultados.md)

- Sinal PRBS aplicado em malha aberta como excitação de entrada.
- Separação de dados 60% identificação / 40% validação.
- Estimação por **mínimos quadrados** de função de transferência discreta.
- Testado com estrutura de 2ª ordem (falhou na validação) e de 10ª ordem (validação qualitativa aceitável).
- Base teórica citada: Aguirre (2004) e o TCC de Klarissa Souza (UFPA-Tucuruí, 2023, identificação não-linear em espaço de estados por regressão esparsa).
