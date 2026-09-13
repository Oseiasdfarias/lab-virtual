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
| 4 | Sinal de entrada em malha aberta (PRBS); `0` em malha fechada | Volts |
| 5 | Repetição da coluna 4 (reservado para uso futuro, não usado hoje) | Volts |
| 6 | Tempo decorrido do ensaio (passo ≈ 0,02 s) | segundos |

Nome do arquivo: `arquivo_<dia>_<mes>_<ano>_<hora>_<min>_<seg>.csv`, gerado por
`datetime.now()` no momento em que a gravação é desligada na interface gráfica.
