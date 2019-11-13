import logging
from . import service
from simple_settings import settings

logger = logging.getLogger(__name__)


def google_drive_auth():
    try:
        drive_service = service.DriveService("/home/osboxes/secrets/client_secrets_2.json")
        drive_service.auth()
        logger.info("Autenticação com Sucesso")
        return drive_service
    except Exception as e:
        logger.error("Erro ao Autenticar no Drive: ", e)


def file_upload(drive_service,file_name, path_file, folder_id, tags):
    try:
        drive_service.upload_file(file_name,path_file,folder_id,tags)
        return True
    except Exception as e:
        logger.error("Falha ao fazer upload no Drive")
        return False

