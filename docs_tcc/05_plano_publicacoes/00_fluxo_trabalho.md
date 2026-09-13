---
fonte: síntese de todo docs_tcc/ + decisões tomadas nas sessões de 2026-09-12/13
gerado_em: 2026-09-13
---

# Fluxo de trabalho — do estado atual às publicações

Este é o documento para abrir **primeiro** ao retomar o trabalho. Ele sequencia as fases,
diz o que é pré-requisito de quê, e aponta para o plano detalhado de cada uma.

```text
Fase 1                Fase 2                     Fase 3 ─ Artigo   (sessão dedicada)
Fechar pendências  →  Finalizar documentação  ┤
da sessão atual        (monografia/software/site) └ Fase 4 ─ Livro    (sessão dedicada)
```

- **Fase 1 → Fase 2**: sequencial. Fase 2 assume que o repositório está num estado limpo.
- **Fase 2 → Fase 3**: sequencial. O artigo depende das métricas quantitativas da Fase 2.
- **Fase 2 → Fase 4**: o livro não depende de nada específico da Fase 2 além do que já está
  pronto hoje — **pode começar em paralelo**, inclusive antes da Fase 2 terminar.
- **Fases 3 e 4 entre si**: independentes. Trabalhar uma não bloqueia a outra.

## Fase 1 — Fechar pendências da sessão de rebranding

**Status em 2026-09-13: concluída, exceto a decisão de dependências (adiada de propósito).**

- [x] Branches `docs/metadados-ufpa` e `docs/roadmap-artigo-livro` consolidadas na branch de
      trabalho `fechamento-fase-1-2` (merge sem conflitos). Falta só o merge final na `main`.
- [x] Pasta `docs/Componentes do Pendulab/` renomeada para `docs/Componentes do Aeropêndulo/`.
- [x] `mkdocs build --strict` **passa sem avisos** — mkdocs foi instalado num venv
      (`/tmp/mkdocs_venv`, fora do repo) para validar. No caminho, achou e corrigiu 2 bugs
      reais que não estavam no radar: config obsoleta do mkdocstrings (`import:` →
      `inventories:`, faltava `paths: [.]`) e uma docstring com parâmetro inexistente. Ver
      "Achados extras" em [`pendencias_documentacao.md`](pendencias_documentacao.md).
- [ ] **Decisão sobre dependências: adiada.** O `poetry.lock` tem ~294 alertas do
      Dependabot, todos vindos de `aiohttp`/`tornado`/`jupyterlab`/etc. — dependências
      transitivas reais do `vpython` (usado no gêmeo digital), não resíduo. `poetry update`
      sozinho não resolve porque o piso `python >=3.8` força versões antigas dessas
      dependências; seria preciso subir o piso para `>=3.10` e então atualizar. Ambas as
      mudanças foram tentadas e revertidas nesta sessão por não terem como ser testadas sem
      o hardware (GUI e comunicação serial precisam ser verificadas no protótipo real antes
      do merge). Retomar como tarefa própria.

**Definição de pronto:** branch de trabalho mesclada na `main`, site publicando sem erro
(ambos confirmados nesta sessão) — falta só a decisão de dependências, adiada com
justificativa registrada.

## Fase 2 — Finalizar a documentação

**Status em 2026-09-13: quase concluída.** Lista completa e detalhada em
[`pendencias_documentacao.md`](pendencias_documentacao.md). Resumo por frente:

| Frente | Itens | Status |
| --- | --- | --- |
| Monografia (texto/fonte LaTeX) | 7 itens | 5 feitos e verificados (compilação real com pdflatex+bibtex); 2 em aberto (padronização de terminologia, sugestões do orientador) |
| Software | 7 itens | Todos os 7 feitos; PID e conversor corrigidos mas **não testados em hardware** |
| Site publicado | 2 itens | Ambos feitos e verificados (`mkdocs build --strict` limpo) |
| Organização do repo | 3 itens, opcionais | Nenhum feito — baixa prioridade, sem impacto em nada externo |

Achados que não estavam no radar original (ver punch list para detalhes): config quebrada
do mkdocstrings, um binário Linux solto dentro do firmware, e um script morto
(`main_aeropendulo.py`) cujos parâmetros físicos já estavam documentados em outro lugar.

**O item que realmente importa para a Fase 3:** calcular métricas quantitativas de erro
(RMSE / NRMSE) do modelo identificado e de desempenho em malha fechada (tempo de
acomodação, sobressinal, erro em regime). Hoje a validação é só visual. Os dados para isso
já existem — os 9 CSVs em `softwares_aeropendulo/src_interface/dados_de_ensaio/` — falta só
processar. Esse cálculo serve três propósitos ao mesmo tempo: fecha a limitação que o
próprio autor reconhece no Cap. 4 da monografia, é pré-requisito do artigo, e vira material
de exemplo no livro. **Candidato natural a próxima sessão de trabalho.**

**Definição de pronto:** todos os itens de `pendencias_documentacao.md` marcados como feitos
ou explicitamente adiados com justificativa; métricas quantitativas calculadas e
documentadas em algum lugar de `docs_tcc/`.

## Fase 3 — Artigo (sessão dedicada separada)

**Decisão de 2026-09-13:** existe um rascunho antigo do COBENGE 2023, em coautoria com outro
orientando (`softwares_aeropendulo/simulador_aeropendulo/docs/utils/Template_Artigos_ST_COBENGE-2023.docx.pdf`),
mas ele **não será usado como base** — o artigo é planejado do zero, focado só no trabalho
próprio. Ver [`plano_artigo.md`](plano_artigo.md).

Não abrir essa sessão antes das métricas quantitativas da Fase 2 estarem prontas — sem elas
não há o que revisor de artigo aceite como resultado.

## Fase 4 — Livro (sessão dedicada separada)

Plano detalhado em [`plano_livro.md`](plano_livro.md). Pode começar a qualquer momento,
independente das Fases 2 e 3 — a primeira decisão (público-alvo) é só de escopo, não de
material pronto.

## O que não fazer ainda

Para não perder o fio: nenhuma linha de artigo ou livro deve ser escrita antes de fechar a
pergunta de escopo respectiva (seção "Perguntas em aberto" de cada plano). O trabalho de
IA nas Fases 3 e 4, até lá, é só inventariar material e levantar opções — não redigir.
