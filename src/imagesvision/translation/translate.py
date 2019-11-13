from core import translate
from simple_settings import settings


def get_translation(word):
    translated = translate(str(word), settings.LANG, "auto")
    return translated
