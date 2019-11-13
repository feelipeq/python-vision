import os
import io
import json
from ast import literal_eval


def get_tags_as_string(tags):
    text_tags = ""
    for t in tags:
        text_tags += t+'\n'
    return text_tags


def format_dict_response(path_image, labels, texts):
    response = {}
    labels_dict={}
    labels_dict_str=""
    labels_list=[]
    cont=0
    for l in labels:
        labels_dict=({'tagname' : str(l), 'label_score' : labels[l]})
        if cont!=len(labels)-1:
            labels_dict_str+=str(labels_dict)+','
            labels_list.append(str(l))
            cont+=1
        else:
            labels_dict_str+=str(labels_dict)
            labels_list.append(str(l))

    labels_dict=literal_eval(labels_dict_str)
    response.update({"caminho_imagem": path_image})
    response.update({"tags": labels_dict})
    response.update({"tag_list": labels_list})
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
    response.update({'timestamp' : timestamp })
    json_str = json.dumps(response, ensure_ascii=False, indent=4).encode('utf-8')
    json_str = json_str.decode()
    return json_str
