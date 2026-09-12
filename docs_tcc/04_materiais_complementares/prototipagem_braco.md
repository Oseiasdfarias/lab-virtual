---
fonte: materiais_complementares/Prototipagem_do_Braco_de_Helicoptero/
gerado_em: 2026-09-12
---

# Prototipagem do Braço de Helicóptero (Aeropêndulo)

Catálogo de alto nível do material de prototipagem física do aeropêndulo (estrutura + eletrônica). Conteúdo majoritariamente visual (fotos, esquemáticos PDF/EPS); não foi necessário abrir binários/imagens em detalhe.

## diagramas/
Diagramas de arquitetura do sistema completo (PDF), não apenas do braço físico:
- `arquitetura_firmware.pdf` — arquitetura do firmware (provavelmente do ESP32).
- `estrutura_pid.pdf` — estrutura do controlador PID.
- `diagrama_ecossistema.pdf` — visão geral do "ecossistema" do projeto (hardware + software).
- `arquitetura_simulador.pdf` — arquitetura do simulador/gêmeo digital.
- `esquema_eletrico_aerop.pdf` / `.png`, `esquema_eletrico_aerop2.pdf` — esquema elétrico do aeropêndulo (duas versões).
- `diag_aerop.pdf` — diagrama geral do aeropêndulo.

## draws/
Fontes editáveis (Draw.io) correspondentes aos diagramas acima:
- `arquitetura_firmware.drawio`, `arquitetura_simulador.drawio`, `diagrama_aeropenduo.drawio`, `ecossistema_aeropendulo.drawio`, `estrutura_pid.drawio`.
- Arquivos `.bkp`/`.dtmp` ocultos — backups automáticos, sem conteúdo próprio.

## flitzing/
Projeto de protoboard/breadboard em Fritzing:
- `projeto_flitzing.fzz` — projeto editável.
- `projeto_flitzing_bb.pdf` — export da vista de breadboard.

## igm_melhoradas/
3 fotos (`.jpg`) do protótipo — versão "melhorada"/revisada da montagem física.

## img/
Fotos e desenhos gerais do protótipo:
- `IMG_20230322_120252_310.webp`, `IMG_20230322_120703_446.webp` — fotos datadas (22/03/2023) do protótipo.
- `prot_01.eps`, `prot_02.eps`, `prot_03.eps`/`.pdf`, `prot_final.pdf` — desenhos/esquemas vetoriais do protótipo em estágios sucessivos.
- `TCC_Oseas.pdf` — documento avulso (não identificado o conteúdo sem abrir; possivelmente rascunho do TCC).

## parte_eletrica/
Documentação por componente elétrico, cada subpasta com fotos (`f1.jpg`, `f2.jpg`...) e um esquemático em EPS/PDF nomeado `f<n>_<componente>`:
- `braço_aerop/` — parte elétrica do braço do aeropêndulo (`f1_braco_aerop.eps`/`.pdf`).
- `cap_resistor/` — capacitores e resistores usados no circuito (`f1_cap.eps`/`.pdf`, `rasistor.pdf`/`.jpg`, `res_cap.pdf`).
- `esp32/` — módulo ESP32 (microcontrolador principal), inclui `fs.zip` (provavelmente firmware/arquivos de sistema de arquivos do ESP32) além das fotos e esquemático (`f1_esp32.eps`/`.pdf`).
- `fonte/` — fonte de alimentação (`f1_fonte.eps`/`.pdf`, 5 fotos).
- `ponteH/` — ponte H (driver do motor), 6 fotos e esquemático (`f4_ponteH.eps`/`.pdf`).
- `potenc/` — potenciômetro (sensor de posição angular), imagem `potenci.png` e `pote.eps`/`.pdf`.

## parte_estrutural/
Materiais estruturais do braço:
- `carbono2x2mm.pdf`/`.eps` — perfil de fibra de carbono 2x2mm (provável material da haste/braço).
- `compensado.pdf`/`.eps` — madeira compensada (provável material da base/estrutura de suporte).

## Arquivo solto
- `Design sem nome.pdf` — arquivo avulso na raiz da pasta, sem nome descritivo (não identificado o conteúdo).

## Observação geral
A pasta documenta a montagem física completa do aeropêndulo: estrutura (fibra de carbono + compensado), eletrônica (ESP32, ponte H, potenciômetro, fonte, capacitores/resistores) e os diagramas de arquitetura de firmware/simulador que conectam essa parte física ao software (gêmeo digital, controlador PID). É o material de referência mais direto para a seção de "Prototipagem" da monografia (estrutura + parte elétrica + montagem, conforme previsto em `estrutura_tcc.tex` — ver `cronograma.md`).
