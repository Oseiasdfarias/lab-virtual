---
fonte: diff entre revisao_tcc/TCC-Oseas/Capitulos/ e revisao_tcc/Template_TCC_FEE/Capitulos/, revisao_tcc/andre/
gerado_em: 2026-09-12
---

## O que já foi corrigido na versão final (evidência: diffs entre rascunho e versão final)

Comparação feita com `diff -bB` (ignora espaços/linhas em branco) entre os 15 arquivos `.tex` presentes em ambos `TCC-Oseas/Capitulos/` (rascunho) e `Template_TCC_FEE/Capitulos/` (versão final). Dois arquivos são idênticos (`2_1_descricao.tex`, `2_4_modelagem_identificacao_sistemas.tex`, `3_0_0_dev_software.tex` — sem mudança de conteúdo).

- **Padrão geral em quase todos os capítulos**: troca sistemática de "Figura" → "figura" (minúsculo) no meio de frases — corresponde diretamente a uma sugestão do orientador ("Trocar 'Figura' para 'figura' quando não estiver iniciando uma frase"). Também pequenas correções de maiúscula/minúscula no início de frases (ex.: "assim" → "Assim", "reescrevendo" → "Reescrevendo").

- **2_2_fundamentacao_teorica.tex**: apenas correções pontuais de capitalização ("dessa forma" → "Dessa forma", "O modelo..." minúsculo → maiúsculo).

- **2_3_modelagem_analitica.tex** (mudanças mais relevantes de conteúdo):
  - Listas com `\itemize` explicando variáveis de equações (Fe, Jb, θ, c, m, d, etc.) foram convertidas em texto corrido ("Onde $F_e$ é o empuxo gerado pela hélice, ...") — atende exatamente à sugestão do orientador de não usar marcadores para descrever parâmetros de equação.
  - Notação `$\dot{\omega}$` (velocidade angular) trocada por `$\omega$` simples, e `$\ddot{\omega}$` (aceleração) por `$\dot{\omega}$` — corrige a confusão apontada pelo orientador ("notação de velocidade angular ficou semelhante à notação de derivada temporal").
  - Removida a referência quebrada `$[xx]$` e adicionado texto explicando o ganho $K_m$ ("em que $K_m$ é um ganho que relaciona a velocidade angular com o empuxo") — responde a duas observações do orientador (referência `[xx]` não identificada e $K_m$ não definido).
  - Figura `ft_subsistemas.pdf` → `.png`.
  - Trecho comentado (`%`) sobre "Identificação de Sistemas" adicionado ao final (parece placeholder/rascunho de seção futura, ainda comentado).

- **3_0_simulador_e_prototipo_do_Aeropendulo.tex, 3_4_firmware.tex, 3_5_ecossistema.tex**: só a correção "Figura"→"figura"; em `3_5_ecossistema.tex` há também troca da última palavra "ecossistema" → "laboratório" no trecho final (possível padronização terminológica — ver seção de atenção abaixo).

- **3_1_prototipagem.tex**:
  - Diversas correções "Figura"→"figura".
  - Ajustes de largura de imagens (`width=0.5`, `0.45`, etc.).
  - A figura de "Componentes eletrônicos" (resistores/capacitores) foi reestruturada: no rascunho eram duas `subfigure` dentro de uma única `figure` com legenda comum; na versão final viraram duas figuras `\begin{figure}` separadas, cada uma com sua própria legenda.
  - Figura do esquema elétrico trocada de `.pdf` para `.png`.

- **3_2_1_python.tex**: sem mudança de conteúdo, apenas remoção de quebras de parágrafo (texto sobre Python/C/C++ virou um único parágrafo).

- **3_2_simulador_usando_python.tex**:
  - "Figura"→"figura".
  - Blocos de código migrados do ambiente customizado `\begin{python}...\end{python}` para `\begin{lstlisting}[language=python,...]` com legendas e numeração de linhas (padrão mais formal de listagem).
  - Comentários de código traduzidos sem acentuação ("ângulo"→"angulo", "gráficos"→"graficos") — possivelmente para evitar problemas de encoding no `lstlisting`.

- **3_3_interface_grafica.tex**: mesma migração de `python`→`lstlisting` com legendas/labels, e "Figura"→"figura".

- **Cap_2_Desenvolvimento.tex**: a seção `\section{Implementação do Protótipo}` (label `implementacao_prototipo`) foi **comentada/removida** na versão final; um novo label `imple_aeropendulo` foi adicionado em outro ponto. Sugere reorganização estrutural do capítulo — vale conferir se o conteúdo dessa seção foi realocado ou perdido.

