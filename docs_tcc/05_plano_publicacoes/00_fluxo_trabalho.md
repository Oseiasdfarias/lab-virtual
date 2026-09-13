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

Curto prazo, mecânico, sem decisões de conteúdo pendentes.

- [ ] Merge da branch `docs/metadados-ufpa` (metadados oficiais da BDM/UFPA no README).
- [ ] Merge desta branch (`docs/roadmap-artigo-livro`).
- [ ] Renomear a pasta `docs/Componentes do Pendulab/` — a marca antiga ainda aparece na
      navegação do site publicado.
- [ ] Rodar `mkdocs build --strict` para confirmar que o site compila com as mudanças de
      marca e de nome do repositório. Não validado ainda por falta de `mkdocs` instalado na
      máquina onde o trabalho foi feito.
- [ ] Decidir o que fazer com as dependências do software (ver nota abaixo) e, se optar por
      atualizar, testar a interface gráfica e a comunicação serial antes de mesclar — isso
      não pode ser validado por um assistente sem acesso ao protótipo físico.

**Nota sobre dependências:** o `poetry.lock` tem ~294 alertas do Dependabot, todos vindos de
`aiohttp`/`tornado`/`jupyterlab`/etc. — dependências transitivas do `vpython` (usado no
gêmeo digital), não de código próprio do projeto. `poetry update` sozinho não resolve
porque o piso `python >=3.8` força versões antigas dessas dependências; seria preciso subir
o piso para `>=3.10` e então atualizar. Ambas as mudanças foram tentadas e revertidas nesta
sessão por não terem como ser testadas sem o hardware. Retomar como tarefa própria, testando
a GUI e a serial antes do merge.

**Definição de pronto:** as 3 branches abertas mescladas na `main`, site publicando sem
erro, decisão registrada sobre as dependências (mesmo que a decisão seja "manter como
está" — registrar o porquê).

## Fase 2 — Finalizar a documentação

Lista completa e detalhada em [`pendencias_documentacao.md`](pendencias_documentacao.md).
Resumo por frente:

| Frente | Itens | Bloqueia o quê |
| --- | --- | --- |
| Monografia (texto/fonte LaTeX) | 7 itens — equações incompletas no Cap. 3, siglas/símbolos genéricos, `.bib` com entradas erradas, etc. | Nada externo; é o registro histórico, corrige-se para futuras recompilações |
| Software | 7 itens — script quebrado, firmware que não compila, nome enganoso de uma variante, bugs suspeitos no PID | Credibilidade técnica do artigo e reprodutibilidade do livro |
| Site publicado | 2 itens — 4 páginas vazias, depende de docstrings completas | Nada externo, mas é a face pública do projeto |
| Organização do repo | 3 itens, opcionais/cosméticos | Nada |

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
