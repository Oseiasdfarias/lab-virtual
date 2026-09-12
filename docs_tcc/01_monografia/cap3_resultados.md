---
fonte: revisao_tcc/Template_TCC_FEE/Capitulos/Cap_3_Resultados_e_Discussoes.tex
gerado_em: 2026-09-12
---

## Estrutura do capítulo

1. Desenvolvimento do protótipo e softwares (síntese, sem dados novos).
2. Identificação de sistema aplicada ao Aeropêndulo.
3. Ensaio em malha fechada com controlador PID.

## 1. Síntese de desenvolvimento

Declara que protótipo físico e softwares foram desenvolvidos "de forma exitosa" a partir de pesquisa bibliográfica e criativa, referenciando as figuras do protótipo e dos softwares (interface, gêmeo digital, arquitetura do firmware).

## 2. Identificação de sistema aplicada ao Aeropêndulo

Base teórica: TCC de Klarissa Souza (UFPA-Tucuruí). Objetivo do ensaio: validar o correto funcionamento do sistema desenvolvido (não é uma análise quantitativa formal — o texto explicita isso mais adiante).

### Ensaio / sinal de excitação

- Sinal **PRBS** (Pseudo-Random Binary Sequence) gerado no microcontrolador, convertido em PWM, aplicado à entrada do driver L298N.
- Parâmetros: amplitude 0,3V, frequência fundamental 0,4Hz, período de amostragem 0,02s, offset de 1V (ponto de operação).
- Saída medida: ângulo do braço via potenciômetro (3.3V/GND do ESP32, terceiro fio em entrada analógica).

### Pipeline de identificação (mínimos quadrados)

Passos documentados no texto:
1. Obter dados entrada/saída do sistema.
2. Dividir dados: **60% identificação / 40% validação**.
3. Definir estrutura da função de transferência discreta.
4. Definir matriz de regressão.
5. Encontrar vetor de coeficientes por mínimos quadrados (`θ = (MᵀM)⁻¹ Mᵀ y`).
6. Substituir coeficientes na função de transferência.
7. Validar com dados reais.

Ferramentas: Python (NumPy, Pandas, Matplotlib, biblioteca `control`). Código-fonte incluído no texto (carregamento CSV, remoção de offset/transitório, montagem de matriz de regressão, `np.linalg.inv`, `ct.tf`, `ct.forced_response`).

### Resultado 1 — modelo de 2ª ordem

- Estrutura: `H(z) = (b1 z⁻¹ + b2 z⁻²) / (1 + a1 z⁻¹ + a2 z⁻²)`.
- Coeficientes obtidos (dt = 0,019s): `Hz = (-0,002602 z² + 0,004962 z + 0,0163) / (z² - 1,176 z + 0,1849)`.
- **Resultado: falhou** — "a saída da simulação não corresponde de forma aceitável com a dinâmica do sinal de saída do sistema real... o modelo não foi robusto o suficiente".

### Resultado 2 — modelo de 10ª ordem

- Estrutura ajustada para `na=10`, `nb=4` regressores.
- Coeficientes obtidos (dt = 0,02s), numerador de 3ª ordem / denominador de 10ª ordem (valores numéricos completos no texto).
- **Resultado: validado qualitativamente** — "pode-se concluir que o modelo proposto... teve êxito", mas o texto reconhece que "ao modelar sistemas reais sempre haverá erro" devido a não linearidades de sensores/atuadores; o modelo é "apenas uma aproximação".
- **Nenhuma métrica quantitativa de erro foi de fato calculada.** Há uma frase comentada (`%`) no próprio `.tex` mencionando "Erro Quadrático Médio (EQM)" que **não chegou a ser aplicado/reportado** — indício de que a análise quantitativa planejada não foi concluída.

## 3. Ensaio em malha fechada com controlador PID

- Controlador PID simples implementado no firmware (biblioteca `controlador_pid`), com requisito único: erro nulo para entrada degrau.
- **Sintonia**: tentativa e erro (não é um método formal como Ziegler-Nichols). Ganhos finais: **Kp = 0,02; Ki = 0,055; Kd = 0,35**.
- **Ensaio 1 — onda quadrada**: frequência 0,5Hz, amplitude 15°, offset 1V. Sistema rastreia a referência; observa-se transitório nas extremidades da onda (picos do sinal de erro nas transições). Gêmeo digital consome o ângulo real em tempo real durante o ensaio.
- **Ensaio 2 — onda dente de serra**: mesmo comportamento — rastreamento com transitório nas extremidades, similar ao degrau.
- Nenhum valor quantitativo de erro, overshoot ou tempo de acomodação é reportado numericamente no texto — a validação é apresentada de forma qualitativa/gráfica (figuras).

## Resumo de resultados quantitativos citados

| Item | Valor |
|---|---|
| Amplitude sinal PRBS | 0,3 V |
| Frequência fundamental PRBS | 0,4 Hz |
| Período de amostragem (ensaio PRBS) | 0,02 s (dt=0,019s no ajuste do modelo de 2ª ordem) |
| Offset (ponto de operação) | 1 V |
| Divisão dados identificação/validação | 60% / 40% |
| Ordem do modelo que falhou | 2ª ordem |
| Ordem do modelo validado (qualitativo) | 10ª ordem |
| Kp / Ki / Kd (PID) | 0,02 / 0,055 / 0,35 |
| Frequência onda quadrada (malha fechada) | 0,5 Hz |
| Amplitude onda quadrada (malha fechada) | 15° |
| Offset onda quadrada (malha fechada) | 1 V |
| Métrica de erro quantitativa (RMSE/EQM) | **Não calculada** (mencionada apenas em comentário no código-fonte, não aplicada) |