- **Cap_3_Resultados_e_Discussoes.tex** (capítulo com mais mudanças de conteúdo):
  - "Figura"→"figura" e correção de referências de imagem erradas (`\ref{fig3:image_13}` duplicado no rascunho → corrigido para `fig3:image_13_1}, \ref{fig3:image_14}` na versão final).
  - "usá-lo para... o ecossistema desenvolvido" → "a partir da estrutura desenvolvida" (troca terminológica "ecossistema"→"estrutura").
  - Todos os blocos `\begin{python}` migrados para `\begin{lstlisting}[...]` com legendas descritivas específicas para cada trecho de código (ex.: "Importação das Bibliotecas...", "Método dos mínimos quadrados.", etc.) — bem mais completo que o rascunho.
  - Equação `eq3:eq2`: no rascunho o período de amostragem aparecia dentro da equação (`\quad dt = 0.019`); na versão final foi movido para o texto ("o período de amostragem é $dt = 0,019$ segundos") — atende à observação do orientador ("Problema na equação 3.2: Hz, dt=0,019?").
  - Adicionado texto explicando numerador/denominador da função de transferência de 10ª ordem (`eq3:eq3`) e da função identificada final (`eq3:eq4`).
  - **Atenção**: nas equações `eq3:eq3` e `eq3:eq4` da versão final, os coeficientes numéricos reais foram substituídos pelo texto literal `\frac{numerador}{denominador}` — no rascunho os valores numéricos completos estavam presentes. Isso parece uma edição incompleta/placeholder esquecido (ver seção de atenção).
  - "Com proposito de testar..." — "Figura"→"figura".
  - "determinaram-se os valores ótimos" → "determinou-se valores" (mudança de tom, removendo "ótimos", talvez por rigor metodológico já que a sintonia foi por tentativa e erro).

- **Cap_4_ Conclusao.tex**:
  - "O ecossistema concebido para este projeto foi..." → "Os subsistemas concebido para este projeto foi..." (troca de termo "ecossistema"→"subsistemas", mas **atenção**: ficou concordância verbal incorreta, ver abaixo).
  - "expansão do ecossistema" → "expansão do laboratório virtual".

## Sugestões do orientador (revisao_tcc/andre/)

O arquivo `Sugestões TCC - Oseias.docx` foi lido com sucesso via `pandoc` (conversão para texto simples). Resumo dos pontos (Prof. André Cruz):

**Formatação geral:**
- Seguir o guia de trabalhos acadêmicos da UFPA; corrigir recuos de parágrafo.
- Frases iniciando com letra minúscula / pontuação indevida.
- Títulos: capítulos em fonte 12, caixa alta e negrito; seções em negrito; subseções em letra normal.
- Usar alíneas alfanuméricas em vez de marcadores (bullets).
- Ajustar tamanho de fonte nas legendas das figuras.
- Numeração de equações deve ser contínua (não por capítulo) — ex.: trocar "(2.1)" por "(1)".
- "Figura"→"figura" fora de início de frase (já corrigido, ver acima).
- Usar ambiente de "quadro" para blocos de código.

**Comentários gerais:**
- Boa justificativa e introdução; modelagem do aeropêndulo/motor parece correta.
- Perguntou como foi identificado que o motor é de ligação série, e quais critérios foram usados para dividir dados de identificação/validação.

**Cap. 1 (Introdução):**
- Não usar vírgula antes de referências.
- Usar tempo passado em vez de futuro (ex.: "será criado" → "foi desenvolvido").

**Cap. 2:**
- Não descrever parâmetros de equação em marcadores, usar texto corrido (já corrigido, ver acima).
- Página 9: referência "[xx]" sem sentido (já corrigido).
- $K_m$ não definido (já corrigido).
- Notação de velocidade/aceleração angular confusa com notação de derivada (já corrigido — trocado $\dot\omega$/$\ddot\omega$ por $\omega$/$\dot\omega$).
- Sentiu falta de parágrafo discutindo os polos da função de transferência (não identificado se foi endereçado — não há trecho novo sobre polos nos diffs revisados).
- Sugeriu projetar uma PCB para o circuito (figura 17) em vez de protoboard — não há evidência nos diffs de que isso foi feito (mudança de hardware não aparece em texto).

**Cap. 3:**
- Explicar siglas PRBS e PWM na primeira ocorrência — não confirmado se foi adicionado (não capturado nos diffs, pode já estar em outro trecho não alterado).
- Questionou uso de potências negativas na equação 3.1 — não haveria evidência de resposta nos diffs analisados.
- Apontou problema no "Hz, dt=0,019" da equação 3.2 (já corrigido, dt movido para o texto).
- Sugeriu gerar gráfico de erro comparando figuras 27/28 — não identificado nos diffs se foi implementado.

