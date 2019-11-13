from pathlib import Path
from simple_settings import settings


def search_file_recursive():
    arquivos = []

    for ext in settings.extensions:
        for filename in Path(settings.folder).rglob(ext):
            if filename != "":
                arquivos.append(filename)
    return arquivos


def get_filename(path_image):
    return path_image.split('/')[-1]