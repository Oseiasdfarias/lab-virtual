---
fonte: softwares_aeropendulo/src_interface/dados_de_ensaio/*.csv
gerado_em: 2026-09-12
atualizado_em: 2026-09-13
---

# Dados de Ensaio (`src_interface/dados_de_ensaio/`)

## Formato

CSVs gerados por `ColetaDados.salvar_dados_colhidos()` (`src_interface/coleta_dados.py`), via `pandas.DataFrame(self.salvar_dados.T).to_csv(...)`. Não têm cabeçalho com nomes de colunas — a primeira linha é só o índice das 7 colunas de dados (`0..6`) mais a coluna de índice de linha do pandas (primeira coluna sem nome). Exemplo (`arquivo_13_8_2023_17_54_0.csv`):

```
,0,1,2,3,4,5,6
0,30.0,29.67,0.33,5.266,1.3,1.3,79.139
1,30.0,29.538,0.462,5.27,1.3,1.3,79.159
```

**Mapeamento confirmado em 2026-09-13** lendo o código-fonte de
`enviar_dados_serial()` em
`firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos/lib/ler_escrever_serial/src/ler_escrever_serial.cpp`
(chamada em `main.cpp`) — a ordem dos `Serial.print` bate exatamente com as 7 colunas lidas
por `coleta_dados.py` (`dados1.split(",")` → array de 7 floats):

| Coluna | Conteúdo | Unidade | Origem no firmware |
| --- | --- | --- | --- |
| 0 | Sinal de referência (setpoint), **já somado a um offset fixo de +31** | graus | `*sinal_ref + 31` |
| 1 | Ângulo medido (saída do potenciômetro, convertido em `Conversor::converte_escala`) | graus | `*theta_saida` |
| 2 | Sinal de erro (`sinal_ref - (theta_saida - 31)` em malha fechada; `0` em malha aberta) | graus | `*erro` |
| 3 | Sinal de controle **antes** da conversão para ciclo PWM | Volts | `*sinal_controle` |
| 4 | Sinal de entrada em malha aberta (PRBS, `OndaPrbs::onda_prbs()`); em malha fechada, mantém o último valor da malha aberta (o firmware não zera a variável) | Volts | `*sinal_entrada_ma` (o parâmetro da função chama-se `ampl`, mas quem chama passa `sinal_entrada_ma` — nome interno enganoso) |
| 5 | **Repetição exata da coluna 4** — o firmware imprime a mesma variável duas vezes; comentário no código diz "estruturas reservas de envio de dados" (reservado para uso futuro, não usado hoje) | Volts | `*ampl` (mesmo valor da coluna 4) |
| 6 | Tempo decorrido do ensaio, incrementos de `Ts = 0,02` s | segundos | `*t` |

**Ressalva:** essa é a variante de firmware mais completa e atual do repositório
(`Esp32_ttgo_modulos`), confirmada por leitura de código. Os 9 arquivos de ensaio são de
2023 (jun–set) e podem ter sido gravados com uma versão anterior do firmware — o mapeamento
acima é a melhor fonte disponível, mas não foi possível confirmar bit a bit contra o
firmware exato que rodava em cada data.

## Arquivos disponíveis (9 ensaios)

| Arquivo | Data/Hora (extraída do nome) | Tamanho |
|---|---|---|
| `arquivo_24_6_2023_19_2_54.csv` | 24/06/2023 19:02:54 | 154 KB |
| `arquivo_24_6_2023_21_14_28.csv` | 24/06/2023 21:14:28 | 231 KB |
| `arquivo_25_6_2023_15_53_41.csv` | 25/06/2023 15:53:41 | 246 KB |
| `arquivo_25_6_2023_16_9_10.csv` | 25/06/2023 16:09:10 | 219 KB |
| `arquivo_25_6_2023_16_20_28.csv` | 25/06/2023 16:20:28 | 241 KB |
| `arquivo_13_8_2023_17_54_0.csv` | 13/08/2023 17:54:00 | 24 KB (bem menor — ensaio curto) |
| `arquivo_9_9_2023_13_33_24.csv` | 09/09/2023 13:33:24 | 152 KB |
| `arquivo_13_9_2023_23_48_56.csv` | 13/09/2023 23:48:56 | 245 KB |
| `arquivo_14_9_2023_20_31_13.csv` | 14/09/2023 20:31:13 | 193 KB |

Nome do arquivo segue o padrão `arquivo_<dia>_<mes>_<ano>_<hora>_<min>_<seg>.csv`, gerado por `datetime.now()` no momento em que a gravação é desligada na GUI.

## Interpretação provável de cada ensaio

Sem metadados explícitos nos arquivos, a natureza de cada ensaio só pode ser inferida pelo conteúdo das colunas 0 (referência) e 4/5 (entrada malha aberta) e pelo agrupamento temporal:

- **Amostras lidas** (`arquivo_13_8_2023...`, `arquivo_24_6_2023_19_2_54...`, `arquivo_9_9_2023...`): coluna 0 (referência) constante em `0.0` ou `30.0` durante o trecho inicial, colunas 4/5 com valor fixo (1.0/1.3/1.5 V) — padrão de **ensaio em malha aberta com entrada constante ou PRBS** (offset de operação fixo, resposta livre do sistema), coerente com o firmware `Esp32_ttgo_modulos` que usa PRBS (`OndaPrbs`) para excitação em malha aberta — usado tipicamente para **identificação de sistema** (estimar parâmetros do modelo J, c, Km, etc.).
- **Datas agrupadas em blocos** (3 ensaios em 24-25/06, 2 ensaios em 9-14/09) sugerem sessões de coleta em dias distintos, possivelmente:
  - Blocos de 24-25/06/2023: repetição de ensaios de identificação/PRBS em malha aberta com pequenas variações de offset/configuração (tamanhos de arquivo similares, ~150-250 KB, ensaios longos, provavelmente para levantamento de dados para ajuste do modelo matemático/controlador).
  - Ensaio isolado de 13/08/2023 (bem menor, 24 KB): possivelmente um teste rápido/validação pontual, não um ensaio completo de identificação.
  - Blocos de 09/09 e 13-14/09/2023: novos ensaios, possivelmente com referência em degrau/onda quadrada (coluna 0 = 30.0 em vez de 0.0) sugerindo teste de **resposta ao degrau em malha fechada com PID** (validação do controlador após a etapa de identificação), já que o valor de referência aparece não-nulo desde o início.

**Nota**: essa interpretação é uma inferência razoável a partir do código e dos primeiros valores lidos (não foi feita leitura integral dos 9 arquivos); para confirmar o tipo exato de cada ensaio (degrau/PRBS/senoidal) seria necessário plotar a coluna 0 (referência) e 4 (entrada MA) ao longo de cada arquivo completo.

## Catálogo (2026-09-13)

Classificação feita a partir dos próprios dados e publicada em
`softwares_aeropendulo/src_interface/dados_de_ensaio/README.md`: 6 ensaios PRBS em malha aberta
(níveis 1,0↔1,3 V ou 1,0↔1,5 V) e 3 em malha fechada com onda quadrada — dois completos entre
0° e 10° (trocas a cada 2,5 s e 3,3 s), usados nas métricas de malha fechada, e um curto de 11 s.
O ensaio de identificação é `arquivo_9_9_2023_13_33_24.csv`. Não há ensaio dente de serra ou
senoidal gravado, e os parâmetros dos ensaios de malha fechada (0,2 e 0,15 Hz, 10°) diferem dos
citados no texto da monografia (0,5 Hz, 15°).

