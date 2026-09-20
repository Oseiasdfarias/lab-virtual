# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# Trabalho de Conclusão de Curso - Aeropêndulo
# -----------------------------------------------------
#
# Título : Classe para criar os gráficos da aplicação
# Professor Orientador: Raphael Teixeira
# Autor: Oséias Farias
#
# Data: 2023
#  ----------------------------------------------------
#
from abc import ABC, abstractmethod


class GraficosSinaisInterface(ABC):
    """Contrato dos gráficos de sinais da interface (ver `GraficosSinais`)."""

    @abstractmethod
    def get_fig_axes_ln(self):
        """Retorna a figura, os eixos e as linhas dos gráficos."""

    @abstractmethod
    def config_axes(self) -> None:
        """Configura títulos, limites e grades dos eixos."""
