---
title: Simulador
---

# Simulador

Liga a animação 3D e os gráficos do gêmeo digital aos dados recebidos pela interface. A cada
chamada de `atualizar_estados(t, theta, ref)`, converte o ângulo medido para radianos,
calcula a variação desde a amostra anterior, gira o modelo 3D e a hélice de acordo e
acrescenta o ângulo e a referência aos gráficos.

::: softwares_aeropendulo.simulador_aeropendulo.simulador.Simulador
    handler: python
    options:
        members:
            - __init__
            - grau2rad
            - rotate
            - atualizar_estados
        show_root_heading: false
        show_source: true
        heading_level: 2
