# Redesenho da Documentação Online (Mapa do Laboratório) — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transformar o site MkDocs (`docs/`) de uma coleção de páginas de software num mapa
pedagógico completo do Laboratório Virtual/Aeropêndulo, cobrindo protótipo, modelagem,
identificação de sistemas, controle e resultados — não só software.

**Architecture:** Site estático MkDocs Material existente, sem mudança de tema/tecnologia.
Introduz um `nav:` explícito organizado por fluxo temático do pipeline científico (visão
geral → protótipo → modelagem → identificação → controle → gêmeo digital → software →
referência de código). Páginas existentes são realocadas (não descartadas); páginas novas
são escritas a partir de fontes já existentes no repositório (monografia, notebook de
modelagem, código-fonte do firmware) — nenhum fato técnico é inventado.

**Tech Stack:** MkDocs 1.5.3+, mkdocs-material, mkdocstrings-python, MathJax (via
`pymdownx.arithmatex`, já configurado em `mkdocs.yml`), `pdftoppm` (Poppler) para conversão
de figuras PDF→PNG.

**Spec:** `docs_tcc/06_site_redesign/2026-09-13-documentacao-online-redesign-design.md`

## Global Constraints

- **Nomes de arquivo/pasta em ASCII minúsculo com hífen** (`prototipo`, não `Protótipo`) —
  evita URLs com `%C3%B3` etc. Títulos exibidos (`title:` no front-matter, texto do `nav:`)
  continuam acentuados normalmente.
- **Nenhum fato técnico, equação ou valor numérico pode ser inventado.** Toda afirmação
  técnica nova deve vir de uma fonte citável já existente no repositório (arquivo e, quando
  fizer sentido, linha). As equações e valores já verificados nesta sessão estão transcritos
  neste plano — use-os literalmente, não re-derive.
- **Preservar histórico do git**: mover arquivo existente usa `git mv`, nunca apagar+recriar.
- **Verificação de build**: `mkdocs build --strict` deve passar sem avisos ao final de cada
  tarefa. Comando exato (venv de teste já existe; recriar se não existir):
  ```bash
  test -x /tmp/mkdocs_venv/bin/mkdocs || {
    python3 -m venv /tmp/mkdocs_venv
    /tmp/mkdocs_venv/bin/pip install mkdocs mkdocs-material mkdocs-material-extensions \
      mkdocstrings mkdocstrings-python pymdown-extensions mkdocs-macros-plugin
  }
  cd /home/osfarias/workspace/workspace_mestrado/Projeto_Tcc_Oseias_Oficial
  /tmp/mkdocs_venv/bin/mkdocs build --strict --site-dir /tmp/_site_check
  ```
- **Equações em Markdown**: usar `$$ ... $$` (bloco) ou `$ ... $` (inline) — MathJax já
  processa via `pymdownx.arithmatex` + `docs/javascripts/mathjax.js`.
- **Figuras**: converter de PDF existente com `pdftoppm -png -r 150 <origem.pdf> <destino_sem_extensao>`
  (adiciona sufixo de página automaticamente, ex: `destino-1.png`), salvar em
  `docs/<secao>/img/`. Nunca gerar imagem nova do zero.
- **Commits pequenos**: um commit por tarefa, branch `site-redesign-plano` (já criada e com o
  spec commitado).

---

## Mapeamento de arquivos (visão geral de todas as tarefas)

| Ação | Caminho atual | Caminho novo |
| --- | --- | --- |
| mover | `docs/Componentes do Aeropêndulo/aeropendulo_doc.md` | `docs/prototipo/index.md` |
| mover | `docs/Componentes do Aeropêndulo/gemeo_digital.md` | `docs/gemeo-digital/index.md` |
| mover | `docs/Componentes do Aeropêndulo/interface_grafica_usuario.md` | `docs/software/interface-grafica.md` |
| mover | `docs/Módulo Firmware/aeropendulo_doc.md` | `docs/software/firmware.md` |
| mover | `docs/Módulos Gêmeo Digital/animacao_aeropendulo_reference.md` | `docs/referencia/animacao-aeropendulo.md` |
| mover | `docs/Módulos Gêmeo Digital/graficos_aeropendulo_reference.md` | `docs/referencia/graficos-aeropendulo.md` |
| mover | `docs/Módulos Gêmeo Digital/interface_interativa_reference.md` | `docs/referencia/interface-interativa.md` |
| mover | `docs/1 Instalações e Configurações/1.1 Instalacao_python/index.md` | `docs/software/instalacao/python/index.md` |
| mover | `docs/1 Instalações e Configurações/1.1 Instalacao_python/1.1 Instalacao_python_ubuntu.md` | `docs/software/instalacao/python/ubuntu.md` |
| mover | `docs/1 Instalações e Configurações/1.1 Instalacao_python/1.2 Instalacao_python_windows.md` | `docs/software/instalacao/python/windows.md` |
| mover | `docs/1 Instalações e Configurações/1.1 Instalacao_python/1.3 Instalacao_python_macos.md` | `docs/software/instalacao/python/macos.md` |
| mover | `docs/1 Instalações e Configurações/1.2 Instalacao_dependencias_python/1.2 Instalacao_dependencias_python.md` | `docs/software/instalacao/dependencias.md` |
| reescrever | `docs/index.md` | (mesmo lugar, conteúdo novo) |
| criar | — | `docs/visao-geral/index.md` |
| criar | — | `docs/visao-geral/arquitetura.md` |
| criar | — | `docs/modelagem/index.md` |
| criar | — | `docs/identificacao/excitacao.md` |
| criar | — | `docs/identificacao/estimacao.md` |
| criar | — | `docs/identificacao/validacao.md` |
| criar | — | `docs/controle/pid.md` |
| criar | — | `docs/controle/resultados.md` |
| modificar | `mkdocs.yml` | adiciona `nav:` explícito |

---

