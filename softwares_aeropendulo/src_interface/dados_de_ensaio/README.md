# Dados de ensaio

CSVs gravados por `ColetaDados.salvar_dados_colhidos()`
(`src_interface/coleta_dados.py`) com o `to_csv` padrão do pandas: a primeira linha é um
cabeçalho que só numera as colunas (`,0,1,2,3,4,5,6`) e a primeira coluna é o índice de
linha. As 7 colunas seguintes vêm, na mesma ordem, do protocolo serial do firmware
(`enviar_dados_serial()` em
`firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos/lib/ler_escrever_serial/`):

| Coluna | Conteúdo | Unidade |
| --- | --- | --- |
| 0 | Sinal de referência (setpoint), já somado a offset fixo de +31 | graus |
| 1 | Ângulo medido (potenciômetro) | graus |
| 2 | Sinal de erro (`0` em malha aberta) | graus |
| 3 | Sinal de controle antes da conversão para PWM | Volts |
| 4 | Sinal de entrada em malha aberta (PRBS); em malha fechada, mantém o último valor da malha aberta (o firmware não zera a variável) | Volts |
| 5 | Repetição da coluna 4 (reservado para uso futuro, não usado hoje) | Volts |
| 6 | Tempo decorrido do ensaio (passo ≈ 0,02 s) | segundos |

Nome do arquivo: `arquivo_<dia>_<mes>_<ano>_<hora>_<min>_<seg>.csv`, gerado por
`datetime.now()` no momento em que a gravação é desligada na interface gráfica.

## Catálogo dos ensaios

Classificação feita a partir dos próprios dados: em malha aberta, o erro e o sinal de controle
são nulos e a entrada alterna entre dois níveis em intervalos irregulares (PRBS); em malha
fechada, a referência alterna periodicamente entre dois níveis (onda quadrada). A amostragem é
de 0,02 s em todos.

| Arquivo | Malha | Excitação | Duração | Uso na documentação |
| --- | --- | --- | ---: | --- |
| `arquivo_24_6_2023_19_2_54.csv` | aberta | PRBS, 1,0 ↔ 1,5 V | 81 s | — |
| `arquivo_24_6_2023_21_14_28.csv` | aberta | PRBS, 1,0 ↔ 1,5 V | 119 s | — |
| `arquivo_25_6_2023_15_53_41.csv` | aberta | PRBS, 1,0 ↔ 1,5 V | 128 s | — |
| `arquivo_25_6_2023_16_9_10.csv` | aberta | PRBS, 1,0 ↔ 1,3 V | 114 s | — |
| `arquivo_25_6_2023_16_20_28.csv` | aberta | PRBS, 1,0 ↔ 1,3 V | 125 s | — |
| `arquivo_13_8_2023_17_54_0.csv` | fechada | Referência entre −1,0° e −0,8°, trocas a cada 2,5 s | 11 s | — (ensaio curto) |
| `arquivo_9_9_2023_13_33_24.csv` | aberta | PRBS, 1,0 ↔ 1,3 V | 80 s | Identificação do modelo (notebook `ident_up`) |
| `arquivo_13_9_2023_23_48_56.csv` | fechada | Onda quadrada 0° ↔ 10°, trocas a cada 2,5 s | 110 s | Métricas de malha fechada |
| `arquivo_14_9_2023_20_31_13.csv` | fechada | Onda quadrada 0° ↔ 10°, trocas a cada 3,3 s | 86 s | Métricas de malha fechada |

Não há ensaio com referência dente de serra ou senoidal entre os arquivos. Os scripts que usam
esses dados estão em
`materiais_complementares/Identificacao_de_Sistemas/identificacao_aeropendulo/ident_up/metricas_validacao.py`
e `materiais_complementares/analise_malha_fechada/metricas_malha_fechada.py`.

