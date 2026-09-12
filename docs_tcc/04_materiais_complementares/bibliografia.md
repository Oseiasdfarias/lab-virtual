---
fonte: materiais_complementares/Bibliografias/, materiais_complementares/Materiais_de_Estudos/
gerado_em: 2026-09-12
---

# Bibliografia e Materiais de Estudo

Catálogo dos PDFs de referência, agrupados por categoria/pasta. Não foram abertos os PDFs — apenas listados os nomes, que em geral indicam autor/tema.

## Bibliografias/

### Artigos e Monografias Braço Levitador (8 PDFs)
Foco no próprio sistema "aeropêndulo"/braço levitador — provavelmente as referências mais diretas do TCC:
- `AeroPendulum.pdf`
- `Aero_pendulum.pdf`
- `A_New_Approach_to_Control_A_Driven_Pendulum_with_PID_Method.pdf` (citado explicitamente na modelagem matemática, ver `modelagem_sistema.md`)
- `Modeling and Control of Mechatronic.pdf`
- `Mechatronic Aeropendulum: Demonstration of Linear and Nonlinear Feedback Control Principles With MATLAB⁄Simulink Real-Time Windows Target.pdf`
- `Authors_postprint.pdf` e `Authors_postprint2.pdf` (2 versões/preprints de artigo, autor não identificável pelo nome do arquivo)
- `YAGO LUIZ MONTEIRO SILVA - TCC ENG. ELÉTRICA 2018.pdf` — TCC de referência de outro autor sobre tema correlato.

### Artigos Motor CC Série (2 PDFs)
- `Modeling and Simulation of Series DC Motors in Electric Car.pdf`
- `Series_DC_Motor_Modeling_Identification.pdf`

### Controladores (3 PDFs)
- `Control_Aula16_Sintonia_2sem17-1.pdf` — material de aula sobre sintonia de controladores.
- `monopoli10001117.pdf` — artigo (autor "Monopoli"?).
- `Apostila sobre PID e Métodos de Sintonia.pdf`

### Livros (3 PDFs)
- `Ljung_L_System_Identification_Theory_for_User-ed2.pdf` — livro clássico de identificação de sistemas (Lennart Ljung).
- `ENGENHARIA_DE_CONTROLE_MODERNO_5a_EDICAO.pdf` — livro-texto de controle moderno (Ogata, 5ª edição).
- `LivroIdentificacao_RG.pdf` — outro livro de identificação de sistemas.

### nrmse (1 PDF)
- `galoa-proceedings--sbai-2019--111356.pdf` — artigo de congresso (SBAI 2019) sobre a métrica NRMSE, usada nos notebooks de identificação.

### TCC_identificacao_sistemas (1 PDF)
- `TCC___Klarissa.pdf` — TCC de referência (autora Klarissa) sobre identificação de sistemas.

### Solto na raiz (1 PDF)
- `CT_CEREC_II_2018_02.pdf` — documento avulso, não categorizado (nome sugere "Colegiado de Curso/CEREC" — possivelmente normativa acadêmica, não bibliografia técnica).

**Total: ~19 PDFs** organizados em 6 categorias temáticas + 1 solto.

## Materiais_de_Estudos/

### SitesPdf/ (raiz)
Capturas de páginas de referência sobre um projeto similar (copter propeller angle) usado como inspiração/comparação:
- `copter_propeller_angle.txt` e `.pdf` — conteúdo/print de site de referência.
- `propeller_levitated_arm_simulation.txt` e `.jpg` — idem, versão "braço levitado por hélice".
- `ModelSimulink_CopterPropeller.jpeg`, `ModelSimulink_arm_CopterPropeller.jpeg` — capturas de modelo Simulink de referência externa.

### SitesPdf/ThePoorEnginner/ (5 PDFs)
Série de tutoriais do blog "ThePoorEngineer" sobre construção de um sistema equivalente (motor + controle + interface), usados como referência prática de implementação:
- `Building the Circuit and the Hardware - ThePoorEngineer.pdf`
- `Motor Speed Control - ThePoorEngineer.pdf`
- `Copter Angle Control (Relative) - ThePoorEngineer.pdf`
- `Plotting Serial Data from Arduino in Real Time with Python - ThePoorEngineer.pdf`
- `Creating a Graphic User Interface (GUI) with Python - ThePoorEngineer.pdf`

## Observação geral
A bibliografia cobre as três frentes teóricas do TCC: (1) sistemas aeropêndulo/braço levitador especificamente, (2) motor CC série, e (3) controle/identificação de sistemas em geral (livros-texto clássicos: Ogata, Ljung). Os materiais de estudo complementares (ThePoorEngineer, site de copter-propeller) são referências práticas externas que parecem ter inspirado a arquitetura de hardware/software do protótipo (ver `prototipagem_braco.md` e `modelagem_sistema.md`).