### Task 1: Nav explícito + migração mecânica das páginas existentes

**Files:**
- Modify: `mkdocs.yml`
- Move (via `git mv`): as 12 linhas "mover" da tabela acima
- Modify: `docs/index.md` (reescrita)
- Test: build check (Global Constraints)

**Interfaces:**
- Produces: a estrutura de pastas/arquivos final que as Tasks 2–9 vão popular
  (`docs/visao-geral/`, `docs/modelagem/`, `docs/identificacao/`, `docs/controle/` ainda
  não existem até esta tarefa criar as pastas vazias-mas-referenciadas no nav; os arquivos
  dentro delas são criados nas tasks seguintes — até lá, o nav vai referenciar arquivos que
  não existem, o que é esperado e temporário: adicione um placeholder mínimo em cada um
  deles nesta task, ver Step 4).

- [ ] **Step 1: Mover as páginas existentes preservando histórico**

```bash
cd /home/osfarias/workspace/workspace_mestrado/Projeto_Tcc_Oseias_Oficial
mkdir -p docs/prototipo docs/gemeo-digital docs/software/instalacao/python docs/referencia

git mv "docs/Componentes do Aeropêndulo/aeropendulo_doc.md" docs/prototipo/index.md
git mv "docs/Componentes do Aeropêndulo/gemeo_digital.md" docs/gemeo-digital/index.md
git mv "docs/Componentes do Aeropêndulo/interface_grafica_usuario.md" docs/software/interface-grafica.md
rmdir "docs/Componentes do Aeropêndulo"

git mv "docs/Módulo Firmware/aeropendulo_doc.md" docs/software/firmware.md
rmdir "docs/Módulo Firmware"

git mv "docs/Módulos Gêmeo Digital/animacao_aeropendulo_reference.md" docs/referencia/animacao-aeropendulo.md
git mv "docs/Módulos Gêmeo Digital/graficos_aeropendulo_reference.md" docs/referencia/graficos-aeropendulo.md
git mv "docs/Módulos Gêmeo Digital/interface_interativa_reference.md" docs/referencia/interface-interativa.md
rmdir "docs/Módulos Gêmeo Digital"

git mv "docs/1 Instalações e Configurações/1.1 Instalacao_python/index.md" docs/software/instalacao/python/index.md
git mv "docs/1 Instalações e Configurações/1.1 Instalacao_python/1.1 Instalacao_python_ubuntu.md" docs/software/instalacao/python/ubuntu.md
git mv "docs/1 Instalações e Configurações/1.1 Instalacao_python/1.2 Instalacao_python_windows.md" docs/software/instalacao/python/windows.md
git mv "docs/1 Instalações e Configurações/1.1 Instalacao_python/1.3 Instalacao_python_macos.md" docs/software/instalacao/python/macos.md
rmdir "docs/1 Instalações e Configurações/1.1 Instalacao_python"

git mv "docs/1 Instalações e Configurações/1.2 Instalacao_dependencias_python/1.2 Instalacao_dependencias_python.md" docs/software/instalacao/dependencias.md
rmdir "docs/1 Instalações e Configurações/1.2 Instalacao_dependencias_python"
rmdir "docs/1 Instalações e Configurações"
```

- [ ] **Step 2: Conferir que nenhum link interno ficou quebrado pelos novos caminhos**

```bash
grep -rn "Componentes do\|Módulo Firmware\|Módulos Gêmeo Digital\|1 Instalações" docs/ mkdocs.yml
```

Esperado: nenhum resultado (fora deste próprio grep). Se aparecer algo, corrija o link para
o novo caminho antes de continuar.

- [ ] **Step 3: Criar placeholders mínimos para as páginas que as Tasks 2–9 vão preencher**

Cada arquivo abaixo recebe só um front-matter + um `# Título` temporário (isso é
INTENCIONAL nesta task — o conteúdo real vem nas tasks seguintes, cada uma delas substitui
o placeholder inteiro):

```bash
mkdir -p docs/visao-geral docs/modelagem docs/identificacao docs/controle

cat > docs/visao-geral/index.md <<'EOF'
---
title: O que é o Laboratório Virtual
---

# O que é o Laboratório Virtual

_Conteúdo desta página é escrito na Task 2 deste plano._
EOF

cat > docs/visao-geral/arquitetura.md <<'EOF'
---
title: Arquitetura do Sistema
---

# Arquitetura do Sistema

_Conteúdo desta página é escrito na Task 3 deste plano._
EOF

cat > docs/modelagem/index.md <<'EOF'
---
title: Modelagem Matemática
---

# Modelagem Matemática

_Conteúdo desta página é escrito na Task 4 deste plano._
EOF

cat > docs/identificacao/excitacao.md <<'EOF'
---
title: Excitação e Aquisição
---

# Excitação e Aquisição

_Conteúdo desta página é escrito na Task 5 deste plano._
EOF

cat > docs/identificacao/estimacao.md <<'EOF'
---
title: Estimação por Mínimos Quadrados
---

# Estimação por Mínimos Quadrados

_Conteúdo desta página é escrito na Task 6 deste plano._
EOF

cat > docs/identificacao/validacao.md <<'EOF'
---
title: Validação do Modelo
---

# Validação do Modelo

_Conteúdo desta página é escrito na Task 7 deste plano._
EOF

cat > docs/controle/pid.md <<'EOF'
---
title: Controlador PID
---

# Controlador PID

_Conteúdo desta página é escrito na Task 8 deste plano._
EOF

cat > docs/controle/resultados.md <<'EOF'
---
title: Resultados em Malha Fechada
---

# Resultados em Malha Fechada

_Conteúdo desta página é escrito na Task 9 deste plano._
EOF
```

- [ ] **Step 4: Substituir o `nav:` em `mkdocs.yml`**

Adicionar logo após a linha `copyright:` (ou em qualquer ponto de nível raiz do YAML) o
seguinte bloco, criando a chave `nav:` (ela não existe hoje no arquivo):

