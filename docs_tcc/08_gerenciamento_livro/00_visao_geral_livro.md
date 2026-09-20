---
titulo: "Visão Geral e Estado Atual do Livro 1"
data_criacao: "2026-09-19"
status: "em_andamento"
categoria: "gerenciamento_editorial"
tags: [livro1, kaobook, aeropendulo, controle, gemeo_digital, esp32]
---

# Visão Geral e Estado Atual do Livro 1

## 1. Identificação da Obra
* **Título Oficial:** *Controle de Sistemas Dinâmicos: Do Aeropêndulo Experimental ao Gêmeo Digital*
* **Subtítulo Oficial:** *Modelagem física, identificação paramétrica e implementação prática*
* **Autores:** Oséias D. de Farias e Raphael B. Teixeira
* **Vínculo Institucional:** Faculdade de Engenharia Elétrica, Universidade Federal do Pará (UFPA), Campus Universitário de Tucuruí
* **Diretório do Código-Fonte:** `/home/osfarias/workspace/workspace_mestrado/Projeto_Tcc_Oseias_Oficial/livro_lab_virtual/`
* **Classe Tipográfica Principal:** `memoir` (layout clássico de livro-texto de engenharia estilo Ogata/Nise/Pearson)
* **Templates Alternativos de Backup:** `/home/osfarias/workspace/workspace_mestrado/Projeto_Tcc_Oseias_Oficial/livro_lab_virtual/backup_templates_alternativos/` (`kaobook` e `scrbook`)
* **Compilador e Ferramental:** `pdflatex` + `biber` (BibLaTeX) + `makeindex`
* **Arquivo PDF Oficial:** [`livro_lab_virtual/main.pdf`](../../livro_lab_virtual/main.pdf) (75 páginas)

---

## 2. Linha do Tempo e Marcos Atingidos
1. **Definição da Estrutura Híbrida (Opção C):** Integração equilibrada entre fundamentação teórica rigorosa (mecânica analítica, identificação ARX e estabilidade) e implementação prática minuciosa (BOM, firmware C++, GUI CustomTkinter e VPython 3D).
2. **Setup Editorial Completo:** Clonagem e adaptação do motor `kaobook` (`kaobook.cls`, `kao.sty`, `kaobiblio.sty`, `kaorefs.sty`, `kaotheorems.sty`).
3. **Escrita da Primeira Edição Substantiva:** Produção integral de 9 capítulos, 4 apêndices e frontmatter/backmatter.
4. **Acoplamento de Recursos Visuais Vetoriais e Fotográficos:** Integração do DCL em TikZ, diagrama do ecossistema, topologia do controlador PID em malha fechada, fotos reais do aeropêndulo e capturas das interfaces.
5. **Resolução de Bibliografia Canônica:** Vínculo das fontes clássicas (Ogata, Nise, Aguirre, Ljung, Åström & Hägglund, Grieves, Quinalha) com geração de lista de referências ao final da obra.
6. **Métrica Atual do Documento:** **78 páginas compiladas** com sumário analítico, lista de ilustrações e tabelas.

---

## 3. Estrutura de Diretórios da Obra

```text
livro_lab_virtual/
├── main.tex                                 # Documento mestre de compilação
├── main.pdf                                 # Arquivo compilado final (78 páginas)
├── kaobook.cls, kao.sty, ...                # Motor tipográfico e estilos auxiliares
├── references.bib                           # Base BibTeX unificada
├── frontmatter/
│   ├── prefacio.tex                         # Motivação pedagógica e guia do leitor
│   └── notacao.tex                          # Tabela de variáveis, operadores e siglas
├── capitulos/
│   ├── 01_introducao.tex                    # Por que construir um laboratório de controle?
│   ├── 02_montagem_mecanica.tex             # Montagem da base, haste de carbono e motor
│   ├── 03_eletronica_instrumentacao.tex     # Ponte H, filtro RC, sensor e ESP32
│   ├── 04_firmware_esp32.tex                # Firmware determinístico (Ts = 20 ms) e telemetria
│   ├── 05_modelagem.tex                     # Dedução de torques, empuxo e linearização
│   ├── 06_identificacao_sistemas.tex        # PRBS, ARX, OLS e análise do atraso z
│   ├── 07_controle_pid.tex                  # PID digital discreto e assimetria gravitacional
│   ├── 08_interface_gui.tex                 # Interface CustomTkinter e telemetria em tempo real
│   └── 09_gemeo_digital.tex                 # Gêmeo 3D VPython/WebGL e sincronização
├── apendices/
│   ├── A_codigo_fonte.tex                   # Estrutura do repositório e trechos centrais
│   ├── B_bom_fornecedores.tex               # Lista de Materiais e custos estimados
│   ├── C_troubleshooting.tex                # Guia de Resolução de Problemas
│   └── D_exercicios.tex                     # Banco de exercícios teóricos e práticos
├── figuras/                                 # Gráficos, esquemas e fotos da bancada
└── tikz/                                    # Diagramas vetoriais matemáticos
```

