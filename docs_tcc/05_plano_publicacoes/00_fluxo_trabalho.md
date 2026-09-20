---
fonte: síntese de todo docs_tcc/ + decisões tomadas nas sessões de 2026-09-12/13
gerado_em: 2026-09-13
atualizado_em: 2026-09-13 (fim do dia)
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

**Status: concluída.** Branches consolidadas e mescladas na `main`, site publicando sem erro.
A decisão de dependências, antes adiada, foi tomada: piso em Python 3.10, alertas do Dependabot
de 151 para 3 (todos do `setuptools`, preso ao `vpython`), validado com instalação limpa,
testes e import dos módulos. A validação no protótipo ficou registrada em
[`../divida_tecnica.md`](../divida_tecnica.md).

## Fase 2 — Finalizar a documentação

**Status: concluída**, exceto o que depende do protótipo real, que está em
[`../divida_tecnica.md`](../divida_tecnica.md). Detalhes em
[`pendencias_documentacao.md`](pendencias_documentacao.md).

| Frente | Situação |
| --- | --- |
| Site | Mapa completo do laboratório, página Início interativa, protótipo com lista de materiais, esquema e pinagem, deploy automático |
| Métricas | Identificação (NRMSE/RMSE) e malha fechada (sobressinal, subida, acomodação, erro em regime), com scripts e testes de reprodutibilidade |
| Software | Docstrings, correções na gravação de ensaios, testes no CI, dependências atualizadas, versão 1.0.0 |
| Dados | Catálogo dos 9 ensaios |
| Repositório | `LICENSE` (MIT), `CITATION.cff`, `CHANGELOG.md`, duplicatas removidas |
| Monografia | Sugestões da banca conferidas ponto a ponto (`../01_monografia/sugestoes_banca.md`); não alterada por estar registrada |

**Achados que alimentam a Fase 3:** a função de transferência de 10ª ordem publicada tem 7
amostras de atraso a mais que o modelo estimado (55,97 % × 78,30 % de NRMSE), e as métricas de
malha fechada mostram assimetria entre subida (≈ 6 % de sobressinal) e descida (≈ 26 %).

## Fase 3 — Artigo (sessão dedicada separada)

**Decisão de 2026-09-13:** existe um rascunho antigo do COBENGE 2023, em coautoria com outro
orientando (`softwares_aeropendulo/simulador_aeropendulo/docs/utils/Template_Artigos_ST_COBENGE-2023.docx.pdf`),
mas ele **não será usado como base** — o artigo é planejado do zero, focado só no trabalho
próprio. Ver [`plano_artigo.md`](plano_artigo.md).

As métricas quantitativas que eram pré-requisito estão prontas (ver Fase 2); a Fase 3 pode
começar. Antes de redigir, decidir com o autor como tratar o atraso da função de transferência
publicada (nota no artigo, errata ou ambos).

## Fase 4 — Livro (sessão dedicada separada)

Plano detalhado em [`plano_livro.md`](plano_livro.md). Pode começar a qualquer momento,
independente das Fases 2 e 3 — a primeira decisão (público-alvo) é só de escopo, não de
material pronto.

## O que não fazer ainda

Para não perder o fio: nenhuma linha de artigo ou livro deve ser escrita antes de fechar a
pergunta de escopo respectiva (seção "Perguntas em aberto" de cada plano). O trabalho de
IA nas Fases 3 e 4, até lá, é só inventariar material e levantar opções — não redigir.