```yaml
nav:
  - Início: index.md
  - Visão Geral:
      - O que é o Laboratório Virtual: visao-geral/index.md
      - Arquitetura do sistema: visao-geral/arquitetura.md
  - Protótipo: prototipo/index.md
  - Modelagem Matemática: modelagem/index.md
  - Identificação de Sistemas:
      - Excitação e aquisição (PRBS): identificacao/excitacao.md
      - Estimação por mínimos quadrados: identificacao/estimacao.md
      - Validação do modelo: identificacao/validacao.md
  - Projeto de Controle:
      - Controlador PID: controle/pid.md
      - Resultados em malha fechada: controle/resultados.md
  - Gêmeo Digital: gemeo-digital/index.md
  - Software:
      - Interface Gráfica: software/interface-grafica.md
      - Firmware: software/firmware.md
      - Instalação:
          - Visão geral: software/instalacao/python/index.md
          - Python (Ubuntu): software/instalacao/python/ubuntu.md
          - Python (Windows): software/instalacao/python/windows.md
          - Python (macOS): software/instalacao/python/macos.md
          - Dependências: software/instalacao/dependencias.md
  - Referência de Código:
      - animacao_aeropendulo: referencia/animacao-aeropendulo.md
      - graficos_aeropendulo: referencia/graficos-aeropendulo.md
      - interface_interativa: referencia/interface-interativa.md
```

- [ ] **Step 5: Reescrever `docs/index.md`**

Ler o `docs/index.md` atual (guarda o conteúdo de "Demonstração", "Membros Atuais" e o
vídeo). Reescrever com esta estrutura:

```markdown
---
hide:
    - toc
---

<p align="center">
  <img src="logo.svg" alt="Laboratório Virtual" width="90">
</p>

<h1 align="center">Laboratório Virtual</h1>

<p align="center"><i>Protótipo, gêmeo digital e identificação de sistemas aplicados a um
aeropêndulo — um mapa completo do desenvolvimento, da física ao código.</i></p>

## Comece por aqui

- **Quer uma visão rápida?** → [O que é o Laboratório Virtual](visao-geral/index.md)
- **Quer aprender o processo científico?** → [Modelagem Matemática](modelagem/index.md) →
  [Identificação de Sistemas](identificacao/excitacao.md) →
  [Projeto de Controle](controle/pid.md)
- **Quer reproduzir ou modificar o hardware/software?** →
  [Protótipo](prototipo/index.md) e [Software](software/interface-grafica.md)

## Sobre o projeto

<!-- Mover para cá o parágrafo original "Esse projeto surgiu do desenvolvimento de um
trabalho de conclusão de curso..." e a seção "Membros Atuais" com a tabela de fotos,
exatamente como estavam no docs/index.md original. -->

## Demonstração

<!-- Mover para cá o iframe do Vimeo que já existia no docs/index.md original. -->
```

Preencha os dois comentários HTML com o conteúdo real que já existia no `docs/index.md`
original (não invente texto novo para essas duas seções — é uma realocação, igual às
páginas movidas).

- [ ] **Step 6: Rodar o build de verificação**

Use o comando exato em Global Constraints. Esperado: `mkdocs build --strict` conclui sem
nenhum WARNING nem ERROR. Se algum link quebrado aparecer, corrija antes de prosseguir —
não ignore o aviso.

- [ ] **Step 7: Commit**

```bash
cd /home/osfarias/workspace/workspace_mestrado/Projeto_Tcc_Oseias_Oficial
git add -A -- docs/ mkdocs.yml
git commit -m "docs(site): nav explícito por fluxo temático + migração das páginas existentes

Reorganiza a navegação do site em torno do pipeline real (visão geral,
protótipo, modelagem, identificação, controle, gêmeo digital,
software, referência) em vez da lista de pastas de software que havia
antes. Nenhuma página é descartada -- todas movidas para o novo lugar.
Páginas novas (visão geral, arquitetura, modelagem, identificação,
controle) entram como placeholder nesta task e são preenchidas nas
tasks seguintes deste plano."
```

---

### Task 2: Página "O que é o Laboratório Virtual" (Visão Geral)

**Files:**
- Modify: `docs/visao-geral/index.md` (substitui o placeholder da Task 1)
- Test: build check

**Interfaces:**
- Consumes: nenhuma dependência de outra task de conteúdo.
- Produces: página de abertura que as próximas seções ("Comece por aqui" em `docs/index.md`)
  já linkam.

**Fontes a ler antes de escrever:**
- `README.md` (raiz do repo) — resumo, arquitetura em tabela, metodologia
- `revisao_tcc/Template_TCC_FEE/elementos_textuais/Cap_1_introducao.tex` — contexto e
  objetivos originais

- [ ] **Step 1: Escrever a página**

Estrutura obrigatória (headings exatos, conteúdo dentro de cada um é redação livre do
executor a partir das fontes acima — mas os FATOS abaixo, quando usados, são verbatim):

```markdown
---
title: O que é o Laboratório Virtual
---

# O que é o Laboratório Virtual

## O problema

(1-2 parágrafos: por que um aeropêndulo, o que ele é fisicamente -- haste articulada em um
pivô com motor CC + hélice na ponta, o empuxo da hélice eleva a haste a partir do repouso,
não linear, instável em malha aberta em parte da faixa de operação.)

## O que este projeto entrega

(Lista com as 4 frentes, mesma tabela do README.md: Protótipo, Firmware, Interface
Gráfica, Gêmeo Digital -- pode reaproveitar a tabela do README quase literalmente.)

## O fluxo completo

(1 parágrafo + um link explícito, em ordem, para cada seção do nav: Protótipo →
Modelagem Matemática → Identificação de Sistemas → Projeto de Controle → Gêmeo Digital →
Software. Use os links reais: `[Protótipo](../prototipo/index.md)`,
`[Modelagem Matemática](../modelagem/index.md)`, etc. -- caminhos relativos a partir de
`docs/visao-geral/index.md`.)

## Origem acadêmica

(1 parágrafo: TCC de Oséias Dias de Farias, UFPA Campus Tucuruí, Faculdade de Engenharia
Elétrica, orientação do Prof. Raphael Barros Teixeira, defendido 11/12/2023, publicado em
acesso aberto em https://bdm.ufpa.br/handle/prefix/6944.)
```

