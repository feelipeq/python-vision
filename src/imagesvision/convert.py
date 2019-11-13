import os
import io
import json


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

def update_dict_with_response_time(response,vision_time,drive_time):
    response.update({'tempo_vision': round(vision_time,2)})
    response.update({'tempo_drive': round(drive_time,2)})
    total_time=vision_time+drive_time
    response.update({'tempo_total_transacao': total_time})
    return response

def json_format_to_es(response, timestamp):
    json_str = json.dumps(response, ensure_ascii=False, indent=4).encode('utf-8')
    json_str = json_str.decode()
    return json_str