**Cap. 4:** considerado bem escrito, sem pontos de correção.

**Geral:** referências deveriam vir antes do apêndice.

**Apresentação (defesa):** pontos positivos (boa dicção, domínio do tema, bom uso de recursos gráficos); sugeriu focar mais em ferramentas numéricas que na modelagem analítica durante a fala, e ampliar a figura 21 (partes da interface gráfica).

## Pontos de atenção para retomar o trabalho

*Inferências baseadas nos diffs e no texto de sugestões — não são fatos confirmados, precisam de checagem manual:*

- **Possível erro introduzido no Cap. 3**: as equações `eq3:eq3` e `eq3:eq4` (funções de transferência discretas de 10ª ordem) na versão final (`Template_TCC_FEE`) mostram o texto literal `\frac{numerador}{denominador}` em vez dos coeficientes numéricos reais que estavam presentes no rascunho (`TCC-Oseas`). Isso parece uma edição incompleta — vale comparar com o PDF final (`TCC-Oseias-Final.pdf` ou o PDF do André) para confirmar se os valores numéricos aparecem corretamente no documento compilado, ou se isso é de fato um bug pendente de correção.

- **Possível erro de concordância verbal no Cap. 4**: "Os subsistemas concebido para este projeto foi meticulosamente desenvolvido e testado..." — sujeito no plural ("Os subsistemas") com verbos no singular ("concebido", "foi", "desenvolvido"). Parece ter sido introduzido durante a troca do termo "ecossistema" (singular) por "subsistemas" (plural) sem ajustar a concordância. Merece revisão de português.

- **Seção "Implementação do Protótipo" comentada no Cap. 2**: não está claro se o conteúdo foi movido para outro lugar (label novo `imple_aeropendulo` foi criado) ou se ficou perdido/incompleto. Vale conferir no PDF final se essa seção aparece com outro título/estrutura.

- **Sugestões do orientador possivelmente ainda pendentes** (não encontradas evidências de correção nos diffs dos 15 arquivos comparados — podem ter sido feitas em outras partes do documento não cobertas por este diff, como PreTextual/elementos_pretextuais, ou simplesmente ainda não feitas):
  - Numeração contínua das equações (não por capítulo).
  - Formatação de títulos (caixa alta/negrito por nível).
  - Uso de alíneas alfanuméricas em vez de bullets (ainda há `\itemize` em outros pontos do texto que não foram revisados neste diff).
  - Ajuste de tempo verbal no Cap. 1 (futuro→passado).
  - Discussão sobre os polos da função de transferência (Cap. 2).
  - Sugestão de projetar PCB (não avaliável só por diff de texto).
  - Explicação das siglas PRBS/PWM.
  - Gráfico de erro comparando as figuras 27/28 no Cap. 3.
  - Reordenar referências antes do apêndice.

- **Terminologia inconsistente "ecossistema" vs "estrutura"/"subsistemas"/"laboratório virtual"**: o termo "ecossistema" foi trocado por diferentes palavras em pontos diferentes do texto (Cap_3: "ecossistema"→"estrutura"; Cap_4: "ecossistema"→"subsistemas" em uma frase e "ecossistema"→"laboratório virtual" em outra; `3_5_ecossistema.tex` também trocou "ecossistema"→"laboratório" no corpo do texto, mas o nome do arquivo continua `3_5_ecossistema.tex`). Vale decidir um termo único e padronizar em todo o documento — atualmente parece indefinido se o projeto é chamado de "ecossistema", "estrutura", "laboratório virtual" ou "subsistemas".

- **Arquivos não comparados neste diff**: PreTextual/Resumo, Abstract, listas de siglas/símbolos, apêndices e elementos pós-textuais não foram comparados (estruturas de diretório diferentes entre `TCC-Oseas/PreTextual/` e `Template_TCC_FEE/elementos_pretextuais/` — nomes e organização divergem, não é diff direto arquivo-a-arquivo). Se sobrar tempo, vale conferir se essas seções também precisam de revisão à luz das sugestões do orientador (ex.: recuos de parágrafo, formatação de títulos).

- **PDFs não lidos neste levantamento**: `TCC_Oseias_final v-André.pdf` (possivelmente com anotações/comentários manuscritos do orientador) e `TCC-Oseias-Final.pdf` não foram abertos/analisados — o `.docx` de sugestões parece ser a transcrição dessas anotações, mas vale abrir o PDF do André manualmente para checar se há marcações adicionais (grifos, comentários inline) não capturadas no `.docx`.
