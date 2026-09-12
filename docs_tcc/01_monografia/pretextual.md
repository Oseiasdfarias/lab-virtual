---
fonte: revisao_tcc/Template_TCC_FEE/elementos_pretextuais/resumo.tex, revisao_tcc/Template_TCC_FEE/elementos_pretextuais/abstract.tex, revisao_tcc/Template_TCC_FEE/elementos_pretextuais/siglas.tex, revisao_tcc/Template_TCC_FEE/elementos_pretextuais/simbolos.tex
gerado_em: 2026-09-12
---

## Aviso importante

As listas de siglas e símbolos abaixo **existem no repositório mas estão comentadas no documento mestre** (`\input{elementos_pretextuais/siglas.tex}` e `simbolos.tex` estão desativados em `tcc_oseias_farias.tex`) — **não aparecem no PDF final**. Além disso, o conteúdo delas é genérico de template (CPU, FPGA, densidade de fluxo elétrico) e **não tem nenhuma relação com o Aeropêndulo, motor CC, identificação de sistemas ou PID** — parecem ter ficado do template original UFPA-FEE sem nunca terem sido customizadas para este trabalho. Trate como não confiável / não representativo do conteúdo real do TCC.

Não existe pasta `PreTextual/` dentro de `Template_TCC_FEE`; a estrutura equivalente lá se chama `elementos_pretextuais/`. Existe também `revisao_tcc/TCC-Oseas/PreTextual/` (versão antiga/paralela, não usada aqui — pode estar desatualizada em relação à versão final).

## Resumo (texto quase integral)

> Este trabalho apresenta um laboratório virtual abrangente para o estudo de sistemas de controle, que combina a integração de um protótipo físico, simulador 3D e uma interface gráfica interativa. A motivação para este projeto reside na intrínseca complexidade associada à compreensão de sistemas de controle, que frequentemente apresenta desafios, sobretudo para estudantes que precisam transpor a barreira de abstrair sistemas físicos em termos de equações matemáticas. Para o desenvolvimento do projeto foi implementado um protótipo do Aeropêndulo completo com um conjunto de software que permite a interação do usuário com o sistema físico, possibilitando ao usuário realizar modificações nos parâmetros do sistema em tempo real, além disso, foi elaborado um gêmeo digital para espelhar a dinâmica do protótipo do Aeropêndulo a partir de um simulador 3D, por fim, foi realizado testes para a validação do laboratório, sendo eles: aplicação de identificação de sistema usando função de transferência discreta e mínimos quadrados e teste em malha fechada com controlador PID. O projeto foi hospedado no GitHub, a fim de disseminar o conhecimento e permitir que entusiastas, estudantes e pesquisadores tenham acesso ao projeto completo. A combinação de protótipos, simuladores, interface gráfica e integração de diversas disciplinas da Engenharia Elétrica cria um ambiente de aprendizado envolvente e eficaz para o estudo de sistemas de controle. Essa abordagem reduz a resistência inicial dos alunos e promove uma compreensão mais profunda dos conceitos e aplicações dessa área. Por meio da prática, os estudantes podem perceber a relevância das abstrações matemáticas na resolução de problemas reais, preparando-os para lidar com sistemas de controle complexos e desafiadores.

**Palavras-chave**: Aeropêndulo, identificação de sistema, protótipo, simulador, Gêmeo Digital.

## Abstract (texto quase integral)

> This work presents a comprehensive virtual laboratory for the study of control systems, which combines the integration of a physical prototype, 3D simulator and an interactive graphical interface. The motivation for this project lies in the intrinsic complexity associated with understanding control systems, which often presents challenges, especially for students who need to overcome the barrier of abstracting physical systems in terms of mathematical equations. To develop the project, an Aeropendulum prototype was implemented, complete with a set of software that allows the user to interact with the physical system, enabling the user to make changes to the system's parameters in real time. In addition, a digital twin was developed to mirror the dynamics of the Aeropendulum prototype using a 3D simulator. Finally, tests were carried out to validate the laboratory, including: application of system identification using discrete transfer function and least squares and closed loop testing with a PID controller. The project has been hosted on GitHub in order to disseminate knowledge and allow enthusiasts, students and researchers to have access to the complete project. The combination of prototypes, simulators, graphical interface and integration of various Electrical Engineering disciplines creates an engaging and effective learning environment for the study of control systems. This approach reduces students' initial resistance and promotes a deeper understanding of the concepts and applications in this area. Through practice, students can see the relevance of mathematical abstractions in solving real problems, preparing them to deal with complex and challenging control systems.

**Keywords**: Aeropendulum, system identification, prototype, simulator, digital twin.

## Lista de siglas (arquivo `siglas.tex` — NÃO usada no PDF final, conteúdo genérico não relacionado ao TCC)

| Sigla | Significado |
|---|---|
| CPU | Central Processing Unit |
| PLD | Programmable Logic Device |
| SPLD | Simple Programmable Logic Device |
| CPLD | Complex Programmable Logic Device |
| ASIC | Application Specific Integrated Circuit |
| FPGA | Field Programmable Gate Arrays |
| VHDL | VHSIC Hardware Description Language |
| VHSIC | Very High Speed Integrated Circuit |
| HDL | Hardware Description Language |

## Lista de símbolos (arquivo `simbolos.tex` — NÃO usada no PDF final, conteúdo genérico de eletromagnetismo, não relacionado ao Aeropêndulo)

| Símbolo | Significado |
|---|---|
| 𝓓 | Densidade de Fluxo Elétrico Instantânea (C/m²) |
| 𝓑 | Densidade de Fluxo Magnético Instantânea (Wb/m²) |
| 𝓔 | Intensidade de Campo Elétrico Instantânea (V/m) |
| 𝓗 | Intensidade de Campo Magnético Instantânea (A/m) |

### Símbolos reais usados no corpo do TCC (não estão nesta lista, extraídos do Cap. 2 — modelagem)

θ (ângulo do braço), F_e (empuxo), J_b (momento de inércia do braço), c (amortecimento viscoso do pivô), m, g, d (massa, gravidade, distância ao pivô), ω (velocidade angular do motor), K_m (ganho empuxo/velocidade), J_m (momento de inércia do motor), b (amortecimento viscoso do motor), T_e/T_c (torque eletromagnético/de carga), Φ (fluxo magnético), K_0 (indutância mútua), R_a/R_f/L_a/L_f (resistências/indutâncias de armadura e campo), V (tensão), i (corrente).
