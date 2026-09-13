<p align="center">
  <img height="120px" src="./brand/png/logo-vertical-800.png" alt="Laboratório Virtual">
</p>

<p align="center">
  <strong>Plataforma didática para modelagem, identificação e controle de sistemas dinâmicos</strong><br>
  <sub>Universidade Federal do Pará · Campus Universitário de Tucuruí · Faculdade de Engenharia Elétrica</sub>
</p>

<p align="center">
  <a href="https://oseiasdfarias.github.io/lab-virtual/"><img alt="Documentação" src="https://img.shields.io/badge/documenta%C3%A7%C3%A3o-online-1D1D1F?style=flat-square"></a>
  <img alt="Python" src="https://img.shields.io/badge/python-3.10%E2%80%933.11-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="Firmware" src="https://img.shields.io/badge/firmware-ESP32%20%7C%20PlatformIO-FF7F00?style=flat-square">
</p>

---

## Resumo

Este repositório reúne o resultado de um Trabalho de Conclusão de Curso em Engenharia
Elétrica cujo objetivo foi construir uma plataforma completa — física e computacional —
para o ensino e a experimentação em modelagem e controle de sistemas dinâmicos.

O sistema adotado como planta é um **aeropêndulo**: uma haste articulada em um pivô, com
um motor CC e hélice acoplados à extremidade. O empuxo gerado pela hélice produz torque em
torno do pivô e eleva a haste a partir do repouso; a variável controlada é o ângulo da
haste em relação à vertical. É uma planta de primeira escolha para ensino por ser
não linear, instável em malha aberta em parte da faixa de operação e de construção
acessível.

A plataforma cobre o ciclo experimental completo: **excitação e aquisição** de dados no
protótipo real, **identificação do modelo** a partir desses dados, **controle em malha
fechada** com PID no firmware, e um **gêmeo digital** que reproduz em 3D, em tempo real, o
movimento medido no protótipo.

## Arquitetura

O sistema é composto por quatro subsistemas que operam de forma integrada:

| Subsistema | Função | Tecnologia |
| --- | --- | --- |
| **Protótipo** | Planta física: haste, motor CC com hélice, potenciômetro como sensor de ângulo, ponte H | Estrutura em madeira e fibra de carbono |
| **Firmware** | Leitura do sensor, controle PID em malha fechada, geração do sinal de referência e comunicação serial | C++ · ESP32 TTGO · PlatformIO |
| **Interface gráfica** | Aquisição em tempo real, visualização dos sinais e registro dos ensaios em CSV | Python · CustomTkinter · PySerial |
| **Gêmeo digital** | Réplica virtual do protótipo: animação tridimensional e gráficos atualizados com o ângulo medido | Python · VPython · Matplotlib |

O firmware e a interface gráfica trocam dados por porta serial: o microcontrolador envia
referência, posição angular, erro, sinal de controle, entrada e tempo; a interface envia
amplitude, frequência e offset do sinal de referência, a forma de onda, o modo de malha e o
comando de execução. Os ganhos do PID são fixos no firmware, definidos em tempo de compilação.

## Metodologia

A obtenção do modelo seguiu a abordagem de **identificação de sistemas** a partir de dados
experimentais, em vez de modelagem exclusivamente analítica:

1. **Excitação** — aplicação de sinal PRBS (*Pseudo-Random Binary Sequence*) na entrada do
   sistema em malha aberta, somado a um offset que mantém a operação em torno do ponto de
   trabalho.
2. **Aquisição** — registro dos pares entrada–saída pela interface gráfica, com divisão do
   ensaio em 60% para identificação e 40% para validação.
3. **Estimação** — ajuste de modelos ARX discretos pelo método dos **mínimos quadrados**; a
   estrutura de 10ª ordem foi a adotada.
4. **Validação** — simulação livre do modelo com a entrada do ensaio e comparação com a
   saída real no trecho de validação.
