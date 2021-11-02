"""
Biblioteca -> chama_interface
    Interface(Biblioteca) -> metodo_interface
        metodo_da_interface

main -> 00-Interface
"""

from interface import Interface

i1 = Interface()
i1.chama_metodo_da_interface()  # classe pai chama classe filho.
i1.outro_metodo_da_interface()  # classe filho sendo chamado.
