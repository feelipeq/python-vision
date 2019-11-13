import logging

from imagesvision.image.gcp_integration import (
    get_binary_image,
    get_vision_instance,
    get_vision_object,
    get_vision_labels,
    get_vision_text
)

from imagesvision.drive.drive_integration import (
    google_drive_auth,
    file_upload
)

from imagesvision.translation.translate import (
    translate_google_labels
)

from imagesvision.convert import (
    get_tags_as_string,
    format_dict_response
)


logger = logging.getLogger(__name__)

#google_drive_auth()

path_image="/home/osboxes/Downloads/dog.jpg"

content = get_binary_image("/home/osboxes/Downloads/dog.jpg")

client = get_vision_instance()

image = get_vision_object(content)

labels = get_vision_labels(client, image)

texts = get_vision_text(client,image)

labels=translate_google_labels(labels)

response=format_dict_response(path_image,labels,texts)


print(response)