---
titulo: "Plano de Ação e Checklist de Implementação (Ciclos 1 e 2)"
autor: "Oséias Dias de Farias"
gerado_em: "2026-09-15"
status: "em_andamento"
tags: [plano_acao, checklist, implementacao, artigo1, livro1, v2_rlaas, artigo2, livro2]
---

# Plano de Ação e Checklist de Implementação
## Validação e Acompanhamento Etapa por Etapa

Este documento consolida o **plano de implementação prático** em 4 blocos sequenciais e acionáveis, com caixas de seleção para validação contínua.

---

## Bloco 1: Fechamento da Base Existente & Dívidas Técnicas (Hardware/Firmware)
> **Objetivo:** Garantir integridade técnica do protótipo físico e transparência nos dados já consolidados.

- [ ] **1.1 Transparência do PID no texto do Artigo/Livro**
  - Registrar formalmente a correção do termo derivativo ($K_d \frac{\Delta \theta}{T_s}$) em relação à fórmula histórica de 2023.
- [ ] **1.2 Recalibração prática do PID (se a bancada estiver acessível)**
  - Gravar firmware corrigido no ESP32 e ajustar $K_d$ para evitar sobreaquecimento/oscilação do motor.
- [ ] **1.3 Suporte a ganhos PID dinâmicos via Serial**
  - Alterar protocolo serial para permitir envio de $(K_p, K_i, K_d)$ pela interface gráfica (e futura API web) sem recompilar o firmware.
- [ ] **1.4 Unificação da pinagem do sensor de ângulo**
  - Harmonizar esquema elétrico e firmware (GPIO 2 vs GPIO 12) na documentação técnica.

---

## Bloco 2: Implementação do Ciclo 1 (Base Existente: Artigo 1 + Livro 1)
> **Objetivo:** Produção bibliográfica imediata e enriquecimento do Lattes utilizando os dados e códigos 100% prontos.

### 2.1 Artigo 1 (IEEE Latin America Transactions)
- [x] **2.1.1 Definição do periódico/conferência-alvo:** Selecionada a *IEEE Latin America Transactions* (Qualis A, 6-9 páginas, LaTeX IEEEtran).
- [x] **2.1.2 Esqueleto e estrutura de seções fechada:** Estrutura canônica modular (Introdução -> Fundamentação Teórica -> Metodologia -> Resultados -> Conclusão).
- [x] **2.1.3 Redação do primeiro rascunho completo:** Manuscrito modularizado em 5 seções em `artigo_ieee_latam/`, atingindo exatamente 6 páginas compiladas em PDF (`main.pdf`).
- [ ] **2.1.4 Revisão e submissão com o orientador**.

### 2.2 Livro 1 (1ª Edição — Guia Completo do Laboratório Virtual)
- [ ] **2.2.1 Definição editorial:** Título oficial, formato (e-book / impresso sob demanda) e registro de ISBN.
- [ ] **2.2.2 Estruturação do sumário detalhado em 5 Partes:**
  - *Parte I — Fundamentos Teóricos e Dinâmica de Pêndulos*.
  - *Parte II — Projeto e Montagem do Hardware Didático (Mecânica e Eletrônica)*.
  - *Parte III — Firmware em C++ e Sistemas de Tempo Real*.
  - *Parte IV — Identificação de Sistemas Aplicada com Python*.
  - *Parte V — Gêmeo Digital 3D e Interface Homem-Máquina*.
- [ ] **2.2.3 Redação modular dos capítulos** (reaproveitando Cap. 1 a 4 da monografia e notebooks).
- [ ] **2.2.4 Diagramação, capa e publicação**.

---

## Bloco 3: Desenvolvimento Técnico da Versão 2.0 (Plataforma Web RLaaS)
> **Objetivo:** Transformar a bancada local em um laboratório remoto em nuvem para alunos e pesquisadores externos.

### 3.1 Camada de Gateway Local (Bancada Física)
- [ ] **3.1.1 Desenvolver daemon/agente local em Python**:
  - Comunicação serial bidirecional com o ESP32.
  - Conexão segura com o backend via WebSockets / MQTT.
  - Consumo da fila de ensaios e upload automático do CSV gerado.

### 3.2 Camada Backend e Cloud (FastAPI / Redis / Banco de Dados)
- [ ] **3.2.1 Autenticação e gestão de usuários** (alunos, pesquisadores, administradores).
- [ ] **3.2.2 Fila assíncrona de ensaios (Job Queue)** com priorização e agendamento.
- [ ] **3.2.3 Módulo de segurança e validação de parâmetros (*Safety Sandbox*)**:
  - Limite estrito de ângulo ($\theta_{ref} \le 60^\circ$).
  - Limite de duty cycle do PWM ($u \le 80\%$) e duração máxima ($\le 90\text{ s}$).
  - Cooldown obrigatório do motor para proteção térmica.
- [ ] **3.2.4 Banco de dados para histórico público/privado de ensaios**.

### 3.3 Camada Frontend Web (Dashboard & Gêmeo Digital Web)
- [ ] **3.3.1 Portal web moderno** (formulário para submissão de ensaios e histórico).
- [ ] **3.3.2 Visualizador interativo de sinais** (gráficos interativos com Plotly/Chart.js).
- [ ] **3.3.3 Migração do Gêmeo Digital para Three.js (WebGL)**:
  - Renderização 3D do aeropêndulo direto no navegador sem necessidade de instalar Python/VPython localmente.
- [ ] **3.3.4 (Opcional) Transmissão de vídeo ao vivo da bancada via WebRTC**.

---

## Bloco 4: Implementação do Ciclo 2 (Artigo 2 + Livro 2 na Nuvem)
> **Objetivo:** Consolidação científica internacional da plataforma remota e nova produção de alto impacto.

- [ ] **4.1 Coleta de métricas da plataforma web** (tempo de resposta, estabilidade, ensaios realizados).
- [ ] **4.2 Artigo 2 (Revista Internacional de Educação/IoT)**:
  - Submissão em periódicos como *IEEE Transactions on Education* ou *Computer Applications in Engineering Education*.
  - Foco na arquitetura RLaaS e impacto pedagógico da democratização do laboratório.
- [ ] **4.3 Livro 2 (2ª Edição Ampliada do Livro 1)**:
  - Inclusão dos novos capítulos cobrindo arquitetura em nuvem, WebSockets, Three.js e laboratórios remotos como serviço.

