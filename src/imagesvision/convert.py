import os
import io


def get_tags_as_string(tags):
    text_tags = ""
    for t in tags:
        text_tags += t+'\n'
    return text_tags


def format_dict_response(path_image, labels, texts):
    response = {}
    response.update({"caminho_imagem": path_image})
    response.update({"tags": [labels]})
    response.update({"texto": str(texts)})
    return response


def get_binary_image(path_image):
    with io.open(path_image, "rb") as image_file:
        content = image_file.read()
    return content
