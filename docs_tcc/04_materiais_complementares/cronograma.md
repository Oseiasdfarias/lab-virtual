---
fonte: materiais_complementares/cronograma_estrutura_tcc/, materiais_complementares/Modelos_de_Documentos_Uteis/, revisao_tcc/Template_TCC_FEE/Capitulos/ (comparação)
gerado_em: 2026-09-12
---

# Cronograma e Estrutura Planejada do TCC

## cronograma_estrutura_tcc/

- `cronogramaTCC_Oseias.xlsx` / `.pdf` / `.png` — cronograma de execução do TCC do autor (planilha + exports).
- `cronogramaTCC_profTeixeira_atualizado.pdf` — versão do cronograma atualizada/revisada pelo orientador (Prof. Raphael Teixeira).
- `estrutura_tcc.tex` / `.pdf` — documento LaTeX standalone com a estrutura de capítulos planejada originalmente (detalhado abaixo).
- `estrutura_tcc.zip` — provável pacote com os fontes do `estrutura_tcc.tex` (imagens/config auxiliares).

### Estrutura originalmente planejada (`estrutura_tcc.tex`)
1. **Introdução** — Justificativa; Objetivos; Escopo do Trabalho
2. **Revisão Bibliográfica** — Modelagem e Controle de Sistemas (Laplace, Espaço de Estados, Transformada Z); Identificação de Sistemas
3. **Simulador e Protótipo do Aeropêndulo** — Prototipagem (estrutural, elétrica, montagem); Simulador usando Python
4. **Desenvolvimento** — Fundamentação Teórica; Modelagem Matemática (Motor CC Série + Aeropêndulo, cada um com identificação de sistemas própria; junção dos modelos)
5. **Projeto de Controle** — Projeto por Função de Transferência / Espaço de Estados / Discretização (Z); Implementação (Firmware do microcontrolador + software de visualização gráfica)
6. **Resultados e Discussões**
7. **Conclusão** — Considerações Finais; Trabalhos Futuros
8. **Referências Bibliográficas**, Apêndices, Anexos, Glossário

## Modelos_de_Documentos_Uteis/
- `abntex2.pdf` — template/manual do pacote LaTeX `abntex2` (formatação ABNT), usado como base do documento final.
- `ANEXO II-Formatação da monografia.pdf` — norma institucional de formatação da monografia (UFPA).

## Comparação com a estrutura real da monografia final (`revisao_tcc/Template_TCC_FEE/Capitulos/`)

Capítulos efetivamente escritos:
1. `Cap_1_introducao.tex` — Introdução: Justificativa, Objetivos (Gerais/Específicos), Escopo do Trabalho — **igual ao planejado**.
2. `Cap_2_Desenvolvimento.tex` — Desenvolvimento, com subseções em `2_aeropendulo/` (descrição, fundamentação teórica, modelagem analítica, modelagem por identificação de sistemas) e `3_hardware_softwares/` (prototipagem, simulador em Python, interface gráfica, firmware, ecossistema, dev. de softwares) — **funde os antigos capítulos 3 ("Simulador e Protótipo") e 4 ("Desenvolvimento") do planejamento original em um único capítulo 2**, mais enxuto.
3. `Cap_3_Resultados_e_Discussoes.tex` — Desenvolvimento do Protótipo e Softwares; Identificação de sistema aplicado ao Aeropêndulo (Mínimos Quadrados); Ensaio em Malha Fechada com Controlador PID (Onda Quadrada, Onda Dente de Serra) — **corresponde ao capítulo 6 original**, mas incorpora resultados de identificação e controle que antes estavam previstos nos capítulos 4/5.
4. `Cap_4_ Conclusao.tex` — Considerações Finais; Trabalhos Futuros — **igual ao planejado**.

### Principais mudanças em relação ao plano original
- A estrutura final tem **4 capítulos** em vez dos ~6-8 originalmente esboçados: os capítulos "Revisão Bibliográfica", "Simulador e Protótipo", "Desenvolvimento" e "Projeto de Controle" foram consolidados em apenas 2 capítulos centrais (Desenvolvimento + Resultados e Discussões).
- Não há capítulo dedicado exclusivamente à "Revisão Bibliográfica" nem seção isolada de "Projeto de Controle" — esses conteúdos parecem ter sido absorvidos dentro de `2_aeropendulo/2_2_fundamentacao_teorica.tex` e nos resultados do capítulo 3.
- A separação conceitual "Motor CC Série" vs. "Aeropêndulo" (dois modelos a modelar e depois juntar) prevista no plano original não aparece como estrutura de capítulo na versão final — a pasta `2_aeropendulo/` sugere que o motor foi tratado como parte da modelagem do aeropêndulo, não como capítulo/seção própria.
- Em resumo: a estrutura real é **mais compacta e pragmática** que o planejamento inicial, mas cobre essencialmente os mesmos temas (introdução, teoria+protótipo+modelagem, resultados, conclusão).