- [ ] **Step 2: Build check** (comando em Global Constraints)

- [ ] **Step 3: Commit**

```bash
git add docs/visao-geral/index.md
git commit -m "docs(site): escreve a página de Visão Geral"
```

---

### Task 3: Página "Arquitetura do Sistema"

**Files:**
- Modify: `docs/visao-geral/arquitetura.md`
- Create: `docs/visao-geral/img/` (figuras convertidas)
- Test: build check

**Fontes a ler:**
- `revisao_tcc/Template_TCC_FEE/Capitulos/3_hardware_softwares/3_5_ecossistema.tex`
- `revisao_tcc/Template_TCC_FEE/Capitulos/3_hardware_softwares/3_0_simulador_e_prototipo_do_Aeropendulo.tex`

**Figura a converter:**
```bash
cd /home/osfarias/workspace/workspace_mestrado/Projeto_Tcc_Oseias_Oficial
mkdir -p docs/visao-geral/img
pdftoppm -png -r 150 \
  "revisao_tcc/Template_TCC_FEE/Capitulos/3_hardware_softwares/3_figuras/diagrama_ecossistema.pdf" \
  docs/visao-geral/img/diagrama-ecossistema
```
(gera `docs/visao-geral/img/diagrama-ecossistema-1.png` — referencie esse nome exato na
página.)

- [ ] **Step 1: Converter a figura** (comando acima)

- [ ] **Step 2: Escrever a página**

```markdown
---
title: Arquitetura do Sistema
---

# Arquitetura do Sistema

O sistema é composto por quatro subsistemas que operam de forma integrada: protótipo
físico, firmware, interface gráfica e gêmeo digital.

![Diagrama do ecossistema do Aeropêndulo](img/diagrama-ecossistema-1.png)

## Como os dados fluem

(Descrever o ciclo: potenciômetro -> firmware -> serial -> interface gráfica -> gêmeo
digital, e o caminho de volta: interface gráfica -> serial -> firmware -> motor. Basear no
texto de 3_5_ecossistema.tex.)

## Por que essa divisão

(1 parágrafo explicando a separação de responsabilidades -- por que o controle roda no
firmware e não no PC, por que a interface e o gêmeo digital são processos Python
separados que se comunicam por classes compartilhadas, não por rede.)
```

- [ ] **Step 3: Build check**

- [ ] **Step 4: Commit**

```bash
git add docs/visao-geral/arquitetura.md docs/visao-geral/img/
git commit -m "docs(site): escreve a página de Arquitetura, com diagrama do ecossistema"
```

---

### Task 4: Página "Modelagem Matemática"

**Files:**
- Modify: `docs/modelagem/index.md`
- Create: `docs/modelagem/img/`
- Test: build check

**Fontes a ler:**
- `revisao_tcc/Template_TCC_FEE/Capitulos/2_aeropendulo/2_2_fundamentacao_teorica.tex`
- `revisao_tcc/Template_TCC_FEE/Capitulos/2_aeropendulo/2_3_modelagem_analitica.tex`
- `softwares_aeropendulo/simulador_aeropendulo/docs/Modelagem_matematica_do_aeropendulo.ipynb`

**Fatos/equações verbatim a usar (já verificados nesta sessão — não re-derivar):**

Parâmetros físicos do Aeropêndulo (tabela do notebook, célula 17):

| Parâmetro | Valor | Unidade |
| --- | --- | --- |
| $K_m$ | 0,0296 | — |
| $d$ | 0,03 | m |
| $J$ | 0,0106 | kg·m² |
| $m$ | 0,36 | kg |
| $g$ | 9,8 | m/s² |
| $c$ | 0,0076 | N·m·s/rad |

Modelo não linear (torque gerado pela hélice = torque resistivo):
$$
K_m V = J\ddot\theta + c\dot\theta + mgd\sin(\theta)
$$

Linearizado (pequenas variações em torno de $\theta=0$, $\sin\theta \approx \theta$):
$$
K_m V = J\ddot\theta + c\dot\theta + mgd\theta
$$

Função de transferência contínua (Laplace, depois substituir os parâmetros):
$$
\frac{\theta(s)}{V(s)} = \frac{K_m/J}{s^2 + (c/J)s + mgd/J}
$$

Numericamente, com os parâmetros da tabela:
$$
\frac{\theta(s)}{V(s)} = \frac{2{,}792}{s^2 + 0{,}717\,s + 9{,}985}
$$

Espaço de estados ($x_1=\theta$, $x_2=\dot\theta$):
$$
\begin{bmatrix}\dot x_1\\ \dot x_2\end{bmatrix} =
\begin{bmatrix}0 & 1\\ -mgd/J & -c/J\end{bmatrix}
\begin{bmatrix}x_1\\ x_2\end{bmatrix} +
\begin{bmatrix}0\\ K_m/J\end{bmatrix} u
$$

**Figuras a converter:**
```bash
cd /home/osfarias/workspace/workspace_mestrado/Projeto_Tcc_Oseias_Oficial
mkdir -p docs/modelagem/img
pdftoppm -png -r 150 "revisao_tcc/Template_TCC_FEE/Capitulos/2_aeropendulo/4_figuras/desenho_aeropendulo.pdf" docs/modelagem/img/desenho-aeropendulo
pdftoppm -png -r 150 "revisao_tcc/Template_TCC_FEE/Capitulos/2_aeropendulo/4_figuras/diagrama_motor_cc.pdf" docs/modelagem/img/diagrama-motor-cc
pdftoppm -png -r 150 "revisao_tcc/Template_TCC_FEE/Capitulos/2_aeropendulo/4_figuras/subsistemas_aeropendulo.pdf" docs/modelagem/img/subsistemas-aeropendulo
```