5. **Controle** — PID no firmware, com ganhos sintonizados por tentativa e erro no protótipo,
   avaliado em malha fechada com referências em onda quadrada e dente de serra.

A dedução analítica do modelo por subsistemas (motor CC série e braço) também está
documentada; a dificuldade de obter numericamente alguns de seus parâmetros é o que motiva a
identificação a partir de dados.

## Estrutura do repositório

```
.
├── brand/                      # Identidade visual (SVG, PNG e scripts geradores)
├── docs/                       # Fonte do site de documentação (MkDocs)
├── docs_tcc/                   # Resumos e índice do projeto para consulta rápida
├── materiais_complementares/   # Bibliografia, estudos de identificação e modelagem
├── revisao_tcc/                # Monografia em LaTeX e versões de revisão
├── softwares_aeropendulo/      # Interface gráfica, gêmeo digital e firmware
└── utils/                      # Figuras e diagramas
```

## Instalação e execução

Requer Python 3.10 ou 3.11. As dependências são gerenciadas por [Poetry](https://python-poetry.org/):

```bash
git clone https://github.com/Oseiasdfarias/lab-virtual.git
cd lab-virtual/softwares_aeropendulo
poetry install
poetry run python rungui.py
```

O firmware está em `softwares_aeropendulo/firmwares_microcontroladores/`. A variante mais
completa é `PlatformIo/Esp32_ttgo_modulos`, organizada em bibliotecas separadas para
controlador PID, conversão de unidades, geração de referência e comunicação serial.
Compilação e gravação pelo PlatformIO:

```bash
cd softwares_aeropendulo/firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos
pio run --target upload
```

O gêmeo digital é opcional (`poetry run python rungui.py -simular sim`) e é alimentado pelos
dados do protótipo: ele reproduz o movimento medido, a partir do ângulo recebido pela serial,
e por isso precisa do protótipo conectado.

## Documentação

A documentação técnica está publicada em
**[oseiasdfarias.github.io/lab-virtual](https://oseiasdfarias.github.io/lab-virtual/)** e
inclui guias de instalação e a referência dos módulos do gêmeo digital. O site é publicado
automaticamente a cada push na `main`; para visualizá-lo localmente:

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Para uma visão consolidada do projeto — resumo por capítulo da monografia, arquitetura do
software, catálogo dos materiais complementares e pendências —, consulte
[`docs_tcc/`](./docs_tcc/), que traz um índice em YAML e resumos em Markdown.

## Publicação

A monografia está publicada em acesso aberto na Biblioteca Digital de Monografias da UFPA:

**[bdm.ufpa.br/handle/prefix/6944](https://bdm.ufpa.br/handle/prefix/6944)** — defendida em
11 de dezembro de 2023.

## Como citar

```bibtex
@mastersthesis{farias2023labvirtual,
  author       = {Farias, Oséias Dias de},
  title        = {Desenvolvimento de protótipo e gêmeo digital como ferramenta para um
                  laboratório virtual com foco em modelagem e controle de sistemas dinâmicos},
  school       = {Universidade Federal do Pará},
  type         = {Trabalho de Conclusão de Curso (Bacharelado em Engenharia Elétrica)},
  address      = {Tucuruí, Brasil},
  year         = {2023},
  url          = {https://bdm.ufpa.br/handle/prefix/6944}
}
```

**Palavras-chave:** aeropêndulo · identificação de sistemas · protótipo · simulador ·
gêmeo digital

## Autoria

Desenvolvido por **Oséias Dias de Farias**, Bacharelado em Engenharia Elétrica da
Faculdade de Engenharia Elétrica — UFPA, Campus Universitário de Tucuruí, sob orientação
do **Prof. Raphael Barros Teixeira**.

<p align="center">
  <img height="34" src="./utils/logos_lg/UFPA-removebg-preview.png" alt="UFPA">
</p>
