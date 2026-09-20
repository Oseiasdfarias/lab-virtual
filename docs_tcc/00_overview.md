---
fonte: síntese de todo docs_tcc/ + estrutura do repositório
gerado_em: 2026-09-12
atualizado_em: 2026-09-13
---

# Visão geral do projeto

## O que é

TCC de Engenharia Elétrica (UFPA — Campus Universitário de Tucuruí), autor **Oséias Dias de Farias**, orientação de **Raphael Barros Teixeira**; o "André" dos arquivos de revisão é o **Prof. André Cruz**, da banca. Defendido em 11/12/2023, publicado na BDM/UFPA (https://bdm.ufpa.br/handle/prefix/6944). Repositório público `Oseiasdfarias/lab-virtual` ("Laboratório Virtual"), versão 1.0.0, código sob MIT e documentação sob CC BY 4.0.

Título no site publicado: *"Desenvolvimento de Protótipo e Gêmeo Digital como Ferramenta para um Laboratório Virtual com Foco em Modelagem e Controle de Sistemas Dinâmicos"*.
Subtítulo/tema no README: *"Identificação de Sistemas, Simulador Gráfico e Prototipagem de um Aeropêndulo para estudos de Projetos de Controle"*.

O projeto tem 4 frentes que se integram:

1. **Protótipo físico** — um aeropêndulo (braço com motor CC + hélice, ESP32/Arduino) para servir de planta real de testes de controle.
2. **Firmware** — roda no microcontrolador, faz leitura de sensores, controle PID em malha fechada e comunicação serial com o PC.
3. **Interface gráfica (PC)** — coleta dados via serial, plota sinais em tempo real, salva ensaios em CSV.
4. **Gêmeo digital** — réplica 3D em VPython que espelha, em tempo real, o ângulo medido no protótipo (não integra um modelo da planta).

## Onde está cada coisa (mapa rápido)

| Área | Pasta no repo | Estado |
|---|---|---|
| Monografia (fonte LaTeX, versão final) | `revisao_tcc/Template_TCC_FEE/` | Completa, com pendências pontuais — ver [`01_monografia/pendencias.md`](01_monografia/pendencias.md) |
| Monografia (PDF final) | `revisao_tcc/Template_TCC_FEE/tcc_oseias_farias.pdf` | — |
| Cópias de revisão (não usar como fonte) | `revisao_tcc/TCC-Oseas/`, `revisao_tcc/andre/` | Desatualizadas, mantidas só para histórico de revisão |
| Software (simulador, interface, firmware) | `softwares_aeropendulo/` | Funcional, com testes automatizados; o que depende do protótipo está em [`divida_tecnica.md`](divida_tecnica.md) |
| Site de documentação publicado (MkDocs/GitHub Pages) | `docs/` | Completo, com deploy automático — ver [`03_docs_publicadas/resumo_mkdocs.md`](03_docs_publicadas/resumo_mkdocs.md) |
| Material de apoio bruto (bibliografia, notebooks, modelagem, prototipagem) | `materiais_complementares/` | Duplicações removidas; inclui os scripts de métricas — ver [`04_materiais_complementares/`](04_materiais_complementares/) |
| Dívida técnica (o que exige o protótipo real) | [`divida_tecnica.md`](divida_tecnica.md) | Firmware sem validação em hardware, pino do sensor, dependências novas |
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

- O arquivo mestre LaTeX (`tcc_oseias_farias.tex`) inclui a introdução de `elementos_textuais/` e os capítulos 2 a 4 de `Capitulos/` — ver [`01_monografia/resumo.md`](01_monografia/resumo.md).
- A função de transferência de 10ª ordem da monografia tem 7 amostras de atraso a mais que o ARX estimado (montagem em potências positivas de z): NRMSE 55,97 % publicado × 78,30 % correto. Ver `docs/identificacao/validacao.md`.
- Correções do firmware (PID, conversor) e as dependências Python novas não foram testadas no protótipo; o esquema elétrico e o firmware divergem no pino do sensor. Ver [`divida_tecnica.md`](divida_tecnica.md).
- Os ensaios de malha fechada gravados (0–10°, 0,2 e 0,15 Hz) não têm os parâmetros citados no texto da monografia (0,5 Hz, 15°).