- [ ] **Step 1: Converter as 3 figuras** (comandos acima)

- [ ] **Step 2: Escrever a página**

```markdown
---
title: Modelagem Matemática
---

# Modelagem Matemática

![Desenho do Aeropêndulo com as variáveis do modelo](img/desenho-aeropendulo-1.png)

## Como a física vira equação

(Explicar o balanço de torques: torque do motor via hélice = torque inercial + torque de
amortecimento viscoso + torque gravitacional restaurador. Usar a Equação 1 (fórmula acima).
Citar a Figura de subsistemas_aeropendulo para mostrar motor CC + braço como dois
subsistemas.)

![Subsistemas: motor CC e braço](img/subsistemas-aeropendulo-1.png)

## Linearização

(Explicar por que linearizar: técnicas clássicas de controle -- PID, alocação de polos --
assumem sistema linear. sin(theta)≈theta vale para pequenas variações em torno do ponto de
operação. Mostrar a Equação 2.)

## Da equação diferencial à função de transferência

(Explicar a transformada de Laplace levando de uma EDO de 2ª ordem à função de
transferência. Mostrar a Equação 3 (forma simbólica) e a Equação 4 (forma numérica com os
parâmetros da tabela).)

## Parâmetros físicos

(Inserir a tabela de parâmetros acima, formatada como tabela Markdown.)

## Representação em espaço de estados

(Mostrar a Equação 5. Explicar por que essa forma é usada depois no projeto de controle:
serve tanto para simulação numérica -- `scipy`/`python-control` -- quanto para projeto de
controladores modernos.)

## Onde essa dedução aparece no código

O modelo linearizado acima é implementado e simulado em
[`Modelagem_matematica_do_aeropendulo.ipynb`](https://github.com/Oseiasdfarias/lab-virtual/blob/main/softwares_aeropendulo/simulador_aeropendulo/docs/Modelagem_matematica_do_aeropendulo.ipynb),
usando as bibliotecas NumPy e Python-Control. A [identificação de sistemas](../identificacao/excitacao.md)
usa uma abordagem diferente -- ajustar o modelo a dados reais em vez de derivá-lo
puramente da física -- e chega a um modelo mais preciso, usado de fato no controlador.
```

- [ ] **Step 3: Build check**

- [ ] **Step 4: Commit**

```bash
git add docs/modelagem/
git commit -m "docs(site): escreve a página de Modelagem Matemática, com dedução e figuras"
```

---

### Task 5: Página "Excitação e Aquisição" (Identificação de Sistemas, parte 1)

**Files:**
- Modify: `docs/identificacao/excitacao.md`
- Create: `docs/identificacao/img/`
- Test: build check

**Fontes a ler:**
- `revisao_tcc/Template_TCC_FEE/Capitulos/3_hardware_softwares/3_0_0_dev_software.tex`
- Início do Cap. 3 (`Cap_3_Resultados_e_Discussoes.tex`) — seção de aquisição/PRBS, antes
  da parte de mínimos quadrados (linhas anteriores à 150 aproximadamente)
- `docs_tcc/02_software/dados_ensaios.md` (mapeamento das 7 colunas do CSV, já confirmado)

**Fatos a usar:**
- Sinal de excitação: PRBS (Pseudo-Random Binary Sequence), aplicado com offset para manter
  o sistema operando em torno de um ponto de trabalho (não em `theta=0`, que seria a
  posição de repouso sem sustentação).
- Firmware gera o PRBS via `OndaPrbs` (`firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos/`),
  parametrizado por frequência máxima, amplitude e offset.
- Dados salvos em CSV pela interface gráfica — 7 colunas, mapeamento exato já documentado
  em `docs_tcc/02_software/dados_ensaios.md` (referencie a tabela de lá, reproduza as 7
  linhas).
