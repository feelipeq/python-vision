import io
import os

from google.cloud import vision
from google.cloud.vision import types

import logging
from pygdrive3 import service

logger = logging.getLogger(__name__)


def google_drive_auth():
    try:
        drive_service = service.DriveService("src/secrets/client_secrets.json")
        drive_service.auth()
        logger.info("Autenticação com Sucesso")
    except Exception as e:
        logger.error("Erro ao Autenticar no Drive: ", e)


def get_vision_object(content):
    image = types.Image(content=content)
    return image


def get_vision_instance():
    client = vision.ImageAnnotatorClient()
    return client


def get_vision_labels(client, image):
    try:
        response = client.label_detection(image=image)
        labels = response.label_annotations
        return labels
    except Exception as e:
        logger.error("Erro na Integração com Vision: ", e)


def get_vision_text(client, image):
    try:
        response = client.text_detection(image=image)
        texts = response.text_annotations
        logger.info("Textos gerados com sucesso")
        return texts
    except Exception as e:
        logger.error("Erro na Integração com Vision: ", e)


def get_binary_image(path_image):
    with io.open(path_image, "rb") as image_file:
        content = image_file.read()
    return content


def get_tags_as_string(tags):
    return 0


def convert_struc_to_dict():
    return 0
