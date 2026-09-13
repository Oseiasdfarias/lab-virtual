---
fonte: brainstorming em sessão de 2026-09-13, aprovado seção por seção pelo usuário
gerado_em: 2026-09-13
status: aprovado — pronto para virar plano de implementação
---

# Design — Redesenho da documentação online (site MkDocs)

## Contexto e motivação

O site publicado (`docs/`, MkDocs Material) hoje cobre só os módulos de software
(interface gráfica, gêmeo digital, firmware) e instalação — 13 páginas, sem seção de
metodologia, resultados, modelagem ou visão geral de arquitetura. O usuário quer que o
site vire **um mapa robusto do laboratório inteiro**, cobrindo o fluxo de desenvolvimento
completo, não só o software.

## Público-alvo (define tom e profundidade)

Dois públicos, ambos escolhidos explicitamente pelo usuário:

1. **Estudantes de controle querendo aprender com o material** — precisam de explicação
   pedagógica real (equações, o *porquê* de cada etapa), não só registro do que foi feito.
2. **Visitantes/portfólio** (recrutadores, outros pesquisadores) — querem entender rápido
   o que é o projeto e seu valor.

**Não** é o foco principal: banca acadêmica (já tem a monografia em PDF pra isso).

## Decisão de profundidade

**Profundidade real no site**, não um resumo com links para o PDF. O site vira o material
de estudo em si: equações renderizadas (MathJax, já configurado), gráficos, código lado a
lado com a explicação. Mais trabalho de conteúdo, mas atende os dois públicos escolhidos —
o visitante rápido lê a Visão Geral e sai satisfeito; o estudante desce até Identificação de
Sistemas e Controle e encontra profundidade de verdade.

## Estrutura de navegação (abordagem aprovada: fluxo temático do pipeline)

Rejeitadas: (A) espelhar a ordem dos capítulos da monografia — pareceria "PDF picotado";
(C) site em duas trilhas (rápida vs. profunda) — dobra o trabalho de navegação e arrisca
duplicar conteúdo.

Aprovada: organizar pela sequência real do trabalho científico/de engenharia — da física
para o modelo, do modelo para a identificação, da identificação para o controle, dos
resultados para a implementação:

```yaml
nav:
  - Início: index.md
  - Visão Geral:
      - O que é o Laboratório Virtual: visao-geral/index.md
      - Arquitetura do sistema: visao-geral/arquitetura.md
  - Protótipo:
      - Estrutura física e elétrica: prototipo/index.md
  - Modelagem Matemática:
      - Dedução do modelo: modelagem/index.md
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
          - Python: software/instalacao/python.md
          - Dependências: software/instalacao/dependencias.md
  - Referência de Código:
      - animacao_aeropendulo: referencia/animacao_aeropendulo.md
      - graficos_aeropendulo: referencia/graficos_aeropendulo.md
      - interface_interativa: referencia/interface_interativa.md
```

Nota: os nomes de arquivo/pasta acima trocam acentos e maiúsculas por ASCII em minúsculas
(`prototipo` em vez de `Protótipo`) — evita problemas de URL/encoding que o site atual tem
(pastas como `Módulo Firmware` geram URLs com `%C3%B3` etc.). O **título exibido** na
navegação continua acentuado normalmente (`title:` no front-matter e o texto do `nav:`).

## Fonte de conteúdo por página nova (nada inventado — tudo adaptado do que já existe)

| Página nova | Fonte primária | Adaptação |
| --- | --- | --- |
| Visão Geral / Arquitetura | `README.md` + Cap. 1 e 3 da monografia | Reescrita curta, tom de abertura |
| Modelagem Matemática | Cap. 2 (`2_2_fundamentacao_teorica.tex`, `2_3_modelagem_analitica.tex`) + `simulador_aeropendulo/docs/Modelagem_matematica_do_aeropendulo.ipynb` (função de transferência numérica já derivada) | Prosa pedagógica + equações MathJax + tabela de parâmetros reais |
| Identificação de Sistemas (3 páginas) | Cap. 3 da monografia (PRBS → mínimos quadrados → Tustin → validação) | Dividido em 3 páginas menores; foco no *porquê* de cada etapa |
| Projeto de Controle (2 páginas) | Cap. 3 (parte de controlador PID) + `materiais_complementares/.../ident_up/` | Idem, registro pedagógico |
| Software/Firmware/Interface/Instalação/Referência | Já existem, preenchidas em sessão anterior | Só realocação de caminho, sem reescrita de conteúdo |

## Migração das páginas existentes (nenhuma descartada)

| Página atual | Novo caminho |
| --- | --- |
| `docs/Componentes do Aeropêndulo/aeropendulo_doc.md` | `prototipo/index.md` |
| `docs/Componentes do Aeropêndulo/gemeo_digital.md` | `gemeo-digital/index.md` |
| `docs/Componentes do Aeropêndulo/interface_grafica_usuario.md` | `software/interface-grafica.md` |
| `docs/Módulo Firmware/aeropendulo_doc.md` | `software/firmware.md` |
| `docs/Módulos Gêmeo Digital/*_reference.md` | `referencia/*.md` |
| `docs/1 Instalações e Configurações/**` | `software/instalacao/**` |
| `docs/index.md` | Reescrito: topo vira gancho + mapa das seções; conteúdo atual (demonstração, membros) desce para uma seção "Sobre" no fim da página |

## Figuras e equações

- **Equações**: MathJax já configurado em `mkdocs.yml` (`pymdownx.arithmatex` +
  `mathjax.js`) — usar `$$...$$` diretamente, sem trabalho de infraestrutura.
- **Figuras**: a maioria está em PDF dentro de `revisao_tcc/.../3_figuras/` e
  `2_aeropendulo/4_figuras/`. Convertê-las para PNG com `pdftoppm` (disponível localmente)
  sob demanda, por página — sem gerar imagem nova, só reaproveitar o que já existe.

## Ordem de entrega (cada etapa é revisável antes da próxima)

1. Estrutura de nav explícita + migração mecânica das páginas existentes (baixo risco)
2. Visão Geral + Arquitetura
3. Modelagem Matemática
4. Identificação de Sistemas (3 páginas)
5. Projeto de Controle (2 páginas)
6. Ajustes finais de navegação cruzada (links entre páginas relacionadas)

## Critério de pronto

- `mkdocs build --strict` passa sem avisos após cada etapa.
- Nenhuma URL antiga fica quebrada sem um motivo documentado (idealmente, redirecionar ou
  aceitar que é troca de estrutura e o site é o mesmo repo/deploy, não precisa de redirect
  externo).
- Todo conteúdo pedagógico novo rastreável a uma fonte real (capítulo da monografia,
  notebook, dado de ensaio) — nada de coeficiente, valor ou afirmação técnica inventada.
