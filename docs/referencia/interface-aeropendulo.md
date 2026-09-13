---
title: InterfaceAeropendulo
---

# InterfaceAeropendulo

Janela principal da interface gráfica, construída com CustomTkinter. Reúne a seleção da
porta USB, os campos de amplitude, frequência e offset, os seletores de forma de onda e de
malha, o botão de gravação dos dados e os gráficos em tempo real; quando recebe um
`Simulador`, repassa a ele cada nova amostra.

::: softwares_aeropendulo.src_interface.interface_grafica.InterfaceAeropendulo
    handler: python
    options:
        members:
            - __init__
            - atualizar_simulador
            - quit
            - set_usb_port
            - aparencia_event
            - init
            - update
            - run_graph
            - switch_event_den_serra
            - switch_event_seno
            - switch_event_quad
            - switch_event_mamb
            - switch_event_sdados
            - get_data_emtry_ampl1
            - get_data_emtry_freq1
            - get_data_emtry_offset1
            - start_gui
        show_root_heading: false
        show_source: true
        heading_level: 2
