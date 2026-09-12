---
fonte: síntese de todo docs_tcc/ — este arquivo é um ESQUELETO, plano ainda não definido com o usuário
gerado_em: 2026-09-12
---

# Plano do livro (rascunho a definir)

> Este arquivo é um ponto de partida, não um plano fechado. As seções "A decidir com o usuário" precisam de uma conversa antes de virar plano de fato.

## Material já disponível que sustenta um livro

O projeto tem naturalmente uma estrutura "didática" reaproveitável, mais ampla do que cabe num artigo:

- **Fundamentação teórica** de sistemas dinâmicos, motor CC série e modelagem de aeropêndulo (Cap. 2 da monografia).
- **Identificação de sistemas aplicada** passo a passo, com dados reais (PRBS, mínimos quadrados, validação) — bom material para um capítulo "prático" com exemplo replicável.
- **Projeto e construção de um protótipo didático do zero**: eletrônica (`materiais_complementares/Prototipagem_do_Braco_de_Helicoptero/parte_eletrica/`), estrutura física, firmware (ESP32/Arduino, com e sem PlatformIO), interface gráfica em Python — cobre hardware + firmware + software num só projeto, com fotos e diagramas já catalogados.
- **Simulação e gêmeo digital em Python** com código completo e reaproveitável.
- Já existe know-how de referência externa incorporado (blog "ThePoorEngineer", ver `04_materiais_complementares/bibliografia.md`) que parece ter inspirado a arquitetura — útil para comparação/creditação.

## A decidir com o usuário

- [ ] Público-alvo: livro técnico-acadêmico (equivalente a uma monografia expandida) ou livro didático/tutorial (formato "construa seu próprio aeropêndulo")?
- [ ] Formato de publicação (editora acadêmica, self-publishing, capítulo de livro coletivo)?
- [ ] Estrutura de capítulos — provavelmente expande os 4 capítulos atuais da monografia em mais unidades (ex.: separar hardware, firmware, software e modelagem em capítulos próprios, hoje concentrados no Cap. 3).
- [ ] Nível de detalhe de reprodutibilidade desejado (esquemas elétricos, BOM de componentes, lista de custos) — o material bruto existe em `materiais_complementares/Prototipagem_do_Braco_de_Helicoptero/` mas não está organizado como "receita" reproduzível ainda.
