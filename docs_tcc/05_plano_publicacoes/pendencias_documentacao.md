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
- [ ] Padronizar terminologia: "ecossistema" vs "estrutura", "subsistemas" vs "laboratório virtual" usados sem consistência entre capítulos. *(Não mexido — decisão editorial de estilo, não um erro objetivo.)*
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
- [ ] Decidir se vale acrescentar métricas quantitativas de erro (RMSE/EQM) na seção de Resultados — segue em aberto, é o item mais valioso para o artigo (ver [`00_fluxo_trabalho.md`](00_fluxo_trabalho.md), Fase 2 → Fase 3).
- [ ] Checar sugestões do orientador ainda não incorporadas — comparar `revisao_tcc/andre/Sugestões TCC - Oseias.docx` ponto a ponto com a versão final. Não feito nesta rodada.

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
      - **Nenhum dos dois foi validado em hardware** — são ganhos configurados em tempo de
        execução pela interface gráfica (não há valor pré-calibrado embutido que o fix
        invalidaria), mas o comportamento em malha fechada deve ser reavaliado/reajustado no
        protótipo real antes de considerar isso definitivamente resolvido.
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

- [ ] Decidir o destino de `revisao_tcc/TCC-Oseas/` e `revisao_tcc/andre/` (cópias de revisão desatualizadas) — manter como histórico ou arquivar fora do repo principal.
- [ ] `materiais_complementares/Identificacao_de_Sistemas/` tem forte duplicação de notebooks entre a raiz, `identificacao_aeropendulo/` e `identificacao_aeropendulo/ident_up/` (esta última é a mais avançada) — vale consolidar.
- [ ] Vários nomes de arquivo com encoding corrompido (ex.: `Identifica├з├гo.py`) dentro de `materiais_complementares/` — renomear para evitar problemas de portabilidade.
