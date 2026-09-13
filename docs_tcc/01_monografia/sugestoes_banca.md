---
fonte: revisao_tcc/andre/Sugestões TCC - Oseias.docx; comparado com revisao_tcc/Template_TCC_FEE (arquivos incluídos por tcc_oseias_farias.tex) e com o texto de tcc_oseias_farias.pdf
gerado_em: 2026-09-13
---

# Sugestões da banca (Prof. André Cruz) × versão final

O documento de sugestões é do **Prof. André Cruz**, membro da banca — não do orientador
(Prof. Raphael Barros Teixeira), como a punch list registrava antes.

Cada ponto foi conferido nos arquivos que o `tcc_oseias_farias.tex` realmente inclui (a
introdução vem de `elementos_textuais/Cap_1_introducao.tex`; os capítulos 2 a 4, de
`Capitulos/`) e no texto extraído do PDF registrado. "Não verificável" indica pontos de
formatação visual que não dá para confirmar sem inspecionar página a página.

A monografia já está registrada na BDM/UFPA; os pontos em aberto servem de referência para
uma eventual nova versão ou para o artigo, e não pedem alteração do documento defendido.

## Resumo

| Situação | Pontos |
| --- | --- |
| Incorporado | 7 (+1 provável) |
| Parcial | 3 |
| Não incorporado | 8 |
| Pergunta não respondida no texto | 2 |
| Não verificável automaticamente | 4 |
| Não se aplica ao texto (elogio ou sugestão de hardware) | demais |

## Formatação

| Sugestão | Situação | Evidência |
| --- | --- | --- |
| Seguir o guia de trabalhos acadêmicos da UFPA | Não verificável | Usa o template abnTeX2 da FEE/CAMTUC |
| Corrigir recuos no início dos parágrafos | Não verificável | — |
| Letras minúsculas iniciando frases e pontuação indevida | Parcial | Ainda há casos, ex.: "em torno de θ. dessa forma, temos a seguinte linearização" (cap. 2) |
| Títulos de seção: fonte 12, caixa alta e negrito (capítulo), negrito (seção), normal (subseção) | Não verificável | Definido pelo template |
| Alíneas alfanuméricas em vez de marcadores | Não incorporado | 10 listas `itemize` em `3_3_interface_grafica.tex` (17 marcadores no PDF) |
| Tamanho da fonte nas legendas | Não verificável | — |
| Numeração contínua das equações, (1) em vez de (2.1) | Incorporado | PDF numera de (1) a (51) |
| "figura" minúsculo fora do início de frase | Incorporado | 19 usos de "figura \ref", nenhum "Figura \ref" no meio de frase |
| Quadros para organizar blocos de código | Não incorporado | 15 blocos `lstlisting`, nenhum ambiente de quadro |

## Comentários gerais e perguntas

| Ponto | Situação | Evidência |
| --- | --- | --- |
| Como foi identificado que o motor tem ligação série? | Não respondido no texto | O texto afirma que é série (`2_3_modelagem_analitica.tex`, `3_1_prototipagem.tex`) sem dizer como isso foi determinado |
| Critérios para dividir identificação e validação | Parcial | Informa 60%/40% (`Cap_3_Resultados_e_Discussoes.tex`, l. 47), sem justificar a escolha |
| Justificativa, introdução, modelagem, dificuldade com parâmetros, figuras | Não se aplica | Comentários positivos |

## Capítulo 1

| Sugestão | Situação | Evidência |
| --- | --- | --- |
| Sem vírgula antes das referências | Incorporado | Nenhuma ocorrência de `, \cite` na introdução compilada |
| Afirmações no passado, não no futuro | Parcial | "será criado" foi revisto; resta "será necessário combinar tecnologias" (`elementos_textuais/Cap_1_introducao.tex`, l. 30) |

## Capítulo 2

| Sugestão | Situação | Evidência |
| --- | --- | --- |
| Descrever parâmetros em parágrafo, não em marcadores | Incorporado | "Onde Fe é o empuxo gerado pela hélice, Jb é o momento de inércia do braço, …" |
| "como mostra [xx]??" na página 9 | Incorporado | Citação resolvida (MOHAMMADBAGHERI; YAGHOOBI, 2011); nenhum "??" no PDF |
| Definir $K_m$ | Incorporado | "Km é um ganho que relaciona a velocidade angular com o empuxo" |
| Notação de velocidade angular parecida com derivada de $\omega$ | Não incorporado | 17 ocorrências de `\dot{\omega}`/`\ddot{\omega}`; em $E_a = \dot\omega K_0 i$ o ponto é de fato um erro (pela eq. $E_a = \omega\Phi(i)$ deveria ser $\omega$) |
| Notação de aceleração angular parecida com segunda derivada de $\omega$ | Não incorporado | Mesmo caso: $K_0 i^2 = J_m\ddot\omega + b\dot\omega + T_c$ |
| Parágrafo discutindo os polos da função de transferência | Não incorporado | Nenhuma ocorrência de "polo" no texto |
| Projetar uma PCB para o circuito da figura 17 | Não se aplica | Sugestão de hardware |

## Capítulo 3

| Sugestão | Situação | Evidência |
| --- | --- | --- |
| Explicar as siglas PRBS e PWM | Não incorporado | Aparecem sem expansão (`Cap_3_Resultados_e_Discussoes.tex`, l. 19 e 34); a lista de siglas está comentada no arquivo mestre |
| Motivo das potências negativas na equação de 2ª ordem | Não respondido | A equação continua em $z^{-1}$, $z^{-2}$ sem justificativa |
| Equação 3.2 com "dt = 0,019" | Não incorporado | `dt = 0,019` (l. 167) contra `dt = 0,02` nas demais (l. 249 e 296); no notebook, esse valor vem de `Ts = np.mean(np.diff(tempo))` |
| Gráfico do erro nas comparações das figuras 27 e 28 | Não incorporado | Sem gráfico nem métrica de erro; o site agora publica NRMSE/RMSE como análise posterior (ver `docs/identificacao/validacao.md`) |

## Capítulo 4, referências e apresentação

| Sugestão | Situação | Evidência |
| --- | --- | --- |
| Referências antes do apêndice | Incorporado | `\bibliography` (l. 131) vem antes de `\include{elementos_postextuais/apendices}` (l. 137) |
| Ampliar a figura 21 (partes da interface) | Incorporado provável | Hoje com `width=0.95\textwidth`; não comparado com a versão revisada pela banca |
| Considerações finais, dicção, domínio do tema, uso do vídeo | Não se aplica | Comentários positivos sobre o texto e a defesa |

## Achado relacionado, fora da lista da banca

Ao reproduzir a identificação para responder ao pedido de gráfico de erro, apareceu uma
diferença entre o modelo estimado e o publicado: a função de 10ª ordem foi montada com
`ct.tf([b0..b3], [1, -a1..-a10])`, que o python-control lê em potências positivas de $z$ —
isso acrescenta 7 amostras de atraso. Simulado corretamente, o ARX estimado tem NRMSE de
78,30% no trecho de validação, contra 55,97% do modelo publicado. Detalhes e script em
`docs/identificacao/validacao.md` e
`materiais_complementares/Identificacao_de_Sistemas/identificacao_aeropendulo/ident_up/metricas_validacao.py`.
