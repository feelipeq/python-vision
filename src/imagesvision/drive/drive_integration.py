import logging
from . import service
from simple_settings import settings

logger = logging.getLogger(__name__)

def google_drive_auth():
    try:
        drive_service = service.DriveService(settings.DRIVE_SECRET)
        drive_service.auth()
        logger.info("Autenticação com Sucesso")
    except Exception as e:
        logger.error("Erro ao Autenticar no Drive: ", e)

def file_upload():
    return 0