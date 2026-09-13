---
title: ColetaDados
---

# ColetaDados

Cuida da comunicação serial com o firmware: lê as amostras numa thread separada, mantém a
janela de dados exibida nos gráficos, codifica e envia os parâmetros de configuração
(ver [Protocolo serial](../software/firmware.md#protocolo-serial)) e grava o ensaio em CSV.

!!! note "Observação"
    O construtor muda o diretório de trabalho para `src_interface` (`os.chdir`), por isso o
    `rungui.py` precisa ser executado a partir da pasta `softwares_aeropendulo`.

::: softwares_aeropendulo.src_interface.coleta_dados.ColetaDados
    handler: python
    options:
        members:
            - __init__
            - get_dados
            - set_amplitude
            - set_frequencia
            - set_offset
            - set_sinal
            - listar_dir
            - salvar_dados_colhidos
            - reconectar
        show_root_heading: false
        show_source: true
        heading_level: 2
