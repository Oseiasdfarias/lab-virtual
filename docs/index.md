---
title: Início
hide:
  - navigation
  - toc
---

<div class="lv-home">

<section class="lv-home-hero" aria-labelledby="lv-home-title">
  <div class="lv-home-hero__text">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 163.14 163.14" class="lv-home-mark" aria-hidden="true" focusable="false">
      <line x1="26.71" y1="36.04" x2="26.71" y2="136.04" stroke="currentColor" stroke-width="3.57" stroke-dasharray="7.14 7.14" stroke-linecap="butt" opacity="0.3"/>
      <line x1="26.71" y1="36.04" x2="103.32" y2="100.31" stroke="currentColor" stroke-width="8.93" stroke-linecap="round"/>
      <line x1="103.32" y1="100.31" x2="121.68" y2="78.43" stroke="currentColor" stroke-width="16.07" stroke-linecap="round"/>
      <line x1="99.80" y1="60.06" x2="143.57" y2="96.79" stroke="currentColor" stroke-width="7.14" stroke-linecap="round"/>
      <circle cx="26.71" cy="36.04" r="10.71" fill="currentColor"/>
      <path d="M 33.18 82.01 A 46.43 46.43 0 0 0 58.97 69.43" fill="none" stroke="currentColor" stroke-width="4.46" stroke-linecap="round" opacity="0.7"/>
      <polygon points="0,-6.43 14.29,0 0,6.43" fill="currentColor" opacity="0.7" stroke="currentColor" stroke-width="0.00" stroke-linejoin="round" transform="translate(58.97 69.43) rotate(-46.00)"/>
    </svg>
    <p class="lv-home-eyebrow">Plataforma didática · Sistemas dinâmicos e controle</p>
    <h1 id="lv-home-title">Laboratório Virtual</h1>
    <p class="lv-home-lead">Protótipo, gêmeo digital e identificação de sistemas aplicados a um
    aeropêndulo — um mapa completo do desenvolvimento, da física ao código.</p>
    <div class="lv-home-actions">
      <a class="lv-btn lv-btn--primary" href="visao-geral/">Explorar o laboratório</a>
      <a class="lv-btn" href="https://github.com/Oseiasdfarias/lab-virtual" target="_blank" rel="noopener">Código no GitHub</a>
    </div>
  </div>
  <figure class="lv-home-hero__visual">
    <div class="lv-hero3d">
      <iframe src="assets/simulador/aeropendulo_3d.html?min=1" style="width: 100%; height: 100%; border: none;" title="Gêmeo Digital 3D do Aeropêndulo"></iframe>
    </div>
    <figcaption>Arraste para orbitar, use o scroll para zoom. O modelo 3D mecatrônico reproduz o protótipo real com base naval, mastro, potenciômetro de precisão e eletrônica embarcada. Veja mais em <a href="gemeo-digital/">Gêmeo Digital</a>.</figcaption>
  </figure>
</section>

<section class="lv-home-stats" aria-label="O laboratório em números">
  <div class="lv-stat"><strong>4</strong><span>subsistemas integrados</span></div>
  <div class="lv-stat"><strong>20 ms</strong><span>período de amostragem do controle</span></div>
  <div class="lv-stat"><strong>7</strong><span>sinais enviados pela serial a cada amostra</span></div>
  <div class="lv-stat"><strong>78,3%</strong><span>ajuste NRMSE do modelo ARX de 10ª ordem —
  <a href="identificacao/validacao/">análise posterior à monografia</a></span></div>
</section>

<section class="lv-home-section" aria-labelledby="lv-home-arq">
  <header class="lv-home-section__head">
    <p class="lv-home-eyebrow">Arquitetura</p>
    <h2 id="lv-home-arq">Como o laboratório funciona</h2>
    <p>Quatro subsistemas trocam dados continuamente. Selecione um bloco para ver o que ele faz
    e seguir para a documentação completa.</p>
  </header>
  <div class="lv-arq" data-lv-arq>
    <div class="lv-arq__canvas" data-lv-arq-canvas role="group" aria-label="Diagrama da arquitetura"></div>
    <aside class="lv-arq__panel" data-lv-arq-panel aria-live="polite"></aside>
  </div>
  <noscript><p>O diagrama interativo precisa de JavaScript. A mesma informação está em
  <a href="visao-geral/arquitetura/">Arquitetura do sistema</a>.</p></noscript>
</section>

