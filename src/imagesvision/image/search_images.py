from pathlib import Path


def search_file_recursive(extensions,folder):
    files = []

    for ext in extensions:
        for filename in Path(folder).rglob(ext):
            if filename != "":
                files.append(str(filename))
    return files


def get_filename(path_image):
    return path_image.split('/')[-1].split('.')[0]