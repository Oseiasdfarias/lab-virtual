---
titulo: "Status Detalhado por Capítulo e Apêndice"
data_criacao: "2026-09-19"
status: "em_andamento"
categoria: "gerenciamento_editorial"
tags: [livro1, progresso, checklist_capitulos]
---

# Status Detalhado por Capítulo e Apêndice

Esta tabela registra o estado de cada componente do livro, indicando os elementos textuais, gráficos e de código já consolidados, além das pendências pontuais de cada módulo.

| Seção / Arquivo | Páginas Est. | Status | Elementos Já Inseridos | Pendências / Melhorias Futuras |
| :--- | :---: | :---: | :--- | :--- |
| **Frontmatter** (`prefacio.tex`, `notacao.tex`) | ~10 | Concluído | Contexto do TCC (UFPA), justificativa pedagógica, tabelas completas de notação e símbolos. | Revisão ortográfica final quando toda a obra estiver consolidada. |
| **Cap. 1: Introdução** (`01_introducao.tex`) | ~8 | Concluído | Lacuna teoria/prática, ecossistema em 3 camadas, foto do protótipo e TikZ de arquitetura. | Ajustar referências internas cruzadas para capítulos subsequentes. |
| **Cap. 2: Montagem Mecânica** (`02_montagem_mecanica.tex`) | ~8 | Concluído | Descrição do compensado, mancal, braço de fibra de carbono 2x2mm, motor e contrapeso. | Fotografias passo a passo de alta resolução (300 DPI) quando houver acesso à bancada. |
| **Cap. 3: Eletrônica e Instrumentação** (`03_eletronica_instrumentacao.tex`) | ~9 | Concluído | Especificação do potenciômetro, filtro RC (80 Hz), fonte 5V/3A, ESP32 e ponte H MOSFET. | Criar esquemático vetorial em TikZ da ponte H e filtro RC para substituir menções textuais. |
| **Cap. 4: Firmware ESP32** (`04_firmware_esp32.tex`) | ~10 | Concluído | Timer por hardware ($T_s = 20$\,ms), amostragem ADC, média móvel, gerador PRBS e protocolo CSV. | Diagrama de estados/fluxograma da ISR em TikZ. |
| **Cap. 5: Modelagem Dinâmica** (`05_modelagem.tex`) | ~9 | Concluído | Equações de Newton/Lagrange, dinâmica do motor, empuxo quadrático, Taylor e TikZ do DCL. | Inserir gráfico comparativo de simulação não linear vs linear (`solve_ivp`). |
| **Cap. 6: Identificação de Sistemas** (`06_identificacao_sistemas.tex`) | ~9 | Concluído | Teoria ARX, OLS em Python, tabela comparativa 2ª vs 10ª ordem, atraso $z$ e gráficos de validação. | Gráficos do sinal de excitação PRBS bruto ($u$ e $y$). |
| **Cap. 7: Controle PID** (`07_controle_pid.tex`) | ~8 | Concluído | PID incremental discreto, sintonia ($K_p, K_i, K_d$), análise da assimetria gravitacional e TikZ de blocos. | Gráficos em alta resolução da resposta transitória ao degrau ($0^\circ \leftrightarrow 10^\circ$). |
| **Cap. 8: Interface Gráfica** (`08_interface_gui.tex`) | ~7 | Concluído | Padrão Inversão de Dependência (ABC), CustomTkinter, `pyudev` e print real da interface. | Diagrama de classes UML simplificado em TikZ. |
| **Cap. 9: Gêmeo Digital 3D** (`09_gemeo_digital.tex`) | ~7 | Concluído | VPython/WebGL, rotação no espaço, sincronização de telemetria e captura do gêmeo 3D. | Captura lado a lado da tela da GUI e do navegador WebGL em operação simultânea. |
| **Apêndice A: Código-Fonte** (`A_codigo_fonte.tex`) | ~6 | Concluído | Estrutura do repositório, dependências Poetry e excertos das funções essenciais. | Substituir trechos ilustrativos pelos arquivos definitivos congelados na tag `v1.0-livro`. |
| **Apêndice B: BOM e Custos** (`B_bom_fornecedores.tex`) | ~3 | Concluído | Tabela com componentes, especificações, quantitativos e custos estimados em R$. | Atualizar cotações e links de distribuidores de componentes nacionais. |
| **Apêndice C: Troubleshooting** (`C_troubleshooting.tex`) | ~4 | Concluído | Matriz estruturada Sintoma $\rightarrow$ Causa Provável $\rightarrow$ Ação Corretiva em 4 subsistemas. | Expandir com cenários adicionais observados em ambiente de sala de aula/laboratório. |
| **Apêndice D: Exercícios** (`D_exercicios.tex`) | ~4 | Concluído | Problemas teóricos, analíticos, computacionais e práticos graduados por capítulo. | Adicionar gabarito ou roteiro de solução comentada em apêndice separado ou repositório. |

---

## Legenda de Status
* **Planejado:** Mapeado na proposta estrutural, ainda sem texto-base.
* **Em Elaboração:** Texto em rascunho com seções incompletas.
* **Concluído:** Texto redigido, equações formatadas, compilação sem erros no LaTeX.
* **Refinado:** Ilustrações vetoriais, fotografias definitivas e revisão ortográfica aplicadas.

