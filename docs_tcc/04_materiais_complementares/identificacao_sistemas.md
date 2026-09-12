---
fonte: materiais_complementares/analise_de_sinais/, materiais_complementares/Identificacao_de_Sistemas/ (incl. gerador_sinais/, identificacao_aeropendulo/, "Programa Python/" e "Programa Python/Dados/Ensaio_02,03,04")
gerado_em: 2026-09-12
---

# Identificação de Sistemas

Catálogo de alto nível dos materiais de identificação de sistemas (bancada Motor-Gerador da disciplina de Laboratório de Controle e, depois, o próprio aeropêndulo).

## analise_de_sinais/

2 notebooks de pós-processamento/plotagem de ensaios (não fazem identificação, só análise visual):

- `Analise_sinal_sys_malha_aberta_onda_quadrada.ipynb` — análise do ensaio do aeropêndulo em malha aberta com entrada em onda quadrada; plota sinais de entrada e saída.
- `Analise_sinais_01.ipynb` — análise do ensaio do aeropêndulo com controlador PI; plota sinal de referência/saída e sinal de controle.

## Identificacao_de_Sistemas/

Pasta central da etapa de identificação, com bastante duplicação entre subpastas (vários notebooks se repetem em `identificacao_aeropendulo/` e `identificacao_aeropendulo/ident_up/`, provavelmente versões sucessivas do mesmo trabalho).

### Notebooks na raiz
- `topicos_identificacao_sys.ipynb` — notas/ideias sobre identificação aplicada ao aeropêndulo; menciona proposta de **controle adaptativo** (identificar o sistema por ângulo e ajustar o controlador dinamicamente) — parece anotação exploratória, não implementação concluída.
- `Identificação_LS_e_Otimização_Massa_Mola_Amortecedor.ipynb` — identificação por Mínimos Quadrados (LS) e otimização aplicada a um sistema massa-mola-amortecedor (exemplo didático), com métrica NRMSE.

### gerador_sinais/
- `sinais.ipynb`, `sinais_1.ipynb` — geração de sinais de excitação: senoidal, onda quadrada e PRBS; inclui teste do sinal PRBS e um exemplo de função de transferência discreta obtida (planta Motor/Gerador).

### identificacao_aeropendulo/
Conjunto de relatórios de laboratório (disciplina "Laboratório de Controle 2023.2", Turma T03, Grupo 4 — Andrez, Oséias, Thalia, Hebert) sobre a bancada didática **Motor/Gerador** (não é ainda o aeropêndulo físico final, é a bancada usada para aprender a técnica):

- `Ensaio1-identificacao_aeropendulo.ipynb`, `Ensaio2-identificacao_aeropendulo.ipynb` — identificação por função de transferência pulsada (domínio z).
- `Relatorio_2_Lab_Sistemas_Controle_Controle_P_PI_Final.ipynb`, `Relatorio_3_Implementação_Controlador_P_e_PI.ipynb`, `Relatorio_6_..._Implementacao.ipynb` — projeto e implementação de controladores P e PI para o sistema Motor/Gerador.
- `relatorio_5_prbs.ipynb` — ensaio com sinal PRBS.
- `identificacao_aeropendulo_modelo_lab_controle.ipynb` — relatório de laboratório de controle, mesmo grupo, mesma disciplina.
- `identificacao_aeropendulo copy.ipynb` — cópia de notebook de geração de sinais (PRBS/senoidal/quadrada), com uma FT identificada do sistema Motor/Gerador.
- `Identificação_LS_e_Otimização_Massa_Mola_Amortecedor.ipynb` — duplicata do notebook da raiz.
- `Analise_sinal_sys_malha_aberta_onda_quadrada.ipynb` — duplicata do notebook em `analise_de_sinais/`.

Subpasta `ident_up/` (versão mais avançada/atualizada, já focada no aeropêndulo em si):
- `Ensaio2-identificacao_aeropendulo.ipynb` — parâmetros de ensaio do aeropêndulo.
- `conv_discreta_continua.ipynb` — conversão de função de transferência discreta (z) para contínua (s) via Tustin; valida modelo obtido com RMSE.
- `validacao_modelo.ipynb` — validação do modelo identificado (offset 1V, sinal de referência 0.2 Hz, amplitude 10°, Ts=0.02s); reduz modelo discreto de 5ª ordem a um modelo contínuo de 2ª ordem aproximado.
- `projeto_controlePI.ipynb` — projeto de controlador PI a partir do sistema identificado, com discretização do controlador (transformada z).
- PDFs de apoio (sinais de entrada/saída, PRBS com e sem offset, validação de modelos de 2º e 10º grau, dados de treino/teste) — apenas figuras exportadas dos notebooks acima.

### Programa Python/
Scripts de bancada originais da monitoria (2020, Bolsista Felipe Silveira Piano, Coordenador Cleison Daniel Silva) usados para coletar dados via serial da bancada Motor-Gerador:

- `ensaio_prbs.py`, `ensaio_prbsRTx.py` — geração/envio de sinal PRBS e coleta da resposta via porta serial.
- `malha_aberta.py`, `malha_fechada.py` — ensaios em malha aberta (onda quadrada/dente de serra) e malha fechada.
- `Kp 1.0 - Malha Fechada.py`, `Identificação.py`, `análise gráfica.py` — scripts de identificação e plotagem (nomes com acentuação/encoding quebrado no filesystem).
- `teste.py` — script trivial de teste de plot (não relevante).
- CSVs soltos na raiz (`ensaio.csv`, `ensaio 2.csv`, `ensaio_0307.csv`, `ensaio_0407.csv`) — dados de ensaios avulsos.

#### Programa Python/Dados/
Dados brutos de ensaios PRBS da bancada Motor-Gerador, documentados por `leia-me.txt` (formato: 3 vetores — tempo, entrada, saída — lidos via `pandas.read_csv`):

- `ensaioG1.csv` ... `ensaioG8.csv` — 8 ensaios avulsos (sem metadados individuais além do leia-me geral).
- `Ensaio_01.rar`, `Ensaio_02.rar`/`Ensaio_02/`, `Ensaio_03.rar`/`Ensaio_03/`, `Ensaio_04.rar`/`Ensaio_04/` — ensaios compactados, cada um com pasta extraída e `leia-me.txt` próprio detalhando ponto de operação, amplitude, faixa de excursão, período de amostragem (0,015s) e nº de amostras (1000):
  - Ensaio_02: ponto de operação 2V, faixa 1,5V–2,5V.
  - Ensaio_03: ponto de operação 2,25V, faixa 1,75V–2,75V.
  - Ensaio_04: ponto de operação 2,5V, faixa 2V–3V.
  - (Ensaio_01 não tem leia-me próprio encontrado, só o .rar.)

## Observação geral
Há bastante redundância proposital entre pastas (cópias de notebooks de relatório de disciplina reaproveitados para o TCC). O material evolui de "bancada Motor-Gerador genérica" (disciplina) para "identificação do aeropêndulo propriamente dito" (pasta `ident_up/`), que é o mais próximo do resultado final usado no TCC.
