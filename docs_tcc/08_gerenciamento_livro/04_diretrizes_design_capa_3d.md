---
titulo: "Diretrizes de Refinamento da Capa (Opção 3d — Perfil da Bancada)"
data_criacao: "2026-09-19"
status: "ativo"
categoria: "design_editorial"
tags: [capa, design_3d, refinamento, identidade_visual, memoir]
---

# Diretrizes de Refinamento da Capa: Opção 3d (Perfil Real da Bancada)

Com base no projeto enviado pelo Claude Design no diretório `teste-design/`, a opção selecionada para o livro é a **Opção 3d: Perfil da bancada — haste em repouso**.

Esta opção foi escolhida por capturar exatamente o espírito dos grandes livros de controle clássicos: **sóbria, minimalista, baseada em geometria de engenharia e sem ilustrações genéricas**.

Criamos a versão refinada e calibrada tecnicamente, salva em:
- **HTML Interativo de Apresentação:** [`livro_lab_virtual/design_capa/capa_refinada_3d.html`](../../livro_lab_virtual/design_capa/capa_refinada_3d.html)

---

## 1. Diagnóstico do Arquivo Original do Claude Design (Opção 3d)

No arquivo original `Identidade Visual - Livro Controle.dc.html`, a opção 3d possuía uma excelente estrutura geral, mas apresentava pequenas inconsistências técnicas e de escala frente à bancada física real:

1. **A Base Hexagonal de Madeira:**
   * *Original:* Polígono simples com linhas ligeiramente descentralizadas e espessura com perspectiva incongruente com a haste.
   * *Refinamento:* Aplicação de proporções isométricas limpas, espessura precisa representando a placa de compensado naval de 15 mm e marcação sutil das linhas centrais e pontos de usinagem.
2. **Ausência da Eletrônica Real de Bancada:**
   * *Original:* A opção 3d havia omitido a eletrônica fixada na base de madeira (que existia na opção 3c).
   * *Refinamento:* Integração discreta em escala de cinzas da fonte chaveada 5V/3A (com a grelha de ventilação) à esquerda, e do módulo ESP32 à direita, com as linhas pontilhadas de fiação subindo rente ao mastro de sustentação.
3. **Conjunto Motor e Hélice:**
   * *Original:* Pás da hélice renderizadas como arcos espessos sem nervuras aerodinâmicas e sem o spinner frontal do eixo motor.
   * *Refinamento:* Curvatura suave de sustentação aerodinâmica, espessura afunilada nas pontas e spinner cilíndrico realista em tinta sólida `#1D1D1F`.
4. **Camada Digital no Rodapé (Mundo Físico $\rightarrow$ Gêmeo Digital):**
   * *Conceito:* Mantivemos com precisão matemática a passagem fundamental que estrutura o livro: a curva analítica suave em cinza claro, o sinal amostrado em escada (ZOH) a cada $T_s = 20$\,ms, e a linha de saída do sinal PWM a 20 kHz.

---

## 2. Paleta Cromática Oficial Adotada (Escala Mineral de Cinzas)

| Código HEX | Amostra | Elemento de Aplicação no Livro |
| :---: | :---: | :--- |
| **`#F5F5F7`** | Papel Gelo / Mist | Fundo da capa frontal, contracapa e páginas de título. |
| **`#E3E3E5`** | Compensado Claro | Superfície superior da base hexagonal e preenchimentos secundários. |
| **`#C9C9CB`** | Cinza Técnico Médio | Curva de sinal analógico contínuo e espessura lateral da madeira. |
| **`#8A8A8C`** | Grafite Médio | Cotas, linhas auxiliares ($T_s = 20$\,ms) e nomes institucionais. |
| **`#616162`** | Ardósia / Subtítulo | Subtítulo da capa, nomes dos autores e legendas de figuras. |
| **`#1D1D1F`** | Tinta Preta Obsidian | Título principal, mastro de sustentação, haste, hélice e sinal amostrado. |

---

## 3. Tipografia Editorial Correspondente

* **Capa e Títulos:** **IBM Plex Sans** (pesos 600 Bold e 500 Medium) — transmite rigor de engenharia contemporânea, legibilidade impecável e precisão geométrica.
* **Subtítulo e Rodapés:** **IBM Plex Sans** (peso 400 Regular, cor `#616162`).
* **Símbolos e Cotas:** **IBM Plex Mono** (peso 500/600, tamanho compacto 6 a 8 pt).
* **Miolo LaTeX (Memoir):** Família **Palatino / NewPX** (`newpxtext` + `newpxmath`) para o corpo e fórmulas matemáticas, com títulos de seções em **TeX Gyre Heros**.

---

## 4. Próximos Passos de Integração no LaTeX
- [ ] Exportar o SVG vetorial da capa refinada em formato PDF vetorial independente (`capa_vetorial.pdf`).
- [ ] Inserir como primeira página da edição oficial em `livro_lab_virtual/main.tex` via pacote `pdfpages` ou ambiente nativo de capa do `memoir`.

