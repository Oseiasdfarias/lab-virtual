---
fonte: docs/index.md, docs/Componentes do Pendulab/*.md, docs/Módulo Firmware/aeropendulo_doc.md, docs/Módulos Gêmeo Digital/*.md, docs/1 Instalações e Configurações/**
gerado_em: 2026-09-12
---

# Resumo do Site MkDocs (docs/)

## Propósito geral
O site é a **documentação pública do "PenduLab"** — nome dado ao ecossistema de software/hardware construído a partir do TCC (protótipo + gêmeo digital de um laboratório virtual de modelagem e controle de sistemas dinâmicos, UFPA Campus Tucuruí). Funciona como: (1) guia de instalação/configuração do ambiente Python, e (2) referência técnica dos componentes do sistema e dos módulos de software do gêmeo digital. Autoria: Oséias Farias.

## Páginas

### docs/index.md
- Página inicial: apresenta o projeto PenduLab, contextualiza que ele nasceu do TCC "Desenvolvimento de Protótipo e Gêmeo Digital como Ferramenta para um Laboratório Virtual com Foco em Modelagem e Controle de Sistemas Dinâmicos" (UFPA/Tucuruí).
- Lista os membros/colaboradores atuais do projeto (com créditos estilo "all-contributors").
- Serve como landing page/apresentação, sem conteúdo técnico.

### Componentes do Pendulab/aeropendulo_doc.md — "Desenvolvimento do Protótipo"
- Página com cabeçalho, logos institucionais e 1 imagem do protótipo físico.
- **Marcada como "EM DESENVOLVIMENTO..."** — página incompleta/stub, sem conteúdo textual real além da imagem.

### Componentes do Pendulab/gemeo_digital.md — "Gêmeo Digital"
- Mesmo padrão: cabeçalho + 1 imagem ilustrativa do gêmeo digital.
- **Marcada como "EM DESENVOLVIMENTO..."** — página incompleta/stub.

### Componentes do Pendulab/interface_grafica_usuario.md — "Interface Gráfica de Usuário"
- Cabeçalho + 1 imagem (screenshot da interface, tema claro).
- **Marcada como "EM DESENVOLVIMENTO..."** — página incompleta/stub.

### Módulo Firmware/aeropendulo_doc.md — "Desenvolvimento do Firmware para ESP32"
- Cabeçalho + 1 imagem (diagrama de blocos do sistema em malha fechada).
- **Marcada como "EM DESENVOLVIMENTO..."** — página incompleta/stub.

### Módulos Gêmeo Digital/animacao_aeropendulo_reference.md
- Referência técnica autogerada (mkdocstrings) da classe `AnimacaoAeropendulo` (módulo `softwares_aeropendulo.simulador_aeropendulo.animacao_aeropendulo`), documentando métodos como `girar_helice`, `pause_giro`, `update_helice`, `__desenhar_pendulo`.
- Página funcional/completa (é gerada automaticamente a partir das docstrings do código-fonte).

### Módulos Gêmeo Digital/graficos_aeropendulo_reference.md
- Referência técnica autogerada da classe `Graficos` (módulo `graficos_aeropendulo`), documentando o método `graficos`.
- Página funcional/completa, porém bem enxuta (só 1 método documentado).

### Módulos Gêmeo Digital/interface_interativa_reference.md
- Referência técnica autogerada da classe `Interface` (módulo `interface_interativa`), documentando `rotate`, `__slide_angle_referencia`, `__criar_interface`, `__executar`.
- Página funcional/completa (gerada via mkdocstrings).

### 1 Instalações e Configurações/
- `1.1 Instalacao_python/index.md` — introdução geral, requisito de Python ≥ 3.8, aponta para os tutoriais por SO.
- `1.1 Instalacao_python/1.1 Instalacao_python_ubuntu.md` — tutorial de instalação do Python 3.10 no Ubuntu.
- `1.1 Instalacao_python/1.2 Instalacao_python_windows.md` — tutorial de instalação do Python 3.10 no Windows.
- `1.1 Instalacao_python/1.3 Instalacao_python_macos.md` — tutorial de instalação do Python 3.10 no macOS.
- `1.2 Instalacao_dependencias_python/1.2 Instalacao_dependencias_python.md` — tutorial de instalação das dependências Python do projeto.
- Conjunto completo e funcional: cobre os 3 principais sistemas operacionais + dependências.

## Diagnóstico de completude
- **Completas/funcionais**: toda a seção "1 Instalações e Configurações" (guias de instalação) e as 3 páginas de referência técnica em "Módulos Gêmeo Digital" (geradas via mkdocstrings a partir do código).
- **Incompletas (stub "EM DESENVOLVIMENTO...")**: as 4 páginas de "Componentes do Pendulab" + "Módulo Firmware" — todas têm apenas cabeçalho institucional e uma imagem, sem texto explicativo. São claramente os pontos pendentes de redação do site.
