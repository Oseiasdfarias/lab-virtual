---
fonte: revisao_tcc/Template_TCC_FEE/elementos_textuais/Cap_1_introducao.tex
gerado_em: 2026-09-12
---

## Observação

O capítulo 1 realmente compilado no PDF final é `elementos_textuais/Cap_1_introducao.tex` (não `Capitulos/Cap_1_introducao.tex`, que é uma versão-irmã ligeiramente diferente na redação, mas com o mesmo conteúdo). Capítulo completo, sem sinais de rascunho.

## Contexto / Motivação

- Sistemas de controle permeiam praticamente todas as áreas da engenharia (foguetes, ônibus espacial, usinagem automatizada, veículos autônomos) — cita Nise (2013).
- Projetar/analisar controladores exige abstrair sistemas físicos em equações matemáticas, o que é difícil para iniciantes.
- Implementar controladores exige competências multidisciplinares: eletrônica analógica/digital, programação, processamento de sinais, circuitos elétricos.
- O ensino teórico tradicional de sistemas de controle dificulta a conexão entre teoria e prática — cita o artigo técnico de Yuri Cota (2023, mesma faculdade/campus).

## Problema

- Alunos enfrentam dificuldade na transição do "mundo físico" para o "mundo matemático abstrato" (equações diferenciais, Laplace).
- Falta de estrutura operacional/laboratorial acessível para visualizar essa dinâmica na prática.

## Proposta / Solução

- Desenvolvimento de um protótipo (Aeropêndulo) + conjunto de softwares formando um "laboratório virtual" de baixo custo, com componentes acessíveis e software open source.
- Componentes do projeto: firmware para microcontrolador (C/C++, framework Arduino + PlatformIO, ESP32), interface de usuário para ajustes em tempo real, e um **gêmeo digital** (simulador 3D) do protótipo físico.
- Cita Grieves (2014, Universidade de Michigan) como referência conceitual de "gêmeo digital", aplicando o conceito à fase de operação/manutenção do produto.

## Objetivo geral

Desenvolver um laboratório virtual abrangente para o estudo de sistemas de controle, integrando protótipo, simulador e interface gráfica, permitindo investigar identificação de sistemas, desenvolvimento e otimização de controladores, e aplicação de IA em sistemas de controle.

Objetivo secundário declarado: aplicar na prática conhecimentos da graduação (sistemas de controle, eletrônica analógica/digital, programação, física, cálculo) em uma configuração física real.

## Objetivos específicos

a. **Desenvolver o protótipo do Aeropêndulo**: projetar estrutura física e elétrica.
b. **Desenvolver um simulador 3D (Gêmeo Digital)**: em Python + biblioteca VPython.
c. **Interface de Usuário**: GUI para manipular o sistema em tempo real, salvar dados de ensaio, testar em malha fechada.
d. **Aplicar Identificação de Sistema à Planta**: obter modelo via função de transferência discreta, método dos mínimos quadrados.
e. **Testar o sistema em Malha Fechada**: implementar controlador PID no firmware e validar.

## Escopo do trabalho

- Parte de uma modelagem matemática newtoniana, usada para demonstrar que essa abordagem se torna trabalhosa/impraticável em sistemas complexos — motivando o uso de identificação de sistemas.
- Interface gráfica permite executar ensaios, salvar dados, configurar sinal de referência (frequência, amplitude, offset) em tempo real.
- Firmware no microcontrolador (ESP32) cuida de comunicação USB serial, geração dos sinais de entrada e leitura do ângulo do braço.
- Gêmeo digital (simulador 3D) integra a dinâmica real com o ambiente computacional em tempo real.

## Metodologia (implícita no escopo/estrutura)

Não há seção de "Metodologia" formal; a abordagem é descrita via escopo: modelagem analítica → constatação de impraticabilidade → identificação de sistemas experimental → validação com ensaio de malha fechada (PID).

## Estrutura do trabalho (conforme descrito no próprio capítulo)

- Seção de fundamentação teórica (rotulada `fundamentacao_teorica`) foca na modelagem matemática.
- Seção de implementação do protótipo (`imple_aeropendulo`) documenta o processo de desenvolvimento até a planta.
- Seção de desenvolvimento de softwares (`dev_softwares`).
- Seção do fluxograma do laboratório virtual (`flu_lab_virtual`).
- Capítulo de Resultados (`cap_3`): identificação de sistemas (`indentificacao`) e ensaio em malha fechada com PID (`malha_fechada`).
- Capítulo de Conclusão (`cap_conclusao`): considerações finais (`concideracoes_finais`) e trabalhos futuros (`trabalhos_futuros`).
