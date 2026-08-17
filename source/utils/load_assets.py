import sys
import os

def obter_caminho_recurso(caminho_relativo):
    if getattr(sys, 'frozen', False):
        # Executável compilado com cx_Freeze
        base_path = os.path.dirname(sys.executable)
    else:
        # Modo desenvolvimento (.py)
        base_path = os.path.abspath(".")
    return os.path.join(base_path, caminho_relativo)

# Exemplo de uso no seu programa:
#caminho_logo = obter_caminho_recurso("assets/logo.png")
#caminho_banco = obter_caminho_recurso("banco.db")