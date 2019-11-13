import logging

from imagesvision.image.gcp_integration import (
    get_binary_image,
    get_vision_instance,
    get_vision_object,
    get_vision_labels,
)

from imagesvision.drive.drive_integration import (
    google_drive_auth,
    file_upload
)


logger = logging.getLogger(__name__)

google_drive_auth()

content = get_binary_image("/home/osboxes/Downloads/dog.jpg")

client = get_vision_instance()

image = get_vision_object(content)

labels = get_vision_labels(client, image)

logger.info(labels, "a")

print(labels)