from pathlib import Path
from simple_settings import settings


def busca_imagens_recursivas():
    arquivos = []

    for ext in settings.extensions:
        for filename in Path(settings.folder).rglob(ext):
            if filename != "":
                arquivos.append(filename)
    return arquivos
