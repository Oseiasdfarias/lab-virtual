---
fonte: mkdocs.yml, docs/, overrides/, .github/workflows/docs.yml
gerado_em: 2026-09-12
atualizado_em: 2026-09-13
---

# Site de documentação publicado

Publicado em https://oseiasdfarias.github.io/lab-virtual/ (MkDocs Material, idioma pt-BR).
O deploy é automático: `.github/workflows/docs.yml` roda `mkdocs build --strict` em PRs e
publica na branch `gh-pages` a cada push na `main`. As versões das ferramentas ficam em
`requirements-docs.txt`.

## Estrutura (ordem do menu)

| Seção | Páginas | Conteúdo |
| --- | --- | --- |
| Início | `index.md` | Hero com aeropêndulo 3D (Three.js, modelo linearizado), números, diagrama interativo da arquitetura (D3), linha do tempo, vídeo e equipe |
| Visão Geral | `visao-geral/index.md`, `arquitetura.md` | O que é a plataforma; fluxo de dados e motivo da divisão firmware × computador |
| Protótipo | `prototipo/index.md` | Lista de materiais, estrutura, eletrônica, montagem, diagrama de comunicação, esquema elétrico e pinagem (com a divergência GPIO 2 × GPIO 12) |
| Modelagem Matemática | `modelagem/index.md` | Equação do braço, motor CC série, linearização, função de transferência, parâmetros e espaço de estados |
| Identificação de Sistemas | `excitacao.md`, `estimacao.md`, `validacao.md` | PRBS e formato dos CSVs; ARX por mínimos quadrados (com o aviso do atraso de 7 amostras na TF publicada); validação com NRMSE/RMSE |
| Projeto de Controle | `controle/pid.md`, `resultados.md` | PID discreto e ganhos (tentativa e erro); métricas de malha fechada dos ensaios gravados |
| Gêmeo Digital | `gemeo-digital/index.md` | VPython e integração com a interface |
| Software | `interface-grafica.md`, `firmware.md`, `instalacao/*` | Execução, bibliotecas, laço do firmware, protocolo serial, gravação; instalação com Poetry ou pip |
| Referência de Código | `referencia/*.md` | mkdocstrings das 7 classes usadas pelo `rungui.py`, agrupadas por gêmeo digital e interface |

## Personalização

- Tema: `docs/stylesheets/extra.css` (paleta monocromática da marca, IBM Plex Sans/Mono, botões
  anterior/próximo) e `home.css` (página Início).
- `overrides/partials/copyright.html`: footer com mapa de links e créditos;
  `overrides/.icons/lab/`: ícone e assinatura da marca usados inline.
- `docs/javascripts/home/` (3D e diagrama) e `docs/javascripts/vendor/` (Three.js 0.186 e D3 7.9,
  com procedência em `LEIAME.txt`), carregados só na página Início.
- Diagramas Mermaid em Visão Geral, Arquitetura, Firmware e Excitação.

## Pontos de atenção

- Os tutoriais de instalação do Python por sistema operacional (`instalacao/python/ubuntu.md`,
  `windows.md`, `macos.md`) ainda ensinam a instalar o Python 3.10.0 e não foram revisados.
- Só a variante `Esp32_ttgo_modulos` do firmware é documentada; as demais estão em
  [`../divida_tecnica.md`](../divida_tecnica.md).
