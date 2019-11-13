from .core import translate
from simple_settings import settings


def get_translation(word):
    translated = translate(str(word), settings.LANG, "auto")
    return translated


def translate_google_labels(labels):
    label_pt_br=""
    labels_pt={}
    for label in labels:
        label_pt_br=translate(str(label.description),"pt-br","auto")
        labels_pt.update({ label_pt_br : round(label.score,3) })
    return labels_pt