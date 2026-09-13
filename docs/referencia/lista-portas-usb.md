---
title: ListaPortasUsb
---

# ListaPortasUsb

Lista as portas seriais disponíveis e monitora, numa thread com `pyudev`, a conexão e a
desconexão de dispositivos USB, atualizando o menu de portas da interface.

::: softwares_aeropendulo.src_interface.lista_portas_usb.ListaPortasUsb
    handler: python
    options:
        members:
            - __init__
            - listar_portas_usb
            - atualizar_dados_menu
        show_root_heading: false
        show_source: true
        heading_level: 2
