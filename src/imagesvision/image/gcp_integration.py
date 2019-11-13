from google.cloud import vision
from google.cloud.vision import types

import logging
from pygdrive3 import service

logger = logging.getLogger(__name__)


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
        logger.info("Labels gerados com sucesso")
        return labels
    except Exception as e:
        logger.error("Erro na Integração com Vision: ", e)


def get_vision_text(client, image):
    try:
        response = client.text_detection(image=image)
        texts = response.text_annotations
        logger.info("Textos gerados com sucesso")
        for text in texts:
            return text.description
        # return texts
    except Exception as e:
        logger.error("Erro na Integração com Vision: ", e)