- Divisão em dados de treino/teste antes de estimar o modelo (mencionado no Cap. 3: "com
  isso obtém-se os dados de saída da simulação, esse dado pode ser comparado com a saída
  do sistema real").

**Figura a converter:**
```bash
cd /home/osfarias/workspace/workspace_mestrado/Projeto_Tcc_Oseias_Oficial
mkdir -p docs/identificacao/img
pdftoppm -png -r 150 "revisao_tcc/Template_TCC_FEE/Capitulos/3_1_resultados_discurcao/3_figuras/sinal_prbs_entrada_saida.pdf" docs/identificacao/img/prbs-entrada-saida
pdftoppm -png -r 150 "revisao_tcc/Template_TCC_FEE/Capitulos/3_1_resultados_discurcao/3_figuras/dados_traino_teste.pdf" docs/identificacao/img/dados-treino-teste
```

- [ ] **Step 1: Converter as 2 figuras**

- [ ] **Step 2: Escrever a página**

```markdown
---
title: Excitação e Aquisição
---

# Excitação e Aquisição

Identificação de sistemas obtém um modelo matemático a partir de **dados observados**, em
vez de deduzi-lo puramente da física (comparar com a [Modelagem Matemática](../modelagem/index.md)).
O primeiro passo é excitar o sistema real com um sinal conhecido e registrar como ele
responde.

## Por que PRBS

(Explicar o que é um sinal PRBS e por que é bom para identificação -- excita uma faixa
ampla de frequências numa única coleta, ao contrário de um degrau único ou senoide de
frequência fixa.)

![Sinal PRBS aplicado e resposta do sistema](img/prbs-entrada-saida-1.png)

## Por que o offset

(Explicar por que o PRBS tem um offset de tensão/ângulo -- o Aeropêndulo em repouso não
sustenta a haste no ar; o offset mantém o sistema operando em torno de um ponto de
equilíbrio onde a linearização da Modelagem Matemática é válida.)

## Como os dados chegam ao computador

(Resumo de 1 parágrafo do caminho firmware -> serial -> interface gráfica -> CSV, com link
para [Interface Gráfica](../software/interface-grafica.md) e [Firmware](../software/firmware.md)
para quem quiser o detalhe de implementação.)

## Formato dos dados coletados

(Reproduzir a tabela de 7 colunas de `docs_tcc/02_software/dados_ensaios.md` aqui, com uma
frase indicando que os arquivos ficam em `softwares_aeropendulo/src_interface/dados_de_ensaio/`.)

## Separação treino/teste

![Divisão dos dados em treino e teste](img/dados-treino-teste-1.png)

(1 parágrafo: por que dividir -- para validar o modelo em dados que ele não viu durante o
ajuste, ver [Validação do Modelo](validacao.md).)
```

- [ ] **Step 3: Build check**

- [ ] **Step 4: Commit**

```bash
git add docs/identificacao/excitacao.md docs/identificacao/img/
git commit -m "docs(site): escreve a página de Excitação e Aquisição (identificação de sistemas)"
```

---

### Task 6: Página "Estimação por Mínimos Quadrados" (Identificação de Sistemas, parte 2)

**Files:**
- Modify: `docs/identificacao/estimacao.md`
- Test: build check (sem figura nova nesta task — reaproveita o contexto textual do Cap. 3)

**Fontes a ler:**
- `revisao_tcc/Template_TCC_FEE/Capitulos/Cap_3_Resultados_e_Discussoes.tex`, a partir da
  linha ~150 até a linha ~250 (a seção que você mesmo corrigiu nesta sessão — contém a
  estrutura ARX, o código dos regressores e o método dos mínimos quadrados).

**Fatos/equações verbatim a usar:**

Primeira tentativa, modelo de 2ª ordem (mostrar como um "não deu certo" pedagogicamente
honesto — a monografia relata que esse grau não aproxima bem a dinâmica real):
$$
Hz = \frac{-0{,}002602z^2+0{,}004962z+0{,}0163}{z^2-1{,}176z+0{,}1849}
$$

Estrutura geral ARX de 10ª ordem que de fato funcionou (equação 50 da monografia, já
corrigida nesta sessão):
$$
H(z) = \frac{b_1z^{-1}+b_2z^{-2}+b_3z^{-3}+b_4z^{-4}}{1+a_1z^{-1}+a_2z^{-2}+a_3z^{-3}+a_4z^{-4}+a_5z^{-5}+a_6z^{-6}+a_7z^{-7}+a_8z^{-8}+a_9z^{-9}+a_{10}z^{-10}}
$$

Método: regressores de saída ($y[k-1]..y[k-10]$) e de entrada ($u[k]..u[k-3]$) montados
numa matriz $M$; coeficientes obtidos por
$\theta = (M^TM)^{-1}M^Ty$ (mínimos quadrados ordinários, sem regularização).

Resultado final, com os valores numéricos (equação 51 da monografia, já corrigida):
$$
Hz = \frac{-0{,}0029z^3+0{,}0023z^2+0{,}0016z+0{,}0097}{z^{10}-0{,}9z^9-0{,}3z^8-0{,}014z^7+0{,}13z^6+0{,}15z^5+0{,}012z^4-0{,}05z^3-0{,}12z^2-0{,}02z+0{,}15}
$$

Período de amostragem: $dt = 0{,}02$ s.

- [ ] **Step 1: Escrever a página**

```markdown
---
title: Estimação por Mínimos Quadrados
---

# Estimação por Mínimos Quadrados

Com os dados de [excitação e aquisição](excitacao.md) em mãos, o próximo passo é ajustar
os parâmetros de um modelo discreto que reproduza a relação entrada/saída observada.

## Por que um modelo discreto (não o modelo analítico)

(Explicar: o modelo da Modelagem Matemática é contínuo e linearizado -- uma aproximação.
O modelo identificado é discreto (natural, já que os dados são amostrados a `dt` fixo) e
não depende de conhecer os parâmetros físicos exatos -- ele "aprende" a dinâmica direto
dos dados, incluindo efeitos não modelados analiticamente como atrito seco, folga mecânica
etc.)

## Primeira tentativa: modelo de 2ª ordem

Mostre a equação do modelo de 2ª ordem acima. Explique: mesma ordem do modelo analítico
seria o candidato natural, mas na prática não aproximou bem a dinâmica real (ver
[Validação do Modelo](validacao.md) para o motivo qualitativo) -- o que motivou tentar uma
ordem maior.

## Estrutura ARX de 10ª ordem

Mostre a equação da estrutura geral (H(z) simbólico). Explique a notação: 4 coeficientes
no numerador (`b`), 10 no denominador (`a`), $z^{-1}$ representa um atraso de uma amostra.

## Montando o problema de mínimos quadrados

(Explicar em prosa a lógica de regressão: cada linha da matriz M contém amostras passadas
de y e u; o vetor theta que minimiza o erro quadrático entre a predição e o y real
observado é dado pela fórmula normal `(M^T M)^-1 M^T y`. Não precisa reproduzir o código
Python linha a linha -- isso já está na monografia; a página aqui é sobre o raciocínio.)

## Resultado

Mostre a equação numérica final (Hz de 10ª ordem) e a nota do período de amostragem
($dt=0,02$s). Um parágrafo: esses 14 números (4 do numerador + 10 do denominador) são o
modelo que de fato foi usado para [projetar o controlador](../controle/pid.md).
```

- [ ] **Step 2: Build check**

- [ ] **Step 3: Commit**

```bash
git add docs/identificacao/estimacao.md
git commit -m "docs(site): escreve a página de Estimação por Mínimos Quadrados"
```

---

### Task 7: Página "Validação do Modelo" (Identificação de Sistemas, parte 3)

**Files:**
- Modify: `docs/identificacao/validacao.md`
- Test: build check

**Fontes a ler:**
- `revisao_tcc/Template_TCC_FEE/Capitulos/Cap_3_Resultados_e_Discussoes.tex`, a seção de
  validação logo após cada equação de função de transferência (as duas figuras "Validação
  do modelo de segundo grau"/"...décima ordem" e o texto ao redor).

**Figuras a converter:**
```bash
cd /home/osfarias/workspace/workspace_mestrado/Projeto_Tcc_Oseias_Oficial
pdftoppm -png -r 150 "revisao_tcc/Template_TCC_FEE/Capitulos/3_1_resultados_discurcao/3_figuras/validacao_model_2grau.pdf" docs/identificacao/img/validacao-2grau
pdftoppm -png -r 150 "revisao_tcc/Template_TCC_FEE/Capitulos/3_1_resultados_discurcao/3_figuras/validacao_model_10grau.pdf" docs/identificacao/img/validacao-10grau
```

**Fato importante a preservar (limitação real, reconhecida na própria monografia — não
suavizar isso):** a validação é qualitativa/visual (comparação gráfica entre saída real e
simulada), sem métrica quantitativa de erro (RMSE/EQM) calculada no trabalho original.

- [ ] **Step 1: Converter as 2 figuras**

- [ ] **Step 2: Escrever a página**

```markdown
---
title: Validação do Modelo
---

# Validação do Modelo

Depois de estimar os coeficientes (ver [Estimação por Mínimos Quadrados](estimacao.md)), é
preciso confirmar que o modelo reproduz a dinâmica real -- inclusive em dados que **não**
foram usados para ajustá-lo.

## Modelo de 2ª ordem: insuficiente

![Validação do modelo de segundo grau](img/validacao-2grau-1.png)

(1-2 parágrafos: descrever o que a figura mostra -- a saída simulada não acompanha bem a
saída real. Essa é a evidência visual que motivou subir a ordem do modelo.)

## Modelo de 10ª ordem: aceitável

![Validação do modelo de décima ordem](img/validacao-10grau-1.png)

(1-2 parágrafos: descrever que a saída simulada acompanha razoavelmente a saída real desta
vez.)

## Limitação reconhecida

Esta validação é **qualitativa** (comparação visual dos gráficos), sem uma métrica
numérica de erro (RMSE/EQM) calculada no trabalho original. Isso é uma limitação conhecida
-- ver [pendências de documentação](https://github.com/Oseiasdfarias/lab-virtual/blob/main/docs_tcc/05_plano_publicacoes/pendencias_documentacao.md)
no repositório para o item em aberto sobre validação quantitativa.
```

- [ ] **Step 3: Build check**

- [ ] **Step 4: Commit**

```bash
git add docs/identificacao/validacao.md docs/identificacao/img/
git commit -m "docs(site): escreve a página de Validação do Modelo"
```

---

### Task 8: Página "Controlador PID"

**Files:**
- Modify: `docs/controle/pid.md`
- Create: `docs/controle/img/`
- Test: build check

**Fontes a ler:**
- `softwares_aeropendulo/firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos/lib/controlador_pid/src/controlador_pid.cpp`
  (já corrigido nesta sessão — leia a versão atual, pós-fix)
- `softwares_aeropendulo/firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos/src/main.cpp`
  (valores default de Kp/Ki/Kd)

**Fatos/equações verbatim a usar:**

Implementação real no firmware (após o fix desta sessão):
$$
P = K_p \cdot e[k] \qquad
I \mathrel{+}= K_i \cdot e[k] \cdot T_s \qquad
D = K_d \cdot \frac{\theta[k-1] - \theta[k]}{T_s}
$$
$$
u[k] = P + I + D
$$

Onde $e[k]$ é o erro (referência − ângulo medido), $\theta[k]$ o ângulo medido na amostra
atual, $T_s=0,02$s o período de amostragem. A derivada é sobre a **medida** ($\theta$), não
sobre o erro — isso evita o "chute derivativo" (*derivative kick*) quando a referência muda
de repente.

Ganhos no firmware (`main.cpp`, linha `PID mypid(0.02, 0.055, 0.35);`) — **fixos em tempo
de compilação**, não recebidos por serial: $K_p=0,02$, $K_i=0,055$, $K_d=0,35$. Verificado
lendo `ler_dados_serial()` em `ler_escrever_serial.cpp`: os únicos parâmetros que a
interface gráfica envia ao firmware são amplitude, frequência, offset, forma de onda de
referência, malha aberta/fechada e o comando de executar — nenhum ganho de PID.

- [ ] **Step 1: Escrever a página**

```markdown
---
title: Controlador PID
---

# Controlador PID

Com o [modelo identificado](../identificacao/validacao.md) validado, o próximo passo é
projetar um controlador que leve o ângulo do Aeropêndulo até a referência desejada e o
mantenha lá, rejeitando perturbações.

## Por que PID

(1 parágrafo: PID é a escolha natural para essa planta -- proporcional reage ao erro
atual, integral elimina erro em regime permanente, derivativo antecipa a tendência e reduz
oscilação. Rodar em um microcontrolador de baixo custo com atualização a cada 20ms é
barato computacionalmente.)

## Implementação no firmware

Mostre as equações acima (P, I, D, u[k]). Explique o detalhe importante: a derivada usa a
diferença de **ângulo medido** entre duas amostras, não a diferença do erro -- porque
derivar o erro amplificaria mudanças bruscas de referência (um "degrau" na referência viraria
um pico artificial no termo derivativo).

## Ganhos

(Tabela com Kp=0,02, Ki=0,055, Kd=0,35 -- os valores fixos no firmware. Uma frase,
importante não inverter isso: esses ganhos são fixos em tempo de compilação
(`PID mypid(0.02, 0.055, 0.35);` em `main.cpp`) -- mudar um ganho exige recompilar e
regravar o microcontrolador. A [Interface Gráfica](../software/interface-grafica.md)
configura outros parâmetros em tempo real -- amplitude, frequência, offset, forma de
onda, malha aberta/fechada -- mas não os ganhos do PID.)

## Onde está o código

O controlador está implementado em
[`controlador_pid.cpp`](https://github.com/Oseiasdfarias/lab-virtual/blob/main/softwares_aeropendulo/firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos/lib/controlador_pid/src/controlador_pid.cpp)
e é chamado a cada iteração do loop principal do [firmware](../software/firmware.md).
```

- [ ] **Step 2: Build check**

- [ ] **Step 3: Commit**

```bash
git add docs/controle/pid.md
git commit -m "docs(site): escreve a página de Controlador PID"
```

---

### Task 9: Página "Resultados em Malha Fechada"

**Files:**
- Modify: `docs/controle/resultados.md`
- Create: `docs/controle/img/`
- Test: build check

**Fontes a ler:**
- Final de `revisao_tcc/Template_TCC_FEE/Capitulos/Cap_3_Resultados_e_Discussoes.tex`
  (seção após a validação do modelo, sobre o controlador em malha fechada)
- `revisao_tcc/Template_TCC_FEE/Capitulos/Cap_4_ Conclusao.tex` (limitações reconhecidas)

**Figura a converter:**
```bash
cd /home/osfarias/workspace/workspace_mestrado/Projeto_Tcc_Oseias_Oficial
pdftoppm -png -r 150 "revisao_tcc/Template_TCC_FEE/Capitulos/3_1_resultados_discurcao/3_figuras/estrutura_pid.pdf" docs/controle/img/estrutura-pid
```

**Fato a preservar (mesma limitação da Task 7, não suavizar):** avaliação em malha fechada
também é qualitativa/visual, sem métricas de tempo de acomodação/sobressinal/erro em
regime calculadas explicitamente no trabalho original.

- [ ] **Step 1: Converter a figura**

- [ ] **Step 2: Escrever a página**

```markdown
---
title: Resultados em Malha Fechada
---

# Resultados em Malha Fechada

![Estrutura do controlador PID em malha fechada](img/estrutura-pid-1.png)

## O que foi testado

(Resumo do ensaio em malha fechada: referência aplicada -- degrau ou onda -- e resposta do
ângulo real do Aeropêndulo, comparando com o comportamento esperado.)

## O que funcionou

(1 parágrafo, honesto e específico: o sistema converge para a referência, erro em regime
tende a zero graças ao termo integral -- consistente com o que a teoria de controle prevê
para um PID bem ajustado.)

## Limitações reconhecidas

A avaliação em malha fechada também foi qualitativa (inspeção visual dos gráficos), sem
métricas numéricas como tempo de acomodação, sobressinal ou erro em regime permanente
calculadas explicitamente. Isso, junto com a validação quantitativa do modelo (ver
[Validação do Modelo](../identificacao/validacao.md)), é a lacuna mais importante para
quem quiser transformar este trabalho em um artigo científico -- os dados brutos dos
ensaios já existem (`softwares_aeropendulo/src_interface/dados_de_ensaio/`), falta somente
processá-los.

## Trabalhos futuros sugeridos

(1 parágrafo com o que o Cap. 4 da monografia sugere como próximos passos.)
```

- [ ] **Step 3: Build check**

- [ ] **Step 4: Commit**

```bash
git add docs/controle/resultados.md docs/controle/img/
git commit -m "docs(site): escreve a página de Resultados em Malha Fechada"
```

---

### Task 10: Navegação cruzada e verificação final

**Files:**
- Modify: várias páginas criadas nas Tasks 2–9 (adicionar links "Ver também")
- Test: build check completo + inspeção visual de 2 páginas no navegador

**Interfaces:**
- Consumes: todas as páginas das Tasks 1–9 devem existir com conteúdo real (não
  placeholder) antes de começar esta task.

- [ ] **Step 1: Adicionar seção "Ver também" no final de cada página nova**

Para cada uma das 8 páginas de conteúdo novo (visão geral, arquitetura, modelagem, 3x
identificação, 2x controle), adicionar ao final um bloco curto linkando para a página
anterior e a próxima no fluxo lógico do pipeline. Exemplo para `docs/modelagem/index.md`:

```markdown
---

**Ver também:** [← Arquitetura do Sistema](../visao-geral/arquitetura.md) ·
[Identificação de Sistemas →](../identificacao/excitacao.md)
```

Siga a ordem do pipeline definida no `nav:` (Task 1) para decidir qual é "anterior" e
"próxima" de cada página.

- [ ] **Step 2: Build check completo**

Comando de Global Constraints. Esperado: zero avisos.

- [ ] **Step 3: Verificação visual**

```bash
pkill -f "mkdocs serve" 2>/dev/null
cd /home/osfarias/workspace/workspace_mestrado/Projeto_Tcc_Oseias_Oficial
nohup /tmp/mkdocs_venv/bin/mkdocs serve -a 127.0.0.1:8123 > /tmp/mkdocs_serve.log 2>&1 &
sleep 2
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8123/
```

Abrir `http://127.0.0.1:8123/modelagem/` e `http://127.0.0.1:8123/identificacao/estimacao/`
no navegador (ou via screenshot com Playwright, como já foi feito em tasks anteriores desta
sessão) e conferir: equações renderizam via MathJax (não aparecem como texto `$$...$$`
literal), figuras carregam (não aparecem como link quebrado), navegação lateral mostra a
estrutura completa do `nav:`.

- [ ] **Step 4: Commit final**

```bash
git add -A -- docs/
git commit -m "docs(site): navegação cruzada entre as páginas do fluxo temático"
```

- [ ] **Step 5: Push da branch**

```bash
git push -u origin site-redesign-plano
```
