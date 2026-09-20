---
fonte: "Planejamento estruturado para submissão na IEEE Latin America Transactions"
gerado_em: "2026-09-15"
status: "em_elaboracao"
veiculo: "IEEE Latin America Transactions"
template: "IEEEtran (LaTeX, duas colunas)"
limite_paginas: "6 a 9 páginas"
idioma: "Português (ou Inglês sob demanda)"
tags: [artigo1, ieee_latam, plano_escrita, latex]
---

# Plano Detalhado do Artigo 1: IEEE Latin America Transactions

## 1. Diretrizes Editoriais do Periódico
* **Veículo:** *IEEE Latin America Transactions* (Região 9 da IEEE).
* **Indexação:** IEEE Xplore, Scopus, Web of Science, Qualis CAPES (A).
* **Taxa:** US$ 250 (apenas após o aceite formal).
* **Extensão obrigatória:** 6 a 9 páginas (no formato final de duas colunas IEEE).
* **Template:** Padrão IEEE `IEEEtran.cls` (LaTeX, duas colunas, espaçamento simples).
* **Terminologia:** Uso de "Index Terms" em vez de "Keywords"; tabelas limpas sem grades verticais; figuras em alta resolução dentro do corpo do texto.
* **Itens extras na submissão:** Graphical Abstract (imagem PNG de resumo) e Letter to the Editor.

---

## 2. Título do Artigo

* **Em Português:**  
  *“Desenvolvimento, Identificação Paramétrica ARX e Controle PID de um Aeropêndulo Experimental Integrado a Gêmeo Digital”*
* **Em Inglês:**  
  *“Development, ARX System Identification, and PID Control of an Experimental Aeropendulum Integrated with a Digital Twin”*

---

## 3. Autoria
* **Primeiro Autor:** Oséias Dias de Farias (Universidade Federal do Pará - UFPA).
* **Coautor / Orientador:** Raphael Barros Teixeira (Universidade Federal do Pará - UFPA).

---

## 4. Estrutura Detalhada das Seções (Meta: 7 a 8 páginas)

### Seção I: Introdução (~1 a 1,2 páginas)
* **Contexto:** Importância de sistemas subatuados e não lineares (aeropêndulos) no ensino e pesquisa em controle.
* **Problema:** Desafio de aproximar a teoria linear das restrições e não linearidades de bancadas físicas reais (atrito em pivô, atraso de transporte e dinâmica do atuador).
* **Proposta e Contribuições:** 
  1. Apresentação da bancada experimental aberta de aeropêndulo baseada em ESP32;
  2. Identificação paramétrica ARX comparativa (2ª vs 10ª ordem) com métricas quantitativas ($NRMSE$ e $RMSE$);
  3. Discussão transparente sobre discretização, atraso e convenções em $z$;
  4. Laço de controle PID fechado em hardware com monitoramento síncrono por Gêmeo Digital 3D.

### Seção II: Arquitetura da Plataforma Experimental (~1 a 1,5 páginas)
* **Estrutura Mecânica e Elétrica:** Haste articulada, motor CC, sensor potenciométrico, ponte H e microcontrolador ESP32 TTGO.
* **Firmware e Comunicação Determinística:** Laço de controle com período de amostragem fixo $T_s = 20\text{ ms}$ (50 Hz), telemetria serial CSV.
* **Interface Gráfica e Gêmeo Digital 3D:** Arquitetura em Python (CustomTkinter) e espelhamento dinâmico visual (VPython).

### Seção III: Modelagem Física Analítica (~1 página)
* **Dinâmica Não Linear do Braço:** Equações de Euler-Lagrange do movimento rotacional com torque gravitacional, atrito viscoso e força de empuxo da hélice.
* **Dinâmica Eletromecânica do Motor:** Modelo elétrico e aproximação estática de empuxo ($F \propto \omega^2 \propto u$).
* **Linearização em Torno do Ponto de Equilíbrio:** Obtenção da função de transferência contínua em torno de $\theta_0$.

### Seção IV: Identificação Paramétrica de Sistemas (~1,5 a 2 páginas)
* **Protocolo de Excitação:** Geração e aplicação do sinal PRBS (*Pseudo-Random Binary Sequence*) para garantia de excitação persistente na banda passante da planta.
* **Formulações Discretas ARX:** Modelo em equações de diferenças lineares estimado por Mínimos Quadrados.
* **Treinamento e Validação Cruzada:** Separação dos dados em $60\%$ (estimação) e $40\%$ (validação em malha aberta).
* **Resultados da Estimação:**
  - Modelo de 2ª ordem: $NRMSE = 51,35\%$, $RMSE = 1,62^\circ$.
  - Modelo de 10ª ordem: $NRMSE = 78,30\%$, $RMSE = 0,72^\circ$.
* **Discussão Crítica Metodológica:** Análise detalhada do impacto da inclusão de atraso de transporte nas potências de $z^{-1}$ vs $z$, demonstrando domínio técnico na conversão para espaço contínuo.

### Seção V: Projeto de Controle e Resultados Experimentais (~1,5 páginas)
* **Controlador PID Digital:** Algoritmo implementado no ESP32 com termo derivativo em relação ao erro de ângulo.
* **Ensaios em Malha Fechada:** Rastreamento de referências periódicas (onda quadrada $0^\circ \leftrightarrow 10^\circ$).
* **Análise Quantitativa de Desempenho:**
  - Sobressinal na subida: $\approx 6\%$.
  - Sobressinal na descida: $\approx 26\%$ (assimetria intrínseca gerada pela força restauradora da gravidade).
  - Tempo de acomodação ($t_s$), tempo de subida ($t_r$) e erro em regime nulo ($e_{ss} \approx 0$).

### Seção VI: Conclusões e Trabalhos Futuros (~0,5 página)
* Síntese das realizações práticas e validações experimentais.
* Conexão natural com a próxima etapa (versão web remota em nuvem - RLaaS).

### Referências Bibliográficas (~0,5 página)
* 20 a 30 referências relevantes (Ogata, Ljung, Chen, trabalhos de aeropêndulos em IEEE, monografia UFPA).

---

## 5. Roteiro Prático de Redação

- [ ] **Etapa 1:** Criar a pasta do artigo com o template oficial `IEEEtran.cls` no repositório.
- [ ] **Etapa 2:** Configurar o arquivo `.bib` com as referências essenciais e compilar o PDF base.
- [ ] **Etapa 3:** Redigir as Seções II e III (Hardware, Software e Modelagem).
- [ ] **Etapa 4:** Redigir a Seção IV (Identificação ARX, PRBS, gráficos e tabelas de NRMSE/RMSE).
- [ ] **Etapa 5:** Redigir a Seção V (Resultados em Malha Fechada e gráficos experimentais).
- [ ] **Etapa 6:** Redigir a Introdução, Conclusão, Abstract e Index Terms.
- [ ] **Etapa 7:** Revisão de extensão (garantir entre 6 e 9 páginas) e compilação do PDF final.
