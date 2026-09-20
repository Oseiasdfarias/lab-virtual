# Changelog

Mudanças relevantes do Laboratório Virtual. O formato segue
[Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e as versões seguem
[Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.0.0] — ainda não publicada

Primeira versão organizada como projeto aberto, a partir do estado defendido na monografia.

### Adicionado

- Documentação online reorganizada como mapa do laboratório: visão geral, protótipo, modelagem,
  identificação, controle, gêmeo digital, software e referência de código (#3).
- Identidade visual da marca, diagramas, página Início com aeropêndulo 3D e diagrama interativo
  da arquitetura (#4, #7, #8).
- Métricas reproduzíveis por script: ajuste NRMSE/RMSE da identificação (#6) e sobressinal,
  tempos de subida e acomodação e erro em regime da malha fechada.
- Página do protótipo com lista de materiais, diagrama de comunicação, esquema elétrico e pinagem.
- Catálogo dos ensaios gravados em `softwares_aeropendulo/src_interface/dados_de_ensaio/`.
- Deploy automático da documentação e build estrito em PRs (#6); testes automatizados do
  pacote Python e dos scripts de análise.
- `LICENSE` (MIT), `CITATION.cff` e esta lista de mudanças.

### Alterado

- Dependências atualizadas; Python suportado passa a ser 3.10–3.11 (#6).
- README reescrito com foco na plataforma (#9, #10).
- Versões do pacote unificadas em 1.0.0.

### Corrigido

- Termo derivativo do PID e limitação do sinal de controle no firmware (#5). A correção ainda
  não foi validada no protótipo — ver `docs_tcc/divida_tecnica.md`.
- Afirmações da documentação sem base no código ou na monografia: ganhos do PID pela serial,
  gêmeo digital simulando a dinâmica, controlador projetado a partir do modelo, planta instável
  em malha aberta, formato dos CSVs (#6, #9).

### Removido

- Código morto (`main_aeropendulo.py`, `interface_interativa.py`) e cerca de 60 MB de arquivos
  duplicados (#5, #6).

## [0.5.0] — 2023

Versão desenvolvida e defendida no Trabalho de Conclusão de Curso (UFPA, 11/12/2023),
preservada na branch `tcc-estado-original`.
