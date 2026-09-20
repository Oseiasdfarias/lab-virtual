---
fonte: revisao_tcc/Template_TCC_FEE/tcc_oseias_farias.tex, revisao_tcc/Template_TCC_FEE/parte_externa/capa_folharosto.tex, revisao_tcc/Template_TCC_FEE/elementos_textuais/Cap_1_introducao.tex, revisao_tcc/Template_TCC_FEE/Capitulos/**, revisao_tcc/Template_TCC_FEE/elementos_pretextuais/**, revisao_tcc/Template_TCC_FEE/bibtex-referencias.bib
gerado_em: 2026-09-12
---

## Nota metodológica importante (leia antes de tudo)

O diretório `revisao_tcc/Template_TCC_FEE/` contém **arquivos duplicados/paralelos** para o Cap. 1, Cap. 3, Cap. 4 e para a bibliografia. O arquivo mestre `tcc_oseias_farias.tex` (o que realmente é compilado) resolve a ambiguidade assim:

- **Cap. 1 (Introdução)**: usa `elementos_textuais/Cap_1_introducao.tex` — **NÃO** `Capitulos/Cap_1_introducao.tex` (que existe mas é uma versão-irmã ligeiramente mais antiga, com parágrafos quebrados de forma diferente). Os resumos abaixo usam a versão realmente compilada.
- **Cap. 2 (Desenvolvimento)**: `\input{Capitulos/Cap_2_Desenvolvimento}`, que por sua vez só inclui alguns dos arquivos de `Capitulos/2_aeropendulo/` e `Capitulos/3_hardware_softwares/` (ver seção de status abaixo — vários `\input` estão comentados).
- **Cap. 3 (Resultados) e Cap. 4 (Conclusão)**: usam os arquivos em `Capitulos/` (as cópias antigas desses capítulos em `elementos_textuais/` não são usadas; duplicatas foram removidas em 2026-09-13 e o texto antigo segue em `revisao_tcc/TCC-Oseas/`).
- **Bibliografia**: `\bibliography{bibtex-referencias}` aponta para `revisao_tcc/Template_TCC_FEE/bibtex-referencias.bib` (17 entradas) — **NÃO** para `Capitulos/Referencias.bib` (132 linhas, conteúdo similar mas não é o arquivo carregado na compilação final).
- **Lista de siglas e símbolos** (`elementos_pretextuais/siglas.tex`, `simbolos.tex`): existem mas estão **comentadas** no documento mestre (não aparecem no PDF final) e, além disso, o conteúdo é genérico/de template (CPU, FPGA, VHDL, densidade de fluxo elétrico) e **não tem relação com o Aeropêndulo** — parecem sobras do template original, nunca customizadas.
- A pasta `revisao_tcc/TCC-Oseas/PreTextual/` também existe como versão antiga/alternativa (`Resumo.tex`, `Abstract.tex`, `lista_siglas.tex`, `lista_de_simbolos.tex`); não foi usada aqui pois `Template_TCC_FEE` é a versão final confirmada por git log.

## Título completo

**DESENVOLVIMENTO DE PROTÓTIPO E GÊMEO DIGITAL COMO FERRAMENTA PARA UM LABORATÓRIO VIRTUAL COM FOCO EM MODELAGEM E CONTROLE DE SISTEMAS DINÂMICOS**

- Autor: Oséias Dias de Farias
- Orientador: Prof. Dr. Raphael Barros Teixeira
- Instituição: Universidade Federal do Pará (UFPA), Campus Universitário de Tucuruí, Faculdade de Engenharia Elétrica
- Local/Ano: Tucuruí, 2023
- Natureza: Trabalho de Conclusão de Curso (TCC) — Bacharelado em Engenharia Elétrica

## Tema

Desenvolvimento de um laboratório virtual para ensino/pesquisa em sistemas de controle, integrando um protótipo físico de baixo custo (Aeropêndulo — 1 grau de liberdade, braço com hélice/motor CC série), um firmware embarcado (ESP32), uma interface gráfica de usuário e um gêmeo digital (simulador 3D em VPython).

## Objetivo geral

Desenvolver um laboratório virtual abrangente para o estudo de sistemas de controle, integrando protótipo, simulador e interface gráfica, aplicável à identificação de sistemas, desenvolvimento/otimização de controladores e, potencialmente, IA aplicada a controle.

## Objetivos específicos

a. Desenvolver o protótipo do Aeropêndulo (estrutura física e elétrica);
b. Desenvolver um simulador 3D / gêmeo digital (Python + VPython);
c. Desenvolver interface de usuário (configuração em tempo real, salvamento de dados, testes em malha fechada);
d. Aplicar identificação de sistemas à planta (função de transferência discreta via mínimos quadrados);
e. Testar o sistema em malha fechada (controlador PID no firmware).

## Estrutura de capítulos

| Capítulo | Conteúdo (1-2 linhas) |
|---|---|
| 1. Introdução | Justificativa (ensino de sistemas de controle é abstrato/difícil), objetivos, escopo e estrutura do trabalho. |
| 2. Desenvolvimento — Aeropêndulo (teoria) | Fundamentação teórica e modelagem analítica (Newton/momento angular para o braço; Kirchhoff + eletromecânica para o motor CC série); descrição do sistema e modelagem por identificação estão praticamente vazias/incompletas. |
| 2/3. Desenvolvimento — Hardware/Softwares | Prototipagem física (estrutura, componentes eletrônicos), firmware (PlatformIO/ESP32), gêmeo digital (VPython), interface gráfica (CustomTkinter/Matplotlib/PySerial/Pandas/NumPy), fluxograma do ecossistema. |
| 3. Resultados e Discussões | Identificação de sistemas via PRBS + mínimos quadrados (modelo de 2ª ordem falhou, modelo de 10ª ordem validado qualitativamente); ensaio em malha fechada com PID sintonizado por tentativa e erro (onda quadrada e dente de serra). |
| 4. Conclusão | Considerações finais (validação bem-sucedida dos subsistemas), trabalhos futuros (mais métodos de identificação, controladores clássicos/IA, expansão do laboratório, documentação e vídeos no GitHub). |
| Pré-textual | Resumo/Abstract curtos e completos; listas de siglas/símbolos genéricas e não usadas no PDF final. |
| Referências | 17 entradas no .bib efetivamente usado (livros, artigos, TCCs correlatos, sites oficiais de bibliotecas Python). |

## Status de completude por capítulo/arquivo (sinais de rascunho)

| Arquivo | Status | Evidência |
|---|---|---|
| `elementos_textuais/Cap_1_introducao.tex` | **Completo** | Texto corrido, objetivos e escopo bem definidos, sem TODOs. |
| `Capitulos/2_aeropendulo/2_1_descricao.tex` | **Vazio / placeholder** | Conteúdo literal: `teste\nteste\nteste\nteste`. Não incluído no PDF final (linha `\input` comentada em `Cap_2_Desenvolvimento.tex`). |
| `Capitulos/2_aeropendulo/2_2_fundamentacao_teorica.tex` | **Completo, porém curto** | Só a introdução da fundamentação teórica (2 parágrafos); a seção "Identificação de Sistemas" citada no objetivo não está aqui. |
| `Capitulos/2_aeropendulo/2_3_modelagem_analitica.tex` | **Completo** | Modelagem matemática detalhada (motor CC série + braço) com equações numeradas até a linearização e função de transferência. |
| `Capitulos/2_aeropendulo/2_4_modelagem_identificacao_sistemas.tex` | **Rascunho abandonado** | 2 linhas; termina com `CONTINUA ...`. Não incluído no PDF final (linha `\input` comentada). O conteúdo real sobre identificação de sistemas (mínimos quadrados, PRBS) acabou sendo escrito diretamente no Cap. 3 (Resultados). |
| `Capitulos/Cap_2_Desenvolvimento.tex` | **Parcial** | Vários `\input`/`\section` comentados (descrição do sistema, identificação de sistemas); a numeração de seções fica quebrada (um `\subsection` sem `\section` pai, pois a seção 2.1 foi comentada). |
| `Capitulos/3_hardware_softwares/*.tex` (7 arquivos) | **Completos** | Prototipagem, dev_software, python, simulador (gêmeo digital), interface gráfica, firmware, ecossistema — todos com texto e referências a figuras. |
| `Capitulos/Cap_3_Resultados_e_Discussoes.tex` | **Completo** | Narrativa extensa dos ensaios, código Python incluso, equações e resultado qualitativo. Sem análise quantitativa de erro (RMSE/EQM comentado no código-fonte como não realizado). |
| `Capitulos/Cap_4_ Conclusao.tex` (note o espaço no nome do arquivo) | **Completo** | Considerações finais e trabalhos futuros bem desenvolvidos. |
| `elementos_pretextuais/resumo.tex` / `abstract.tex` | **Completos** | Resumo e abstract bem escritos e simétricos. |
| `elementos_pretextuais/siglas.tex` / `simbolos.tex` | **Não usados / desatualizados** | Conteúdo genérico de template (CPU, FPGA, campo elétrico) sem relação com o Aeropêndulo; comentados no documento mestre. |
| `bibtex-referencias.bib` | **Completo mas com 1 erro de dado** | Entradas `vpython` e `vpython11` são duplicadas e ambas apontam por engano para a URL do CustomTkinter em vez do site oficial do VPython. Contém também uma entrada de exemplo/placeholder não relacionada ao trabalho (`exemplo`, artigo de física de partículas). |

## Conclusão geral sobre o estado da monografia

O trabalho está **majoritariamente completo e coerente** nos capítulos efetivamente compilados (Introdução, parte de modelagem analítica, todo o capítulo de hardware/software, Resultados e Conclusão). As lacunas ficam concentradas na **seção de descrição do sistema (placeholder "teste")** e na **seção de modelagem por identificação de sistemas teórica (abandonada com "CONTINUA...")** — ambas conscientemente excluídas da compilação final pelo autor (via comentário dos `\input`), e o conteúdo equivalente foi na prática absorvido pelo Capítulo 3 (Resultados), que descreve o método de mínimos quadrados/PRBS de forma completa e aplicada.
