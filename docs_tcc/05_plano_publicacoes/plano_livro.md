---
fonte: síntese de todo docs_tcc/ + achados de 2026-09-13 (ver plano_artigo.md)
gerado_em: 2026-09-13
---

# Plano do livro

> Este arquivo é um ponto de partida, não um plano fechado. A seção "Perguntas em aberto"
> precisa de uma conversa antes de virar plano de fato — mas, diferente do artigo, aqui não
> há nenhum rascunho pré-existente para revisar primeiro. É trabalho a criar do zero.

## Material já disponível que sustenta um livro

O projeto tem naturalmente uma estrutura "didática" reaproveitável, mais ampla do que cabe
num artigo:

- **Fundamentação teórica** de sistemas dinâmicos, motor CC série e modelagem de
  aeropêndulo — Cap. 2 da monografia (`revisao_tcc/Template_TCC_FEE/Capitulos/2_aeropendulo/`).
- **Identificação de sistemas aplicada** passo a passo, com dados reais (PRBS, mínimos
  quadrados, validação) — bom material para um capítulo "prático" com exemplo replicável.
  Cadeia mais completa em `materiais_complementares/Identificacao_de_Sistemas/identificacao_aeropendulo/ident_up/`.
- **Projeto e construção de um protótipo didático do zero**: eletrônica
  (`materiais_complementares/Prototipagem_do_Braco_de_Helicoptero/parte_eletrica/`),
  estrutura física, firmware (ESP32/Arduino, com e sem PlatformIO), interface gráfica em
  Python — cobre hardware + firmware + software num só projeto, com fotos e diagramas já
  catalogados.
- **Simulação e gêmeo digital em Python** com código completo e reaproveitável
  (`softwares_aeropendulo/simulador_aeropendulo/`).
- **Uma dedução de modelagem já escrita para publicação**, no rascunho de artigo do COBENGE
  (ver [`plano_artigo.md`](plano_artigo.md)) — a seção "Módulo 2 — Aeropêndulo" ali pode
  virar ponto de partida de um capítulo, já que passou por uma rodada de redação e revisão.
- Know-how de referência externa incorporado (blog "ThePoorEngineer", ver
  `04_materiais_complementares/bibliografia.md`) que parece ter inspirado a arquitetura —
  útil para comparação/creditação.

## Duas direções possíveis (a decidir primeiro — tudo mais depende disso)

| | Técnico-acadêmico | Guia prático |
| --- | --- | --- |
| Público | Estudantes de controle/engenharia elétrica, nível de monografia expandida | Makers, professores de ensino técnico, hobbistas de eletrônica |
| Tom | Formal, com rigor matemático completo | Passo a passo, "construa o seu" |
| Reaproveita bem | Cap. 2 (modelagem), identificação de sistemas | Prototipagem, firmware, montagem |
| O que falta mais | Pouco — a monografia já é quase nesse registro | Lista de materiais com custo, esquemas elétricos organizados como receita, fotos passo a passo |
| Risco principal | Ficar redundante com a própria monografia sem agregar | Exigir documentação de reprodutibilidade que hoje não existe organizada |

## Checklist para retomar (sessão dedicada)

- [ ] Decidir a direção (tabela acima) — sem isso, nenhum outro item deste plano pode
      avançar.
- [ ] Se **guia prático**: levantar o inventário completo de materiais e custos a partir de
      `materiais_complementares/Prototipagem_do_Braco_de_Helicoptero/parte_eletrica/`
      (hoje são fotos e desenhos soltos, não uma lista compilada).
- [ ] Se **guia prático**: decidir se os esquemas elétricos existentes (`utils/esquematico_aeropendulo.png`,
      `utils/arquitetura_firmware*.png`) bastam ou precisam ser refeitos em ferramenta
      própria (KiCad/Fritzing) para qualidade de publicação.
- [ ] Se **técnico-acadêmico**: mapear explicitamente quais capítulos da monografia viram
      quais capítulos do livro, e o que precisa de expansão (a monografia é enxuta; um livro
      pede mais contexto e exemplos).
- [ ] Definir formato de publicação (editora acadêmica, self-publishing, capítulo de livro
      coletivo) — isso determina extensão-alvo, licenciamento e prazo.
- [ ] Estrutura de capítulos candidata — provavelmente expande os 4 capítulos atuais da
      monografia em mais unidades (ex.: separar hardware, firmware, software e modelagem em
      capítulos próprios, hoje concentrados no Cap. 3).

## Perguntas em aberto para a sessão dedicada

- [ ] Público-alvo — ver tabela de direções acima.
- [ ] Formato de publicação.
- [ ] Nível de detalhe de reprodutibilidade desejado, se for guia prático.
- [ ] Prazo — existe alguma janela (defesa, evento, oportunidade editorial) que deveria
      pautar o ritmo?

## Como retomar esta sessão

Ao abrir uma sessão dedicada ao livro:
1. Ler este arquivo inteiro e a tabela de direções.
2. Responder a pergunta de direção antes de qualquer outra coisa — todo o resto do plano
   depende dela.
3. Só depois entrar em estrutura de capítulos e cronograma de escrita.
