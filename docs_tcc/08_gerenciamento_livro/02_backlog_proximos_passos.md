---
titulo: "Backlog de Pendências e Próximos Passos do Livro 1"
data_criacao: "2026-09-19"
status: "ativo"
categoria: "gerenciamento_editorial"
tags: [livro1, backlog, pendencias, proximas_tarefas]
---

# Backlog de Pendências e Próximos Passos (Livro 1)

Este documento funciona como o painel de tarefas prioritárias para orientar as próximas sessões de trabalho e garantir o avanço contínuo da obra.

---

## 1. Prioridade Alta (Essencial para o Escopo Técnico)

- [ ] **Esquemático do Circuito Elétrico em TikZ (Capítulo 3):**
  - Desenhar o circuito analógico do filtro RC ($R = 1\,\text{k}\Omega, C = 2\,\mu\text{F}, f_c \approx 80\,\text{Hz}$) conectado ao pino do potenciômetro e à entrada do ADC do ESP32.
  - Desenhar a ponte H MOSFET simplificada conectada ao motor CC e pinos de controle PWM do ESP32.
- [ ] **Fluxograma da Rotina de Interrupção por Hardware (Capítulo 4):**
  - Modelar em TikZ o ciclo temporal rígido da ISR disparada a cada $T_s = 20\,\text{ms}$ (Leitura ADC $\rightarrow$ Média Móvel $\rightarrow$ Conversão Cinemática $\rightarrow$ PID $\rightarrow$ PWM $\rightarrow$ Envio Serial).
- [ ] **Gráfico de Resposta Temporal do PID em Malha Fechada (Capítulo 7):**
  - Gerar e exportar a partir dos dados CSV existentes (`materiais_complementares/analise_malha_fechada/`) o gráfico comparativo da onda quadrada mostrando a assimetria na subida ($6{,}1\%$) vs descida ($26{,}4\%$).
- [ ] **Congelamento da Tag no GitHub (Apêndice A):**
  - Criar e publicar no repositório `Oseiasdfarias/lab-virtual` a tag imutável `v1.0-livro`, garantindo que o leitor acesse exatamente os arquivos sincronizados com as explicações da obra.

---

## 2. Prioridade Média (Enriquecimento Didático e Visual)

- [ ] **Diagrama de Classes da Aplicação Python (Capítulo 8):**
  - Ilustrar em TikZ o padrão de Inversão de Dependência adotado no software (`ColetaDadosInterface` $\rightarrow$ `ColetaDados`, `SimuladorInterface` $\rightarrow$ `Simulador`).
- [ ] **Gráfico de Excitação PRBS (Capítulo 6):**
  - Extrair dos dados de ensaio gravados o gráfico das curvas de entrada PWM e resposta angular nos 60 segundos de identificação.
- [ ] **Simulação Comparativa Linear vs Não-Linear em Python (Capítulo 5):**
  - Inserir gráfico gerado por script `scipy.integrate.solve_ivp` comparando o modelo simplificado com a dinâmica trigonométrica completa.
- [ ] **Ampliação dos Exercícios (Apêndice D):**
  - Incluir seções adicionais de desafios práticos voltados a estudantes de pós-graduação e projetos integradores.

---

## 3. Prioridade Baixa / Futura (Depende de Recursos Externos)

- [ ] **Sessão Fotográfica da Bancada Física (Capítulo 2):**
  - *Condição:* Aguardar momento oportuno em que houver acesso físico ao aeropêndulo.
  - *Meta:* Fotografar em estúdio/fundo neutro os componentes isolados e a montagem passo a passo a 300 DPI com iluminação difusa.
- [ ] **Captura Conjugada GUI + WebGL (Capítulo 9):**
  - Capturar imagem de alta resolução em monitor widescreen com a interface CustomTkinter em um lado da tela e o simulador 3D VPython renderizando o pêndulo no navegador no outro lado.
- [ ] **Revisão Ortográfica e Gramatical Fina:**
  - Realizar leitura de prova completa antes do fechamento para submissão à editora.

---

## 4. Registro de Tarefas Concluídas nesta Rodada

- [x] Estruturação modular do livro em 9 capítulos e 4 apêndices com template `kaobook`.
- [x] Redação de todo o corpo textual inicial com rigor matemático e viés pedagógico.
- [x] Integração de 3 diagramas TikZ vetoriais (DCL, arquitetura e controle).
- [x] Inserção de fotos da bancada, interface gráfica e gêmeo digital existentes.
- [x] Configuração e compilação do BibLaTeX/Biber com citações bibliográficas resolvidas.
- [x] Verificação da compilação: **78 páginas** no PDF `livro_lab_virtual/main.pdf`.

