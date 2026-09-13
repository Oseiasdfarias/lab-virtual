---
fonte: síntese de todo docs_tcc/ — este arquivo é um ESQUELETO, plano ainda não definido com o usuário
gerado_em: 2026-09-13
---

# Plano do artigo (planejado do zero)

> Decisão de 2026-09-13: existe um rascunho antigo (COBENGE 2023, coautoria com outro
> orientando) em `softwares_aeropendulo/simulador_aeropendulo/docs/utils/Template_Artigos_ST_COBENGE-2023.docx.pdf`.
> Foi decidido **não usá-lo como base** — o artigo será planejado do zero, focado só no
> trabalho próprio (Aeropêndulo). O arquivo antigo continua no repositório sem uso.

## Material já disponível que sustenta um artigo

- **Modelagem matemática completa** do aeropêndulo (motor CC série + braço) em espaço de estados, com implementação em Python — `materiais_complementares/Modelagem_do_Sistema/Simulacoes/Aeropendulo_Python/arquivos_complementares/README.md` e Cap. 2 da monografia.
- **Identificação de sistemas** (PRBS + mínimos quadrados) aplicada ao protótipo real, com cadeia completa identificação → discreto→contínuo (Tustin) → validação → projeto de PI, em `materiais_complementares/Identificacao_de_Sistemas/identificacao_aeropendulo/ident_up/`.
- **Protótipo físico + firmware + interface + gêmeo digital** funcionando de ponta a ponta (arquitetura em `02_software/`), com dados reais de 9 ensaios coletados (`softwares_aeropendulo/src_interface/dados_de_ensaio/`).
- Referência direta de literatura próxima: *"A New Approach to Control A Driven Pendulum with PID Method"* (citado na modelagem) e a bibliografia levantada sobre braço levitador / TRMS / motor CC série (`04_materiais_complementares/bibliografia.md`).

## Lacunas a resolver antes de submeter

- Resultados atuais são qualitativos/visuais — sem RMSE/EQM. Um artigo tipicamente pede validação quantitativa (ver punch list em [`pendencias_documentacao.md`](pendencias_documentacao.md)).
- Decidir se o artigo foca em (a) o processo de identificação de sistemas, (b) a arquitetura do protótipo/gêmeo digital como ferramenta didática, ou (c) ambos.

## A decidir com o usuário

- [ ] Público-alvo / periódico ou evento de destino.
- [ ] Escopo: recorte do TCC (um capítulo específico) ou síntese do trabalho todo.
- [ ] Se serão necessários novos experimentos/dados para fortalecer a validação quantitativa.
- [ ] Coautoria (orientador Raphael Barros Teixeira).
