---
fonte: revisao_tcc/Template_TCC_FEE/bibtex-referencias.bib
gerado_em: 2026-09-12
---

## Aviso sobre qual arquivo .bib é o real

O documento mestre (`tcc_oseias_farias.tex`) carrega `\bibliography{bibtex-referencias}`, ou seja, o arquivo **`revisao_tcc/Template_TCC_FEE/bibtex-referencias.bib`** (17 entradas). Existe também `Capitulos/Referencias.bib` (132 linhas, conteúdo parecido mas não idêntico em formatação) que **não é o arquivo efetivamente usado na compilação** — provavelmente uma cópia/versão anterior. Este resumo é baseado no arquivo realmente usado.

## Quantidade total

**17 entradas** no `.bib` usado, sendo:
- 1 entrada claramente **fora de escopo / placeholder de template** (`exemplo` — artigo de física de partículas "Divergence Disease of the Pion-Baryon Interaction", nada a ver com o TCC — provavelmente sobra do template original do LaTeX).
- 2 entradas **duplicadas** (`vpython` e `vpython11`) apontando para a mesma URL, e essa URL está **errada**: ambas apontam para `customtkinter.tomschimansky.com` em vez do site oficial do VPython — erro de copiar/colar no `.bib`.
- Logo, ~14-15 referências efetivamente distintas e corretas.

## Categorias temáticas

1. **Sistemas de controle (livros-texto)**: Ogata (Engenharia de Controle Moderno), Nise (Engenharia de Sistemas de Controle).
2. **Máquinas elétricas / motor CC**: Umans (Máquinas Elétricas de Fitzgerald e Kingsley), Liceaga-Castro et al. (modelagem/identificação de motor CC série).
3. **Modelagem do Aeropêndulo/pêndulo acionado**: Mohammadbagheri & Yaghoobi (controle PID de "driven pendulum").
4. **Identificação de sistemas**: Aguirre (Introdução à Identificação de Sistemas), TCC de Klarissa Souza (identificação não-linear em espaço de estados por regressão esparsa, bancada motor-gerador, UFPA-Tucuruí).
5. **Gêmeos digitais**: Quinalha (Gêmeos digitais, futuro da indústria 4.0 — estudo de caso).
6. **Trabalhos correlatos do mesmo grupo/curso**: Cota, Yuri de Oliveira (artigo técnico sobre laboratório virtual de controle com VPython, mesma faculdade).
7. **Bibliotecas de software Python (sites oficiais, citadas como fonte técnica)**: VPython, CustomTkinter, Matplotlib, PySerial, NumPy, Pandas.
8. **Fora de escopo**: `exemplo` (física de partículas, não citado no corpo do texto — resíduo de template).

## Lista das ~15 referências centrais

| Chave BibTeX | Referência | Categoria | Onde é citada (capítulo) |
|---|---|---|---|
| `ogata5ed` | OGATA, K. Engenharia de Controle Moderno. Pearson, 2014. | Controle (livro-texto) | Cap. 2 (fundamentação teórica) |
| `nise2013` | NISE, S.N. Engenharia de sistemas de controle. 3ed. LTC, 2013. | Controle (livro-texto) | Cap. 1 (introdução/justificativa) |
| `umans2014` | UMANS, S.D. Máquinas Elétricas de Fitzgerald e Kingsley. 7ed. AMGH, 2014. | Máquinas elétricas | Cap. 2 (modelagem motor CC série) |
| `aguirre2004intro` | AGUIRRE, L.A. Introdução à identificação de sistemas. Editora UFMG, 2004. | Identificação de sistemas | Cap. 2 (2.4, não compilado) / base conceitual do Cap. 3 |
| `jesus` | LICEAGA-CASTRO et al. Series DC Motor Modeling and Identification. ICCAIRO, 2017. | Máquinas elétricas / identificação | Cap. 2 (modelagem motor CC série) |
| `amin` | MOHAMMADBAGHERI, A.; YAGHOOBI, M. A New Approach to Control a Driven Pendulum with PID Method. UkSim, 2011. | Aeropêndulo/pêndulo + PID | Cap. 2 (modelagem do braço) |
| `tcc_klarissa_ufpa` | SOUZA, Klarissa. Identificação não-linear no espaço de estados por regressão esparsa de bancada motor-gerador. UFPA-Tucuruí, 2023. | Identificação de sistemas (trabalho correlato local) | Cap. 3 (base teórica do método de identificação) |
| `quinalha2018gemeos` | QUINALHA, E. Gêmeos digitais, o futuro da indústria 4.0: estudo de caso. UTFPR, 2018. | Gêmeos digitais | Cap. 1 (introdução, conceito de gêmeo digital) |
| `yuri_tcc` | COTA, Y.O. Explorando o potencial do laboratório virtual de controle de sistemas com VPython no ensino de engenharia. UFPA-Tucuruí, 2023. | Trabalho correlato (mesmo grupo) | Cap. 1 (justificativa) |
| `vpython` / `vpython11` | Site oficial VPython (URL incorreta no .bib, aponta para CustomTkinter). | Software/biblioteca | Cap. 3 (gêmeo digital) |
| `customtkinter` | Site oficial CustomTkinter (T. Schimansky). | Software/biblioteca | Cap. 3 (interface gráfica) |
| `matplotlib` | Site oficial Matplotlib. | Software/biblioteca | Cap. 3 (interface gráfica, identificação) |
| `pyserial` | Documentação oficial PySerial (C. Liechti). | Software/biblioteca | Cap. 3 (interface gráfica) |
| `numpy_opl` | Introdução ao NumPy (A. Neto, OPL/UFC). | Software/biblioteca | Cap. 3 (interface gráfica, identificação) |
| `pandas` | Site oficial Pandas. | Software/biblioteca | Cap. 3 (interface gráfica) |

## Referência fora de escopo (não usar como fonte de conteúdo)

- `exemplo`: Y. Nogami e Akira Suzuki, "Divergence Disease of the Pion-Baryon Interaction in Quark-Based Models", Progress of Theoretical Physics, 1983 — artigo de física de partículas, sem relação com o tema; resíduo do template LaTeX original, aparentemente não citado no corpo do texto.
