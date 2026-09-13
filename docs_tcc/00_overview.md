---
fonte: síntese de todo docs_tcc/ + estrutura do repositório
gerado_em: 2026-09-12
---

# Visão geral do projeto

## O que é

TCC de Engenharia Elétrica (UFPA — Campus Universitário de Tucuruí), autor **Oséias Farias**, orientação de **Raphael Teixeira** (revisor identificado como "André" nos arquivos de revisão pode ser um segundo revisor/banca — checar).

Título no site publicado: *"Desenvolvimento de Protótipo e Gêmeo Digital como Ferramenta para um Laboratório Virtual com Foco em Modelagem e Controle de Sistemas Dinâmicos"*.
Subtítulo/tema no README: *"Identificação de Sistemas, Simulador Gráfico e Prototipagem de um Aeropêndulo para estudos de Projetos de Controle"*.

O projeto tem 4 frentes que se integram:

1. **Protótipo físico** — um aeropêndulo (braço com motor CC + hélice, ESP32/Arduino) para servir de planta real de testes de controle.
2. **Firmware** — roda no microcontrolador, faz leitura de sensores, controle PID em malha fechada e comunicação serial com o PC.
3. **Interface gráfica (PC)** — coleta dados via serial, plota sinais em tempo real, salva ensaios em CSV.
4. **Gêmeo digital / simulador** — modelo matemático em Python que reproduz a dinâmica do aeropêndulo (animação + gráficos), usado tanto para projeto de controlador quanto para fins didáticos.

## Onde está cada coisa (mapa rápido)

| Área | Pasta no repo | Estado |
|---|---|---|
| Monografia (fonte LaTeX, versão final) | `revisao_tcc/Template_TCC_FEE/` | Completa, com pendências pontuais — ver [`01_monografia/pendencias.md`](01_monografia/pendencias.md) |
| Monografia (PDF final) | `revisao_tcc/Template_TCC_FEE/tcc_oseias_farias.pdf` | — |
| Cópias de revisão (não usar como fonte) | `revisao_tcc/TCC-Oseas/`, `revisao_tcc/andre/` | Desatualizadas, mantidas só para histórico de revisão |
| Software (simulador, interface, firmware) | `softwares_aeropendulo/` | Funcional com bugs pontuais — ver [`02_software/`](02_software/) |
| Site de documentação publicado (MkDocs/GitHub Pages) | `docs/` | Parcialmente incompleto ("EM DESENVOLVIMENTO" em 4 páginas) — ver [`03_docs_publicadas/resumo_mkdocs.md`](03_docs_publicadas/resumo_mkdocs.md) |
| Material de apoio bruto (bibliografia, notebooks, modelagem, prototipagem) | `materiais_complementares/` | Volumoso, com duplicações — ver [`04_materiais_complementares/`](04_materiais_complementares/) |
| Imagens/diagramas usados no README e docs | `utils/` | — |

## Como este `docs_tcc/` deve ser usado

Este diretório é um **cache de contexto** para não precisar reabrir os fontes originais (LaTeX, PDFs, notebooks, código) inteiros a cada nova tarefa:

1. Comece por **`index.yaml`** — índice de todos os documentos aqui dentro, com resumo de uma linha e tags.
2. Abra o `.md` relevante para o resumo já processado.
3. Só abra o arquivo-fonte original (caminho no campo `fonte` do front-matter de cada `.md`) quando precisar de um detalhe que não está no resumo.
4. Se o conteúdo-fonte mudar (nova revisão da monografia, novo commit no software), os resumos aqui ficam desatualizados — regenerar sob demanda, não automaticamente.

## Os 3 objetivos declarados pelo usuário (para orientar próximos passos)

1. **Finalizar a documentação do TCC** — ver punch list consolidado em [`05_plano_publicacoes/pendencias_documentacao.md`](05_plano_publicacoes/pendencias_documentacao.md).
2. **Escrever um artigo com base no TCC** — planejado do zero (decisão de 2026-09-13: um
   rascunho antigo do COBENGE 2023 existe no repositório, mas não será usado como base) —
   esqueleto/inventário em [`05_plano_publicacoes/plano_artigo.md`](05_plano_publicacoes/plano_artigo.md).
3. **Escrever um livro com base no TCC** — esqueleto/inventário de material em [`05_plano_publicacoes/plano_livro.md`](05_plano_publicacoes/plano_livro.md) (plano ainda não definido com o usuário).

**Para retomar o trabalho em qualquer sessão futura, comece por
[`05_plano_publicacoes/00_fluxo_trabalho.md`](05_plano_publicacoes/00_fluxo_trabalho.md)** —
ele sequencia as 4 fases acima (fechar pendências → finalizar documentação → artigo/livro em
sessões separadas) e diz o que é pré-requisito do quê.

## Achados críticos (não ignorar)

- O arquivo mestre LaTeX (`tcc_oseias_farias.tex`) usa `elementos_textuais/` e `elementos_pretextuais/`, **não** as pastas `Capitulos/` e `PreTextual/` que os nomes sugeririam à primeira vista — ver nota em [`01_monografia/resumo.md`](01_monografia/resumo.md).
- `softwares_aeropendulo/main_aeropendulo.py` está **quebrado** (importa classes que não existem mais); o entry point real e funcional é `rungui.py`.
- Duas equações do Capítulo 3 final aparecem literalmente como `\frac{numerador}{denominador}` em vez dos coeficientes — parece edição incompleta (ver `01_monografia/pendencias.md`).
- 4 páginas do site MkDocs publicado estão marcadas "EM DESENVOLVIMENTO..." sem conteúdo.
