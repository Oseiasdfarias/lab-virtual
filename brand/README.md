# Laboratório Virtual — identidade visual

Marca do projeto (protótipo + gêmeo digital de aeropêndulo para estudo de modelagem,
identificação e controle de sistemas dinâmicos).

## O símbolo

O ícone é o próprio aeropêndulo, com a física correta:

- **Pivô** no topo, com a **linha tracejada** marcando a posição de repouso (haste na vertical).
- **Arco com seta** indicando o movimento real: a haste **sobe** do repouso até o ângulo
  comandado. Não é balanço simétrico de pêndulo.
- **Haste** erguida a 50° da vertical.
- **Motor** perpendicular à haste (o empuxo perpendicular é o que gera torque no pivô).
- **Hélice** na ponta do motor, com a envergadura paralela à haste — ou seja, o disco da
  hélice contém a haste, como no equipamento real.

Tomando o comprimento da haste como `L`: motor e meia-envergadura da hélice valem `0,286·L`
cada; espessuras de haste, motor e hélice são `0,089·L`, `0,161·L` e `0,071·L`; o pivô tem
raio `0,107·L`; o arco de subida tem raio `0,464·L` e vai de 8° a 44°.

Esses números são a transcrição exata do desenho aprovado — não altere sem pedido explícito.

## Arquivos

### SVG (`svg/`) — use sempre que possível

**O padrão é a versão com contorno** (preenchimento claro + contorno escuro): ela funciona
sobre fundo claro, escuro ou foto sem precisar trocar de arquivo. Por isso não existe uma
variante "para fundo escuro" — é a mesma.

| Arquivo | Uso |
| --- | --- |
| `icone.svg` | **Padrão.** Símbolo completo com contorno. |
| `icone-reduzido.svg` | Idem, sem o arco e a linha de repouso. Para tamanhos médios. |
| `logo-horizontal.svg` | **Padrão.** Assinatura: símbolo + nome lado a lado. |
| `logo-vertical.svg` | **Padrão.** Assinatura empilhada, para espaços estreitos. |
| `favicon.svg` | Corte compacto e mais pesado. **Sólido de propósito** — abaixo de ~32 px o contorno fecha os vãos e vira borrão. |
| `favicon-branco.svg` / `favicon-contorno.svg` | Alternativas do favicon. |

Alternativas sólidas — use quando o contorno atrapalhar (impressão em uma cor, gravação,
tamanhos pequenos, ou quando o logo já está sobre fundo de cor conhecida):

| Arquivo | Uso |
| --- | --- |
| `icone-solido.svg` / `logo-horizontal-solido.svg` / `logo-vertical-solido.svg` | Tinta sólida, para fundo claro. |
| `icone-solido-branco.svg` | Branco sólido, para fundo escuro. |
| `icone-mono.svg` / `logo-horizontal-mono.svg` | Usam `currentColor` — herdam a cor do CSS. Ideal para web. |
| `icone-coral.svg` | Cor legada do Pendulab (#FF5757), caso queira o acento antigo. |

### PNG (`png/`)

Rasterizados com Chrome headless (antialiasing superior). Ícone em 1024/512/256/128/64,
favicon em 180/64/32/16, assinaturas em 1600/800 px.

## Cores

| Papel | Hex |
| --- | --- |
| Tinta (símbolo e texto, fundo claro) | `#1D1D1F` |
| Papel (símbolo e texto, fundo escuro) | `#F5F5F7` |
| Coral legado (Pendulab, opcional) | `#FF5757` |

O arco e a linha de repouso são anotação de medição, não fazem parte do objeto físico.
Eles são desenhados **por cima** da haste (senão a seta fica cortada ao meio), e por isso
usam cor sólida em vez de opacidade — sobre o preto da haste, cinza translúcido sumiria:

| Elemento | Sobre fundo claro | Sobre fundo escuro |
| --- | --- | --- |
| Arco e seta | `#616162` | `#B4B4B6` |
| Linha de repouso | `#BBBBBC` | `#5E5E60` |

São exatamente o equivalente sólido de 70% e 30% da cor principal sobre o fundo.
A variante `icone-mono.svg` mantém opacidade real, já que herda a cor do CSS.

## Tipografia

**IBM Plex Sans SemiBold** para o nome; **IBM Plex Sans** Regular/Medium para textos de apoio.

Escolhida por ter sido desenhada para contexto técnico — tem caráter de engenharia sem
virar estilização — e por vir com a família completa (Sans, Mono e Serif) sob SIL OFL, o que
dá um sistema tipográfico coerente para reaproveitar na monografia, no artigo e em slides.

Nas assinaturas em SVG o texto já está convertido em curvas, então não depende da fonte
estar instalada em quem abre o arquivo. O alinhamento vertical do nome contra o ícone usa a
altura de caixa alta real declarada na fonte (`OS/2.sCapHeight`), não um fator fixo — trocar
de fonte no script reposiciona o texto sozinho.

## Regras de uso

- Área de respiro mínima ao redor da assinatura: a altura do pivô (o círculo do topo).
- Abaixo de ~48 px, troque o ícone completo pelo `favicon.svg` — o arco e a linha
  tracejada entopem em tamanhos pequenos.
- Não recolora o símbolo fora da tabela acima, não incline e não altere o ângulo da haste
  (50° é o que mantém a leitura de "erguido, não pendurado").
- Sobre foto ou fundo de cor incerta, use a variante `-branco-contorno`.

## Como regenerar

Os arquivos são gerados por script, não desenhados à mão. Fonte dos scripts:
`gen_brand.py` (geometria e SVG) e `render_browser.py` (rasterização via Chrome).
Alterar uma proporção significa mudar a constante no script e rodar de novo, para que
todas as peças continuem consistentes entre si.