<section class="lv-home-section" aria-labelledby="lv-home-fluxo">
  <header class="lv-home-section__head">
    <p class="lv-home-eyebrow">Metodologia</p>
    <h2 id="lv-home-fluxo">Do ensaio ao controle</h2>
    <p>A documentação segue o mesmo ciclo experimental do desenvolvimento.</p>
  </header>
  <ol class="lv-timeline">
    <li class="lv-timeline__step">
      <span class="lv-timeline__num">01</span>
      <h3>Protótipo</h3>
      <p>Haste articulada, motor CC série com hélice e potenciômetro medindo o ângulo.</p>
      <a href="prototipo/">Ver protótipo →</a>
    </li>
    <li class="lv-timeline__step">
      <span class="lv-timeline__num">02</span>
      <h3>Modelagem</h3>
      <p>Equações da física, linearização e a função de transferência do braço.</p>
      <a href="modelagem/">Ver modelagem →</a>
    </li>
    <li class="lv-timeline__step">
      <span class="lv-timeline__num">03</span>
      <h3>Identificação</h3>
      <p>Ensaio PRBS em malha aberta e modelo ARX estimado por mínimos quadrados.</p>
      <a href="identificacao/excitacao/">Ver identificação →</a>
    </li>
    <li class="lv-timeline__step">
      <span class="lv-timeline__num">04</span>
      <h3>Controle</h3>
      <p>PID no ESP32, com ganhos sintonizados no protótipo e ensaios em malha fechada.</p>
      <a href="controle/pid/">Ver controle →</a>
    </li>
    <li class="lv-timeline__step">
      <span class="lv-timeline__num">05</span>
      <h3>Gêmeo digital</h3>
      <p>Réplica 3D que acompanha, em tempo real, o movimento medido no protótipo.</p>
      <a href="gemeo-digital/">Ver gêmeo digital →</a>
    </li>
  </ol>
</section>

<section class="lv-home-section" aria-labelledby="lv-home-comece">
  <header class="lv-home-section__head">
    <p class="lv-home-eyebrow">Por onde começar</p>
    <h2 id="lv-home-comece">Comece por aqui</h2>
  </header>
  <div class="lv-paths">
    <a class="lv-path" href="visao-geral/">
      <span class="lv-path__q">Quer uma visão rápida?</span>
      <span class="lv-path__a">O que é o Laboratório Virtual →</span>
    </a>
    <a class="lv-path" href="modelagem/">
      <span class="lv-path__q">Quer aprender o processo científico?</span>
      <span class="lv-path__a">Modelagem → Identificação → Controle →</span>
    </a>
    <a class="lv-path" href="prototipo/">
      <span class="lv-path__q">Quer reproduzir ou modificar o hardware/software?</span>
      <span class="lv-path__a">Protótipo e Software →</span>
    </a>
  </div>
</section>

<section class="lv-home-section" aria-labelledby="lv-home-demo">
  <header class="lv-home-section__head">
    <p class="lv-home-eyebrow">Em funcionamento</p>
    <h2 id="lv-home-demo">Demonstração</h2>
  </header>
  <div class="lv-video">
    <iframe src="https://player.vimeo.com/video/893039111?h=80089a63c1&amp;autoplay=1&amp;loop=1&amp;muted=1" title="Demonstração do Laboratório Virtual" loading="lazy" allow="autoplay; fullscreen; picture-in-picture"></iframe>
  </div>
</section>

<section class="lv-home-section lv-home-about" aria-labelledby="lv-home-sobre">
  <div class="lv-home-about__text">
    <p class="lv-home-eyebrow">Origem</p>
    <h2 id="lv-home-sobre">Sobre o projeto</h2>
    <p>Esse projeto surgiu do desenvolvimento de um <strong>trabalho de conclusão de curso</strong>, intitulado, <strong>Desenvolvimento de Protótipo e Gêmeo Digital como Ferramenta para um Laboratório Virtual com Foco em Modelagem e Controle de Sistemas Dinâmicos</strong>, desenvolvido na <strong>Universidade Federal do Pará</strong> no <strong>Campus de Tucuruí</strong>, pelo discente da <strong>Faculdade de Engenharia Elétrica</strong>, <strong>Oséias Farias</strong>.</p>
  </div>
  <div class="lv-team">
    <a class="lv-person" href="https://github.com/Oseiasdfarias" target="_blank" rel="noopener">
      <img src="https://avatars.githubusercontent.com/u/52744236" alt="" width="64" height="64" loading="lazy">
      <span><strong>Oséias Farias</strong><small>Autor</small></span>
    </a>
    <a class="lv-person" href="https://github.com/raphateixeira" target="_blank" rel="noopener">
      <img src="https://avatars.githubusercontent.com/u/13009893?v=4" alt="" width="64" height="64" loading="lazy">
      <span><strong>Raphael Teixeira</strong><small>Orientador</small></span>
    </a>
  </div>
</section>

</div>

<script src="javascripts/vendor/d3/d3.min.js" defer></script>
<script src="javascripts/home/arquitetura.js" defer></script>
