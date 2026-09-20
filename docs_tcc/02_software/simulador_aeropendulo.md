---
fonte: softwares_aeropendulo/simulador_aeropendulo/simulador.py, softwares_aeropendulo/simulador_aeropendulo/animacao_aeropendulo.py, softwares_aeropendulo/simulador_aeropendulo/graficos_aeropendulo.py, softwares_aeropendulo/simulador_aeropendulo/__init__.py, softwares_aeropendulo/simulador_aeropendulo/README.md, softwares_aeropendulo/simulador_aeropendulo/interfaces/
gerado_em: 2026-09-12
atualizado_em: 2026-09-13
---

# Simulador Aeropêndulo (Gêmeo Digital)

## Nota sobre `interfaces/`

`simulador_aeropendulo/interfaces/` **não é uma cópia duplicada** do conteúdo da raiz do pacote. Contém apenas as classes abstratas (`ABC`) que definem o contrato de cada módulo (`SimuladorInterface`, `AnimacaoAeropenduloInterface`, `GraficosInterface`), muito menores (poucas dezenas de linhas, só assinaturas `@abstractmethod`). Os arquivos da raiz (`simulador.py`, `animacao_aeropendulo.py`, `graficos_aeropendulo.py`) importam dessas interfaces e implementam de fato a lógica. Não há duplicação de lógica — apenas separação interface/implementação.

## Modelo físico

O modelo matemático do aeropêndulo (documentado em `simulador_aeropendulo/README.md` e no notebook `docs/Modelagem_matematica_do_aeropendulo.ipynb`) é derivado por Newton/momento angular:

```
T = J·θ̈ + c·θ̇ + m·g·d·sin(θ)        (equação não linear do aeropêndulo)
T ≈ Km·V                              (aproximação linear empuxo ≈ ganho do motor × tensão)
```

Onde `J` = momento de inércia, `c` = coeficiente de atrito viscoso, `m` = massa, `d` = distância do centro de massa ao eixo, `Km` = ganho estático do motor/hélice, `V` = tensão de controle, `θ` = ângulo do braço.

**Importante:** essa equação diferencial (a parte "matemática" do gêmeo digital, que integraria os estados a partir de `u`) não está implementada em nenhuma classe do pacote atual `simulador_aeropendulo`. A classe que faria isso (`ModeloMatAeropendulo`) não existe mais no código-fonte, e o script que a usava (`main_aeropendulo.py`) foi removido. A classe `Simulador` atual (ver abaixo) **não resolve a EDO**: ela é um "consumidor" de estados (ângulo, referência, tempo) vindos de fora (da interface real via serial, ou de outro lugar) e só cuida da parte gráfica/visual (rotacionar o modelo 3D e atualizar os plots).

## `simulador.py` — classe `Simulador`

```python
class Simulador(SimuladorInterface):
    def __init__(self, graficos: GraficosInterface, animacao_aeropendulo: AnimacaoAeropenduloInterface) -> None: ...
    def atualizar_estados(self, t, theta, ref) -> None: ...
```

- Recebe já prontos `graficos` (objeto `Graficos`) e `animacao_aeropendulo` (objeto `AnimacaoAeropendulo`) por injeção de dependência.
- `atualizar_estados(t, theta, ref)` é o método central, chamado externamente (por `InterfaceAeropendulo.atualizar_simulador()` em `src_interface/interface_grafica.py`) a cada novo dado lido do microcontrolador:
  - converte `theta` de graus para rad;
  - deriva numericamente a velocidade angular (`dtheta_rad = Δθ/Δt`);
  - rotaciona o objeto 3D do aeropêndulo (`vp.compound`) proporcionalmente à variação angular;
  - anima a hélice (`update_helice`);
  - atualiza dois plots VPython (`plot1`=ângulo, `plot2`=referência).
- Ou seja: o "gêmeo digital" atual é **guiado por dados reais** (hardware) — não roda uma simulação independente da física; ele espelha visualmente o que está acontecendo no aeropêndulo físico.

## `animacao_aeropendulo.py` — classe `AnimacaoAeropendulo`

Implementa a cena 3D usando VPython (`vp.canvas`, `vp.box`, `vp.cylinder`, `vp.compound`, `vp.text`):

- Monta a estrutura física do aeropêndulo: base de madeira, parede de fundo com texto "AEROPÊNDULO", braço (`barra`), motor (cilindro + caixa), hélice composta por 4 pás (`helice`, `helice1..3` em ângulos de 0/45/90/135° para simular giro por transparência/visibilidade alternada).
- `pause_giro()` / `girar_helice()` alternam a visibilidade das pás extras para dar ilusão de rotação quando o motor está ligado/parado.
- `update_helice(angle, ts)` gira a hélice em torno de si mesma (eixo local, ângulo pequeno fixo por frame — `0.09` rad — independente da física real; é só efeito visual de "girando").
- `set_posicao_helice(angle)` reposiciona a hélice acompanhando a rotação do braço em torno do eixo de suspensão (`origin=(0, 5.2, 0)`).
- Logo da UFPA carregado via URL externa (`vp.textures`, imagem no imgur) — dependência de rede para a textura.

## `graficos_aeropendulo.py` — classe `Graficos`

Cria um gráfico VPython (`vp.graph`, scroll automático, `xmin=0, xmax=14`) com duas curvas (`vp.gcurve`):
- `curva1` — Posição Angular (graus).
- `curva2` — Referência Angular (graus).

Curvas de velocidade angular e sinal de controle estão comentadas no código (desativadas), sugerindo uma versão anterior mais completa que foi simplificada.

## `interface_interativa.py` (removido)

A classe `Interface` (widgets sobre a cena VPython) só era usada pelo `main_aeropendulo.py` e
dependia de um controlador que não existe no repositório; foi removida em 2026-09-13.

## Resumo do fluxo de animação

1. Hardware real envia via serial: referência, ângulo, erro, sinal de controle, etc. (ver `dados_ensaios.md`).
2. `src_interface.interface_grafica.InterfaceAeropendulo.update()` lê esses dados e chama `simulador.atualizar_estados(t, theta, ref)`.
3. `Simulador` traduz o ângulo real em rotação 3D do modelo VPython e atualiza os 2 gráficos VPython — funcionando como uma visualização 3D paralela aos gráficos 2D (matplotlib) da GUI principal.
