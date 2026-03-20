import os
import sys

def resource_path(relative_path):
    """ Retorna o caminho absoluto para o recurso, compatível com PyInstaller """
    try:
        # PyInstaller cria uma pasta temp e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
