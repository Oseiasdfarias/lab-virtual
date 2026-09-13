---
fonte: softwares_aeropendulo/simulador_aeropendulo/docs/utils/Template_Artigos_ST_COBENGE-2023.docx.pdf (lido integralmente, 21 páginas)
gerado_em: 2026-09-13
---

# Plano do artigo

> Achado principal desta revisão: **já existe um manuscrito quase pronto**, não apenas uma
> intenção. As seções abaixo foram reescritas em cima disso — não é mais um plano do zero.

## O que já existe (achado em 2026-09-13)

Dentro de `softwares_aeropendulo/simulador_aeropendulo/docs/utils/` há um arquivo chamado
`Template_Artigos_ST_COBENGE-2023.docx.pdf` que, apesar do nome, **não é um template em
branco** — é um rascunho de artigo já escrito para o COBENGE 2023 (51º Congresso Brasileiro
de Educação em Engenharia), com 21 páginas e as seguintes seções com texto real:

- **Introdução** — completa, com framing pedagógico (evasão em cursos de engenharia,
  simulação como ferramenta de ensino).
- **Metodologia** — dois módulos:
  - **Módulo 1 — MAGLEV** (levitação magnética): modelagem em espaço de estados, controle
    integral com observador, técnica de Ackermann para alocação de polos, simulação
    numérica via `scipy.integrate.solve_ivp`. Este módulo **não é seu** — é baseado no TCC de
    Milhomem (2010) e no artigo de Costa, Silva e Teixeira (2012), de um colega orientado
    pelo mesmo professor (Raphael B. Teixeira). O artigo é conjunto.
  - **Módulo 2 — Aeropêndulo** — modelagem por Newton/momentos angulares, linearização,
    diagrama de blocos, simulador 3D em VPython. Este módulo **é o seu trabalho** (figuras
    marcadas "Fonte: Autor, 2023").
- **Conceitos utilizados em ambos os módulos** — Python e bibliotecas (NumPy, SciPy,
  Control, SymPy, Matplotlib), VPython, proposta pedagógica.
- **Resultados** — para os dois módulos, com prints das interfaces 3D e gráficos de
  resposta em malha fechada.
- **Conclusão** — completa.
- **Referências** — lista completa, formatada.

**O que falta, pelo que dá para ver no PDF:**
- Numeração de figuras e equações ainda tem placeholders (`xx`, `(X)`) em vários pontos —
  precisa de uma passada de revisão final antes de submeter.
- Resumo/abstract e dados de autoria não estão no corpo (a norma do COBENGE pede isso só no
  formulário de submissão online, não no arquivo) — precisam ser escritos à parte.
- Seção "Agradecimentos" está vazia (só o título).
- O evento-alvo original (COBENGE 2023, Rio de Janeiro, 18–20/set/2023) **já aconteceu**.
  Para usar este rascunho é preciso decidir um novo destino: outra edição do COBENGE (checar
  data/chamada vigente) ou outro evento/periódico.
- Os resultados do módulo Aeropêndulo são só um gráfico de resposta em malha fechada, sem
  métrica de erro — mesma lacuna já identificada na monografia (ver
  [`pendencias_documentacao.md`](pendencias_documentacao.md)).

**Existe uma segunda cópia**, mais curta (17 páginas), em
`softwares_aeropendulo/firmwares_microcontroladores/Arduino_IDE/arduino_uno/`. Parece uma
versão anterior/incompleta da mesma — **não editar as duas**; usar a de 21 páginas como
fonte e decidir depois se a curta deve ser removida ou é só material de histórico.

## Por que isso muda a prioridade

Terminar este rascunho é muito mais barato do que escrever um artigo do zero, e está mais
adiantado do que qualquer outro produto deste plano de publicações. Antes de pensar em
título/escopo/coautoria como se fosse um projeto novo, a primeira pergunta é: **este
manuscrito ainda serve, ou o enfoque mudou desde 2023?**

## Checklist para retomar (sessão dedicada)

- [ ] **O `.docx` editável não está no repositório** (já verificado — o único `.docx`
      próximo, `untitled-document-2b1a4328....docx`, tem só uma equação solta, não o
      manuscrito). O PDF foi exportado do Google Docs (metadado `Producer: ... Google Docs
      Renderer`), então o documento original provavelmente ainda existe no Google Drive de
      quem escreveu — vale localizar lá antes de re-digitar 21 páginas a partir do PDF.
- [ ] Falar com o coautor do módulo MAGLEV — o artigo é conjunto, decisão de submissão não é
      só sua.
- [ ] Confirmar com o Prof. Raphael B. Teixeira se o rascunho ainda reflete o que ele quer
      submeter, e para qual evento/edição.
- [ ] Resolver as numerações pendentes (`xx`, `(X)`) de figuras e equações.
- [ ] Decidir se vale fortalecer a seção de Resultados do módulo Aeropêndulo com métrica
      quantitativa (RMSE/NRMSE do modelo, tempo de acomodação e sobressinal em malha
      fechada) — os dados para isso já existem nos 9 CSVs de ensaio do repositório.
- [ ] Escrever resumo/abstract e verificar normas atualizadas de formatação do evento-alvo
      (a versão de 2023 exigia até 12 páginas, sem dados de autor no corpo do arquivo).
- [ ] Escrever Agradecimentos.

## Perguntas em aberto para a sessão dedicada

- [ ] O enfoque do artigo (laboratório virtual com dois módulos, MAGLEV + Aeropêndulo)
      ainda é o que você quer, ou prefere um artigo separado focado só no Aeropêndulo,
      aproveitando o texto do módulo 2 como base?
- [ ] Evento/periódico de destino e prazo.
- [ ] Ordem e lista de autoria (você, o colega do MAGLEV, o orientador).

## Como retomar esta sessão

Ao abrir uma sessão dedicada ao artigo, comece por:
1. Ler este arquivo inteiro.
2. Abrir o PDF de 21 páginas e conferir se ele ainda reflete a intenção atual.
3. Resolver a pergunta de enfoque (mono-módulo vs. dois módulos) antes de tocar em texto.
