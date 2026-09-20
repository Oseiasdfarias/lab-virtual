# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# Trabalho de Conclusão de Curso - Aeropêndulo
# -----------------------------------------------------
#
# Título : Classe para listagem de Portas USB Disponíveis
# Professor Orientador: Raphael Teixeira
# Autor: Oséias Farias
#
# Data: 2023
#  ----------------------------------------------------
#

from abc import ABC, abstractmethod


class ListaPortasUsb(ABC):
    """Contrato da listagem de portas USB (ver `lista_portas_usb.ListaPortasUsb`)."""

    @abstractmethod
    def listar_portas_usb(self):
        """Retorna as portas seriais disponíveis."""

    @abstractmethod
    def atualizar_dados_menu(self):
        """Atualiza o menu de portas da interface."""
