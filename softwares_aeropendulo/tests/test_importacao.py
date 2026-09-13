"""Os módulos usados pelo rungui.py importam com as dependências fixadas no poetry.lock."""

import importlib

import pytest


@pytest.mark.parametrize(
    "modulo",
    [
        "src_interface.coleta_dados",
        "src_interface.graficos_sinais",
        "src_interface.interface_grafica",
        "src_interface.lista_portas_usb",
        "simulador_aeropendulo.simulador",
        "simulador_aeropendulo.animacao_aeropendulo",
        "simulador_aeropendulo.graficos_aeropendulo",
        "rungui",
    ],
)
def test_importa(modulo):
    importlib.import_module(modulo)
