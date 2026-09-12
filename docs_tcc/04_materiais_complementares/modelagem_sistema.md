---
fonte: materiais_complementares/Modelagem_do_Sistema/ (Diagramas_draw/, Modelos_Matematicos/, Simulacoes/)
gerado_em: 2026-09-12
---

# Modelagem do Sistema

Catálogo de alto nível da modelagem matemática e simulações do aeropêndulo e do motor CC série.

## Modelos_Matematicos/

### Modelagem_matematica_do_aeropendulo/
- `Modelagem_matematica_do_aeropendulo.ipynb` — dedução do modelo matemático do braço do aeropêndulo a partir das leis de Newton/momento angular. Referência citada: "A New Approach to Control A Driven Pendulum with PID Method". Trata o sistema como 1 grau de liberdade (ângulo θ), decompõe em dois subsistemas (motor CC série + braço do aeropêndulo), obtém a equação diferencial `F_e = J_b·θ'' + c·θ' + mgd·sen(θ)` e sua função de transferência via Laplace. Relaciona empuxo da hélice com velocidade angular do motor (aproximação linear `F_e ≈ K_m·ω̇`).
- `utils/` — imagens de apoio (`diagrama_aeropendulo.png`, `aeropendulo.png`) e `desenho_aeropendulo.pdf`.

### Modelagem_MotorCC_Serie/
- `Modelagem_motor_cc_serie.ipynb` — modelagem do motor CC série (enrolamento de campo em série com armadura, `i = i_f = i_a`). Cobre modelagem da parte mecânica (`J·ω'' = T_e - b·ω' - T_L`) e elétrica do motor.
- `modelagem_motorcc.xopp` / `modelagem_motorcc.pdf` — anotações manuscritas (Xournal++) da dedução, exportadas em PDF.
- `utils/` — diagramas de apoio: esquema elétrico do motor (`esquema_motor_cc.pdf`, `esquema_motorcc.png`), diagrama elétrico/mecânico (`diagrama_motorcc.png`, `diagrama_motor_cc.pdf`) e imagem do braço com hélice (`propeller_levitated_arm.png`).

## Simulacoes/

### Aeropendulo_MatlabSimulink/
- `Simulink_copter_propeller_angle.slx` — modelo Simulink único do sistema copter/propeller-angle (arquivo binário, não inspecionado em profundidade).

### Aeropendulo_Python/
- `animacao_aeropendulo1.py` — animação 3D do aeropêndulo usando VPython (classe `AnimacaoAeropendulo`), autoria "Oséias Farias", projeto "Laboratório Virtual Sistemas Dinâmicos e Controle" (orientadores Raphael Teixeira e Rafael Bayma). É um protótipo antecessor do módulo de animação hoje documentado em `docs/Módulos Gêmeo Digital/animacao_aeropendulo_reference.md`.
- `aeropendulo.png`, `simulacao.png` — imagens de apoio/resultado.
- `arquivos_complementares/`:
  - `README.md` — documento completo com a dedução do modelo linearizado do aeropêndulo (equações 1–10, incluindo representação em espaço de estados na forma canônica de controlador) e um tutorial passo a passo de simulação em Python usando a biblioteca `control` (define matrizes A/B/C/D, calcula FT via `ss2tf`, resposta ao degrau, polos/zeros, `step_info`). Parâmetros usados: K_m=0,0296; d=0,03m; J=0,0106 kg·m²; m=0,36; g=9,8; c=0,0076 Nms/rad.
  - `Modelagem_matematica_do_aeropendulo.ipynb` — cópia do notebook de `Modelos_Matematicos/`.
  - `modelagem_e_analise.pdf` / `.xopp` — anotações manuscritas equivalentes.
  - `braca_helicoptero.py` — script simples de simulação de pêndulo com VPython (protótipo/rascunho, referencia variáveis `bob`/`pivot` não definidas antes do uso — parece exemplo de teste/estudo, não código final).
  - `sim_pendulo_simples_graficos.py`, `test_mma.py`, `test.py` — scripts de teste/exploração adicionais (não inspecionados em detalhe, nomes sugerem simulação de pêndulo simples e testes do modelo).
  - `utils/` — pasta de apoio (imagens).

## Diagramas_draw/

Diagramas em formato Draw.io (`.drawio`) com exports em PDF/SVG/PNG, cobrindo:
- `subsistemas_aeropendulo.drawio` / `subsistemas_aeropendulo1.drawio` — diagrama de blocos dos subsistemas do aeropêndulo (motor + braço), com exports em `img/subsistemas_aeropendulo.pdf` e `img/subsistemas_aeropendulo1.pdf`.
- `ft_subsistemas.drawio` — diagrama de função de transferência dos subsistemas (`img/ft_subsistemas.pdf`, `ft_subsistemas.svg`).
- `esquema_eletrico.drawio` — esquema elétrico geral, com exports em `.pdf`, `.png`, `.dxf` (também aberto no FreeCAD: `diagrama_eletrico.FCStd`/`.FCStd1`).
- `img/subsistemas_motorcc1.pdf` — diagrama de blocos específico do motor CC.
- `exemplo.drawio` — arquivo de exemplo/teste do Draw.io (não relevante ao conteúdo).
- Pastas `esquematico_eletrico/` e `esq/` — variações/rascunhos do esquema elétrico.
- Arquivos `.bkp`/`.dtmp` ocultos — backups automáticos do Draw.io, sem conteúdo próprio.

## Observação geral
A modelagem segue a abordagem clássica de dividir o aeropêndulo em dois subsistemas (motor CC série + braço/hélice), obter cada função de transferência por Newton/Laplace, e depois validar/ajustar via identificação de sistemas (ver `identificacao_sistemas.md`). A simulação em Python (`arquivos_complementares/README.md`) é o material mais completo e citável para reconstituir a dedução matemática linearizada e o código de simulação em `control`/`numpy`.
