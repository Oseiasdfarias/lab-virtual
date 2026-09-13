// Diagrama interativo da arquitetura na página Início (D3).
// Os textos resumem docs/visao-geral/arquitetura.md, software/firmware.md e
// software/interface-grafica.md; os números vêm do main.cpp e do protocolo serial.
(function () {
  "use strict";

  const raiz = document.querySelector("[data-lv-arq]");
  if (!raiz || typeof d3 === "undefined") return;

  const canvas = raiz.querySelector("[data-lv-arq-canvas]");
  const painel = raiz.querySelector("[data-lv-arq-panel]");
  const semMovimento = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const NOS = [
    {
      id: "prototipo",
      titulo: "Protótipo",
      sub: "haste · motor · hélice",
      texto:
        "A planta física: uma haste articulada num pivô, com motor CC série e hélice na ponta. " +
        "O empuxo ergue a haste, e um potenciômetro no pivô mede o ângulo.",
      fatos: [
        "Estrutura em compensado e fibra de carbono",
        "Ponte H (driver L298N) acionando o motor",
        "Potenciômetro como sensor de ângulo",
      ],
      link: "prototipo/",
    },
    {
      id: "firmware",
      titulo: "Firmware",
      sub: "ESP32 · C++",
      texto:
        "Roda no ESP32 e fecha a malha sozinho: lê o ângulo, gera a referência (ou o PRBS em " +
        "malha aberta), calcula o PID e aciona o motor por PWM.",
      fatos: [
        "Período de amostragem de 20 ms",
        "PID com Kp 0,02 · Ki 0,055 · Kd 0,35, fixos no código",
        "PWM de 500 Hz com 8 bits de resolução",
      ],
      link: "software/firmware/",
    },
    {
      id: "interface",
      titulo: "Interface gráfica",
      sub: "Python · CustomTkinter",
      texto:
        "Aplicação em Python que conversa com o firmware pela serial, plota os sinais em tempo " +
        "real e grava cada ensaio para a identificação.",
      fatos: [
        "Serial a 115200 baud via PySerial",
        "Gráficos em tempo real com Matplotlib",
        "Ensaios salvos em CSV com Pandas",
      ],
      link: "software/interface-grafica/",
    },
    {
      id: "gemeo",
      titulo: "Gêmeo digital",
      sub: "VPython · 3D",
      texto:
        "Réplica 3D do aeropêndulo que acompanha o protótipo: recebe o ângulo medido e " +
        "reproduz o movimento na tela, junto com os gráficos de ângulo e referência.",
      fatos: [
        "Animação 3D com VPython",
        "Mesmo processo Python da interface",
        "Opcional: python rungui.py -simular sim",
      ],
      link: "gemeo-digital/",
    },
  ];

  const ARESTAS = [
    { de: "prototipo", para: "firmware", rotulo: "ângulo (A/D)", curva: -1 },
    { de: "firmware", para: "prototipo", rotulo: "PWM → ponte H", curva: -1 },
    { de: "firmware", para: "interface", rotulo: "7 valores por amostra", curva: -1 },
    { de: "interface", para: "firmware", rotulo: "configuração", curva: -1, config: true },
    { de: "interface", para: "gemeo", rotulo: "chamada de método", curva: 0 },
  ];

  const LAYOUTS = {
    largo: {
      largura: 820,
      altura: 400,
      no: { w: 180, h: 86 },
      pos: { prototipo: [96, 200], firmware: [410, 200], interface: [724, 76], gemeo: [724, 324] },
    },
    estreito: {
      largura: 360,
      altura: 820,
      no: { w: 220, h: 84 },
      pos: { prototipo: [180, 60], firmware: [180, 320], interface: [180, 580], gemeo: [180, 770] },
    },
  };

  let selecionado = "firmware";
  let modoAtual = null;
  const idAnimacao = { valor: 0 };

  function porId(id) {
    return NOS.find((n) => n.id === id);
  }

  function pontoNaBorda(centro, alvo, meia) {
    const dx = alvo[0] - centro[0];
    const dy = alvo[1] - centro[1];
    const escala = Math.min(meia.w / Math.abs(dx || 1e-6), meia.h / Math.abs(dy || 1e-6));
    return [centro[0] + dx * escala, centro[1] + dy * escala];
  }

  function caminho(aresta, layout) {
    const a = layout.pos[aresta.de];
    const b = layout.pos[aresta.para];
    const meia = { w: layout.no.w / 2 + 6, h: layout.no.h / 2 + 6 };
    const dx = b[0] - a[0];
    const dy = b[1] - a[1];
    const dist = Math.hypot(dx, dy);
    const nx = -dy / dist;
    const ny = dx / dist;
    const desvio = aresta.curva * Math.min(62, dist * 0.26);
    const controle = [(a[0] + b[0]) / 2 + nx * desvio, (a[1] + b[1]) / 2 + ny * desvio];
    const inicio = pontoNaBorda(a, controle, meia);
    const fim = pontoNaBorda(b, controle, meia);
    const meio = [
      0.25 * inicio[0] + 0.5 * controle[0] + 0.25 * fim[0],
      0.25 * inicio[1] + 0.5 * controle[1] + 0.25 * fim[1],
    ];
    // Rótulo afastado da curva, para o lado para onde ela se curva; em ligações retas, fica sobre a linha.
    const lado = Math.sign(desvio);
    const ox = nx * lado;
    const oy = ny * lado;
    let ancora = "middle";
    let pos = meio;
    if (lado !== 0) {
      pos = [meio[0] + ox * 10, meio[1] + oy * 12];
      if (Math.abs(ox) > Math.abs(oy)) ancora = ox > 0 ? "start" : "end";
    }
    return {
      d: `M${inicio[0]},${inicio[1]} Q${controle[0]},${controle[1]} ${fim[0]},${fim[1]}`,
      meio: pos,
      ancora,
    };
  }

  function desenhar() {
    const modo = canvas.clientWidth < 560 ? "estreito" : "largo";
    if (modo === modoAtual) return;
    modoAtual = modo;
    idAnimacao.valor += 1;
    const layout = LAYOUTS[modo];

    d3.select(canvas).selectAll("*").remove();
    const svg = d3
      .select(canvas)
      .append("svg")
      .attr("viewBox", `0 0 ${layout.largura} ${layout.altura}`)
      .attr("role", "presentation");

    svg
      .append("defs")
      .append("marker")
      .attr("id", "lv-arq-seta")
      .attr("viewBox", "0 0 10 10")
      .attr("refX", 9)
      .attr("refY", 5)
      .attr("markerWidth", 7)
      .attr("markerHeight", 7)
      .attr("orient", "auto-start-reverse")
      .append("path")
      .attr("d", "M0,0 L10,5 L0,10 z")
      .attr("class", "lv-arq-seta")
      .style("fill", "var(--lv-faint)");

    const dados = ARESTAS.map((a) => ({ ...a, ...caminho(a, layout) }));

    const grupoArestas = svg.append("g");
    const linhas = grupoArestas
      .selectAll("path")
      .data(dados)
      .join("path")
      .attr("class", (a) => "lv-arq-edge" + (a.config ? " lv-arq-edge--config" : ""))
      .attr("d", (a) => a.d)
      .attr("marker-end", "url(#lv-arq-seta)");

    const rotulos = svg
      .append("g")
      .selectAll("g")
      .data(dados)
      .join("g")
      .attr("class", "lv-arq-edge-label")
      .attr("transform", (a) => `translate(${a.meio[0]},${a.meio[1]})`);
    rotulos
      .append("text")
      .attr("text-anchor", (a) => a.ancora)
      .attr("dominant-baseline", "central")
      .text((a) => a.rotulo);
    rotulos.each(function () {
      const caixa = this.querySelector("text").getBBox();
      d3.select(this)
        .insert("rect", "text")
        .attr("x", caixa.x - 6)
        .attr("y", caixa.y - 3)
        .attr("width", caixa.width + 12)
        .attr("height", caixa.height + 6)
        .attr("rx", 6);
    });

    const nos = svg
      .append("g")
      .selectAll("g")
      .data(NOS)
      .join("g")
      .attr("class", "lv-arq-node")
      .attr("tabindex", 0)
      .attr("role", "button")
      .attr("aria-label", (n) => `${n.titulo}: ver detalhes`)
      .attr("transform", (n) => `translate(${layout.pos[n.id][0]},${layout.pos[n.id][1]})`)
      .on("click", (_, n) => selecionar(n.id))
      .on("keydown", (evento, n) => {
        if (evento.key === "Enter" || evento.key === " ") {
          evento.preventDefault();
          selecionar(n.id);
        }
      });

    nos
      .append("rect")
      .attr("x", -layout.no.w / 2)
      .attr("y", -layout.no.h / 2)
      .attr("width", layout.no.w)
      .attr("height", layout.no.h)
      .attr("rx", 14);
    nos
      .append("text")
      .attr("class", "lv-arq-node__title")
      .attr("text-anchor", "middle")
      .attr("y", -4)
      .text((n) => n.titulo);
    nos
      .append("text")
      .attr("class", "lv-arq-node__sub")
      .attr("text-anchor", "middle")
      .attr("y", 18)
      .text((n) => n.sub);

    marcarSelecionado();
    if (!semMovimento) animarPulsos(svg, linhas, idAnimacao.valor);
  }

  function animarPulsos(svg, linhas, id) {
    const grupo = svg.append("g").attr("pointer-events", "none");
    linhas.each(function (_, i) {
      const trajeto = this;
      const comprimento = trajeto.getTotalLength();
      const duracao = 1600 + comprimento * 5;
      const ponto = grupo.append("circle").attr("class", "lv-arq-dot").attr("r", 4);

      function ciclo() {
        if (id !== idAnimacao.valor) return;
        ponto
          .attr("opacity", 0)
          .transition()
          .delay(i * 280)
          .duration(duracao)
          .ease(d3.easeCubicInOut)
          .attrTween("transform", () => (t) => {
            const p = trajeto.getPointAtLength(t * comprimento);
            return `translate(${p.x},${p.y})`;
          })
          .attrTween("opacity", () => (t) => String(Math.min(1, Math.min(t, 1 - t) * 8)))
          .on("end", ciclo);
      }
      ciclo();
    });
  }

  function marcarSelecionado() {
    d3.select(canvas)
      .selectAll(".lv-arq-node")
      .classed("is-selected", (n) => n.id === selecionado)
      .attr("aria-pressed", (n) => String(n.id === selecionado));
  }

  function selecionar(id) {
    selecionado = id;
    marcarSelecionado();
    preencherPainel();
  }

  function preencherPainel() {
    const n = porId(selecionado);
    const p = d3.select(painel);
    p.selectAll("*").remove();
    p.append("p").attr("class", "lv-home-eyebrow").text("Subsistema");
    p.append("h3").text(n.titulo);
    p.append("p").text(n.texto);
    p.append("ul").selectAll("li").data(n.fatos).join("li").text((f) => f);
    p.append("a").attr("class", "lv-btn").attr("href", n.link).text("Ver documentação →");
  }

  preencherPainel();
  desenhar();
  let espera;
  new ResizeObserver(() => {
    clearTimeout(espera);
    espera = setTimeout(desenhar, 120);
  }).observe(canvas);
})();
