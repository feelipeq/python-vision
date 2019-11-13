import imagesvision.image.gcp_integration
import logging

logger=logging.getLogger(__name__)


#google_drive_auth()

content=get_binary_image('/home/osboxes/Downloads/dog.jpg')

client = get_vision_instance(content)

image=get_vision_object(content)

labels=get_vision_labels(client,image)

logger.info(labels,'a')

