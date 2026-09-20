---
fonte: síntese de docs_tcc/01_monografia/pendencias.md, docs_tcc/02_software/*, docs_tcc/03_docs_publicadas/resumo_mkdocs.md
gerado_em: 2026-09-12
atualizado_em: 2026-09-13
---

# Punch list — o que falta para "finalizar a documentação"

Lista consolidada dos gaps encontrados no levantamento. Itens concluídos em 2026-09-13
(Fase 1 e 2 do [`00_fluxo_trabalho.md`](00_fluxo_trabalho.md)) ficam marcados com a data e
uma nota de como foram verificados — nada foi marcado como feito sem checagem (build
`--strict`, compilação real da monografia, ou leitura de código-fonte).

## Monografia (texto)

- [x] **2026-09-13** — Resolvidas as 2 equações do Cap. 3 (`eq3:eq3`, `eq3:eq4`): os
      coeficientes já estavam escritos por extenso no texto corrido ao lado de cada
      equação — foi transcrição, não derivação nova. Verificado compilando a monografia
      inteira com `pdflatex` + `bibtex` (3 passagens, sem erros nem referências pendentes) e
      conferindo visualmente as páginas 55–56 do PDF gerado.
- [x] **2026-09-13** — Corrigida a concordância verbal no Cap. 4 ("Os subsistemas
      concebido...foi..." → "concebidos...foram...").
- [ ] **Terminologia — diagnóstico refeito em 2026-09-13.** A contagem nos arquivos
      compilados mostra que "ecossistema" não aparece no texto (só no nome do arquivo
      `3_5_ecossistema.tex` e da figura) e que "estrutura" quase sempre se refere à
      estrutura física. A inconsistência real é **"simulador" (36×) vs "gêmeo digital"
      (30×)** para o mesmo software. Sugestão para o artigo e o livro: "gêmeo digital" para
      o conceito e `Simulador` só para a classe Python. Não alterado na monografia
      registrada.
- [x] **2026-09-13 (investigado, não alterado)** — As listas de siglas/símbolos
      (`elementos_pretextuais/siglas.tex`, `simbolos.tex`) têm conteúdo genérico de template,
      mas **estão comentadas no arquivo mestre** (`%\input{...}`) — nunca aparecem no PDF
      compilado. Ativar e popular essas listas é uma decisão editorial (adicionar uma seção
      pré-textual nova), não um bug — deixado para o usuário decidir.
- [x] **2026-09-13** — Corrigido o `.bib` real (`bibtex-referencias.bib`): removida a
      entrada `vpython11` (duplicata não citada em lugar nenhum), removida a entrada
      `exemplo` (resíduo de template sobre física de partículas, também não citada), e
      corrigida a URL de `vpython` (apontava para o site do CustomTkinter). Verificado que
      nenhuma citação ficou órfã: `bibtex` rodou sem nenhum aviso de entrada faltante.
- [x] **2026-09-13** — Os dois arquivos abandonados (`2_1_descricao.tex`,
      `2_4_modelagem_identificacao_sistemas.tex`) ganharam um comentário no topo explicando
      que estão excluídos da compilação (`\input` comentado em `Cap_2_Desenvolvimento.tex`)
      e para onde o conteúdo real migrou. Não apagados — mantidos como histórico.
- [x] **2026-09-13** — Métricas de erro calculadas como análise posterior (não entram na
      monografia registrada): o script
      `materiais_complementares/.../ident_up/metricas_validacao.py` refaz a identificação a
      partir do CSV original, com coeficientes idênticos aos do notebook, e mede NRMSE/RMSE
      no trecho de validação — 2ª ordem 51,35%/1,62°, 10ª ordem publicada 55,97%/1,47°,
      10ª ordem ARX simulada corretamente 78,30%/0,72°. Publicado em
      `docs/identificacao/validacao.md`.
- [ ] **Achado para o artigo:** a função de 10ª ordem da monografia foi montada com
      `ct.tf([b0..b3], [1, -a1..-a10])`, que o python-control lê em potências positivas de
      $z$ — 7 amostras de atraso que não existem no ARX estimado. É o que separa 55,97% de
      78,30% de ajuste. A figura de validação de 10ª ordem e a equação numérica do Cap. 3
      refletem o modelo com atraso.
- [x] **2026-09-13** — Sugestões da banca conferidas ponto a ponto contra os arquivos
      compilados e o PDF: ver [`../01_monografia/sugestoes_banca.md`](../01_monografia/sugestoes_banca.md).
      O documento é do **Prof. André Cruz** (banca), não do orientador. Resultado: 7
      incorporadas (+1 provável), 3 parciais, 8 não incorporadas, 2 perguntas não
      respondidas no texto, 4 não verificáveis automaticamente.

## Software

- [x] **2026-09-13** — `main_aeropendulo.py` removido (importava classes que não existem
      mais). Os parâmetros físicos que ele carregava (`K_m=0.0296`, `J=0.0106`, `c=0.0076`,
      `m=0.36`, `d=0.03`) já estão documentados, com a derivação completa e a função de
      transferência analítica, em
      `simulador_aeropendulo/docs/Modelagem_matematica_do_aeropendulo.ipynb` — nada foi
      perdido.
- [x] **2026-09-13** — Corrigido o erro de sintaxe em
      `PlatformIo/Arduino_Nano/src/main.cpp` (caractere `k` solto fora de qualquer função,
      no fim do arquivo). *Não foi possível compilar com o PlatformIO real para confirmar
      (toolchain não disponível) — fix é textualmente inequívoco, mas fica sem validação por
      build.*
- [x] **2026-09-13** — `Esp32_ttgo_modulos_freertos` ganhou um `README.md` explicando que
      não usa FreeRTOS de verdade e apontando para `Esp32_ttgo_modulos` como a variante mais
      completa. Não renomeado (para não quebrar caminhos já referenciados).
- [x] **2026-09-13** — Removidos os arquivos vazios
      `PlatformIo/Esp32_ttgo/lib/ler_escrever_serial/src/ler_escrever_serial.{cpp,h}` (e o
      `library.json` da mesma pasta) — confirmado que nada em `Esp32_ttgo/src/main.cpp`
      referenciava essa lib.
- [x] **2026-09-13** — Os dois bugs suspeitos eram reais, corrigidos:
      - `controlador_pid.cpp`: o termo derivativo multiplicava por `erro` (não deveria) e
        por `Ts` em vez de dividir por `Ts` (a discretização de uma derivada divide pelo
        passo de amostragem). Corrigido para `D = Kd * (lastTheta - theta) / Ts`.
      - `conversor.cpp`: `0.0 <= sinal_controle <= 3.3` não faz o que parece em C++ — é
        avaliado como `(0.0 <= sinal_controle) <= 3.3`, um booleano comparado a 3.3, sempre
        verdadeiro. O clamp em 255 nunca era alcançado e valores negativos não eram limitados.
        Corrigido com `if/else if/else` explícito.
      - **Nenhum dos dois foi validado em hardware.** Correção de 2026-09-13: este item
        dizia antes que os ganhos do PID são "configurados em tempo de execução pela
        interface gráfica" — **isso estava errado**. Verificado lendo `ler_dados_serial()`
        em `ler_escrever_serial.cpp`: os únicos parâmetros que a interface envia ao
        firmware são amplitude, frequência, offset, forma de onda, malha aberta/fechada e
        o comando de executar — nenhum ganho de PID. Os ganhos são fixos em `main.cpp`
        (`PID mypid(0.02, 0.055, 0.35);`), definidos em tempo de compilação. Isso significa
        que esses 3 valores foram calibrados empiricamente contra a fórmula **antiga e
        errada** do termo derivativo — o comportamento em malha fechada deve ser
        reavaliado/reajustado (e os ganhos possivelmente recalibrados) no protótipo real
        antes de considerar isso definitivamente resolvido.
- [x] **2026-09-13** — `requirements.txt` regenerado com `poetry export` a partir do
      `poetry.lock` atual (148 pacotes). Ainda inclui a árvore do Jupyter — **isso é
      esperado, não é bug**: `vpython` depende de `ipykernel`/`jupyter`/`jupyter-server-proxy`
      de verdade (confirmado lendo o `poetry.lock`). O arquivo agora reflete com precisão o
      que `poetry install` instalaria, o que antes não era o caso.
- [x] **2026-09-13** — Mapeamento das 7 colunas dos CSVs de ensaio confirmado lendo
      `enviar_dados_serial()` no firmware (não é mais inferência) e documentado em dois
      lugares: [`../02_software/dados_ensaios.md`](../02_software/dados_ensaios.md) e um novo
      `src_interface/dados_de_ensaio/README.md` no próprio projeto.

## Site publicado (MkDocs / GitHub Pages)

- [x] **2026-09-13** — As 4 páginas "EM DESENVOLVIMENTO" foram preenchidas com conteúdo
      adaptado do Capítulo 3 da monografia (prototipagem, gêmeo digital, interface gráfica,
      firmware) — mesmo autor, mesmas palavras, só reformatadas para Markdown. Verificado com
      `mkdocs build --strict` (zero avisos) e conferência visual de uma das páginas
      renderizada no navegador.
- [x] **2026-09-13** — Docstrings conferidas: estão completas onde importa. A build
      `--strict` só falhou por um problema real e diferente (ver "Achados extras" abaixo);
      depois de corrigido, a página de referência de `interface_interativa.py` renderiza
      classe, atributos e métodos corretamente.

## Achados extras (não estavam na lista original)

- [x] **2026-09-13** — `mkdocs.yml` estava com uma configuração **quebrada** do
      mkdocstrings: a chave `import:` foi renomeada para `inventories:` numa versão mais
      recente da lib, e faltava `paths: [.]` para localizar os módulos de
      `softwares_aeropendulo`. Com isso, `mkdocs build --strict` nunca tinha rodado com
      sucesso até esta sessão (não havia `mkdocs` instalado antes). Corrigido.
- [x] **2026-09-13** — `animacao_aeropendulo.py`: docstring de `__aminacao()` documentava um
      parâmetro `comprimento_braco` que não existe na assinatura do método (copiado de
      `__init__` por engano). Corrigido — era o único erro real que a build `--strict`
      apontou depois do fix do `mkdocs.yml`.
- [x] **2026-09-13** — `Esp32_ttgo_modulos_freertos/` tinha um binário Linux x86-64
      compilado (`teste`) e um `.c` de teste de ponteiros (`teste.c`) sem nenhuma relação com
      o projeto, soltos na raiz do diretório do firmware. Removidos.
- [x] **2026-09-13** — Pasta `docs/Componentes do Pendulab/` renomeada para
      `docs/Componentes do Aeropêndulo/` (marca antiga na navegação do site); removido
      `docs/favicon_aeropendulo_png.png`, órfão desde a troca de identidade visual.

## Organização do repositório (limpeza, opcional)

- [ ] Decidir o destino de `revisao_tcc/TCC-Oseas/` (18 MB) e `revisao_tcc/andre/` (19 MB) —
      manter como histórico ou arquivar fora do repo principal. *(Decisão do autor.)*
- [x] **2026-09-13** — Duplicação resolvida: 119 arquivos duplicados removidos (≈ 60 MB), sempre
      mantendo ao menos uma cópia de cada conteúdo — verificado arquivo a arquivo, e a
      monografia compilada depois das remoções (65 páginas, sem citação indefinida nem
      arquivo ausente). Saíram as figuras repetidas em `revisao_tcc/TCC-Oseas/` e em
      `Template_TCC_FEE/elementos_textuais/` (ficaram os `.tex`), o `revisao_tcc/TCC-Oseas.zip`
      (todo o conteúdo existe em arquivos do repositório), as cópias soltas em `utils/`, dois
      notebooks "copy", um `.dxf~` de backup e outras cópias pontuais. Mantidas de propósito:
      as figuras em `Template_TCC_FEE/Capitulos/` (a compilação precisa delas) e seus
      originais em `materiais_complementares/`, os arquivos-padrão de cada projeto
      PlatformIO/Arduino, os `__init__.py` vazios e as cópias da marca que o MkDocs exige
      dentro de `docs/` e `overrides/`.
- [x] **2026-09-13** — Os dois nomes com codificação corrompida em
      `Identificacao_de_Sistemas/Programa Python/` foram renomeados para
      `identificacao.py` e `analise_grafica.py` (nenhum arquivo os referenciava).
- [x] **2026-09-13** — Removido `utils/Oseias_Fariascertificado_horas_complementares.pdf`
      (certificado pessoal). Continua no histórico do git; tirá-lo de lá exige reescrever o
      histórico com force push.

## Rodada de 2026-09-13 (tarde) — site, software e infraestrutura

- [x] Site: botões anterior/próximo em todas as páginas, footer completo e sensível ao tema,
      páginas antigas sem `<style>`/ícone solto, figuras de `utils/` trazidas para `docs/`
      (foto do protótipo de 12,9 MB para 189 KB).
- [x] Site e README: corrigidas afirmações sem base no código ou na monografia — gêmeo digital
      "autônomo"/"simulando a dinâmica identificada", ganhos do PID enviados pela serial,
      controlador projetado a partir do modelo, conversão de Tustin.
- [x] Site: legenda da Figura 1 do firmware, instruções de gravação, pasta de execução do
      `rungui.py`, caminho do `requirements.txt`, formato real dos CSVs (têm cabeçalho e
      índice), notação ARX, unidade de $K_m$, seção do motor CC série, nota sobre as duas
      formulações de $K_m$ (notebook × monografia).
- [x] Referência de código com as 7 classes usadas pelo `rungui.py`; removido
      `interface_interativa.py` (código morto).
- [x] Deploy do site automatizado (`.github/workflows/docs.yml`), com build estrito em PRs e
      versões fixadas em `requirements-docs.txt`.
- [x] Dependências: piso em Python 3.10; os 151 alertas do Dependabot aplicáveis ao lock caem
      para 1. Validado em Python 3.11 (instalação, imports do `rungui.py`, script de métricas).
- [→] **Alerta do `setuptools`** e **validação em hardware** (firmware, dependências novas):
      movidos para [`../divida_tecnica.md`](../divida_tecnica.md).
- [x] **2026-09-13** — Branches já mescladas apagadas no remoto e localmente; restam `main`,
      `gh-pages`, `dev`, `backup-lab-virtual` e `tcc-estado-original`.

## Rodada de 2026-09-13 (noite) — melhorias sem dependência de hardware

- [x] `LICENSE` (MIT para código e firmware; documentação própria sob CC BY 4.0, monografia e
      material de terceiros com os termos originais), `CITATION.cff` validado e `CHANGELOG.md`.
- [x] Versões unificadas em 1.0.0 e descrição do pacote corrigida.
- [x] Página do protótipo com lista de materiais, diagrama de comunicação, esquema elétrico e
      pinagem; divergência de pino do sensor sinalizada.
- [x] Catálogo dos 9 ensaios e métricas de malha fechada com script
      (`materiais_complementares/analise_malha_fechada/`).
- [x] Descrição da coluna de entrada corrigida: em malha fechada ela mantém o último valor da
      malha aberta, não zero.
- [x] Docstrings (13 → 57 de 62), correção do buffer de gravação e da checagem de eventos USB,
      suíte de testes (24) no CI.
- [x] Instalação unificada com Poetry como caminho principal.
- [x] Resumos de `docs_tcc/` atualizados para o estado atual; dívida técnica criada.
- [ ] Revisar os tutoriais de instalação do Python por sistema operacional (ainda ensinam o
      3.10.0, que continua suportado). Baixa prioridade.

## Ações que dependem do autor

- [ ] **Release v1.0.0 com DOI:** ativar a integração do repositório no Zenodo
      (zenodo.org → GitHub) **antes** de criar a release; depois, publicar a release `v1.0.0`
      e acrescentar o DOI ao `README.md` e ao `CITATION.cff`.
- [ ] **Atraso na função de transferência publicada:** decidir entre nota no artigo, errata
      na monografia ou ambos.
- [ ] Destino de `revisao_tcc/TCC-Oseas/` e `revisao_tcc/andre/`.
