---
fonte: síntese de docs_tcc/01_monografia/pendencias.md, docs_tcc/02_software/*, docs_tcc/03_docs_publicadas/resumo_mkdocs.md
gerado_em: 2026-09-12
---

# Punch list — o que falta para "finalizar a documentação"

Lista consolidada dos gaps encontrados no levantamento, para decidir por onde retomar. Sem prioridade definida ainda — priorizar com o usuário.

## Monografia (texto)

- [ ] Resolver as 2 equações do Cap. 3 (`eq3:eq3`, `eq3:eq4`) que aparecem como `\frac{numerador}{denominador}` literal em vez dos coeficientes reais — provável edição incompleta. Ver [`../01_monografia/pendencias.md`](../01_monografia/pendencias.md).
- [ ] Corrigir erro de concordância verbal no Cap. 4 ("Os subsistemas concebido... foi... desenvolvido").
- [ ] Padronizar terminologia: "ecossistema" vs "estrutura", "subsistemas" vs "laboratório virtual" usados sem consistência entre capítulos.
- [ ] Revisar listas de siglas/símbolos (`elementos_pretextuais/siglas.tex`, `simbolos.tex`) — atualmente têm conteúdo genérico de template (CPU, FPGA, VHDL, campo elétrico) sem relação com o aeropêndulo.
- [ ] Corrigir entradas duplicadas/erradas no `.bib` real (`bibtex-referencias.bib` na raiz do `Template_TCC_FEE`): `vpython`/`vpython11` apontam para URL errada (CustomTkinter em vez de VPython); entrada `exemplo` (física de partículas) é resíduo de template.
- [ ] Confirmar se os dois arquivos abandonados (`2_1_descricao.tex` só com "teste", `2_4_modelagem_identificacao_sistemas.tex` com "CONTINUA...") devem ser apagados ou se o conteúdo real (que migrou para o Cap. 3) precisa de uma referência cruzada explicando a reorganização.
- [ ] Decidir se vale acrescentar métricas quantitativas de erro (RMSE/EQM) na seção de Resultados — atualmente a validação é só qualitativa/visual (o autor já reconhece isso como limitação no Cap. 4).
- [ ] Checar sugestões do orientador ainda não incorporadas — comparar `revisao_tcc/andre/Sugestões TCC - Oseias.docx` (já lido pelo agente) ponto a ponto com a versão final.

## Software

- [ ] `main_aeropendulo.py` está quebrado (importa `ModeloMatAeropendulo`/`ControladorDiscreto`, que não existem mais no pacote) — decidir se remove o arquivo ou atualiza para usar a API atual (`Simulador`, `Graficos`, `AnimacaoAeropendulo`).
- [ ] `firmwares_microcontroladores/PlatformIo/Arduino_Nano/src/main.cpp` tem erro de sintaxe (caractere solto `k`) — não compila.
- [ ] Renomear ou corrigir `Esp32_ttgo_modulos_freertos`: não usa nenhuma API de FreeRTOS de fato e tem menos funcionalidade que `Esp32_ttgo_modulos` (que é a variante mais completa). Nome atual induz a erro.
- [ ] Remover arquivos vazios: `PlatformIo/Esp32_ttgo/lib/ler_escrever_serial/src/ler_escrever_serial.{cpp,h}`.
- [ ] Revisar dois bugs suspeitos no firmware: dimensionamento do termo derivativo em `controlador_pid.cpp`; condição de clamp `0.0 <= x <= 3.3` em `conversor.cpp` (não faz clamping em C++, é sempre verdadeira).
- [ ] `requirements.txt` desatualizado (pip freeze de ambiente Jupyter) — ou remover ou regenerar a partir do `pyproject.toml`/Poetry para não confundir quem for reproduzir o ambiente.
- [ ] Documentar o mapeamento de colunas dos CSVs de ensaio (`src_interface/dados_de_ensaio/*.csv`) — hoje só tem índices numéricos, sem cabeçalho nomeado nem documentação do protocolo serial em lugar nenhum do projeto.

## Site publicado (MkDocs / GitHub Pages)

- [ ] 4 páginas marcadas "EM DESENVOLVIMENTO...": as páginas de "Componentes do Pendulab" (exceto talvez uma) e "Módulo Firmware" — só têm cabeçalho institucional e uma imagem, sem texto real. Ver [`../03_docs_publicadas/resumo_mkdocs.md`](../03_docs_publicadas/resumo_mkdocs.md) para a lista exata.
- [ ] As páginas de referência técnica (`Módulos Gêmeo Digital/*_reference.md`, via mkdocstrings) dependem de docstrings no código Python estarem completas — conferir se `simulador_aeropendulo/*.py` tem docstrings suficientes para essas páginas não saírem vazias.

## Organização do repositório (limpeza, opcional)

- [ ] Decidir o destino de `revisao_tcc/TCC-Oseas/` e `revisao_tcc/andre/` (cópias de revisão desatualizadas) — manter como histórico ou arquivar fora do repo principal.
- [ ] `materiais_complementares/Identificacao_de_Sistemas/` tem forte duplicação de notebooks entre a raiz, `identificacao_aeropendulo/` e `identificacao_aeropendulo/ident_up/` (esta última é a mais avançada) — vale consolidar.
- [ ] Vários nomes de arquivo com encoding corrompido (ex.: `Identifica├з├гo.py`) dentro de `materiais_complementares/` — renomear para evitar problemas de portabilidade.
