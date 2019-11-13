import logging

from imagesvision.image.gcp_integration import (
    get_vision_instance,
    get_vision_object,
    get_vision_labels,
    get_vision_text,
)

from imagesvision.drive.drive_integration import google_drive_auth, file_upload

from imagesvision.translation.translate import translate_google_labels

from imagesvision.convert import (
    get_binary_image,
    get_tags_as_string,
    format_dict_response,
)

from imagesvision.image.search_images import (
    get_filename,
    search_file_recursive
)

logger = logging.getLogger(__name__)

# google_drive_auth()

path_image = "/home/osboxes/Downloads/dog.jpg"

content = get_binary_image(path_image)

client = get_vision_instance()

image = get_vision_object(content)

labels = get_vision_labels(client, image)

texts = get_vision_text(client, image)

labels = translate_google_labels(labels)

response = format_dict_response(path_image, labels, texts)

drive_service = google_drive_auth()

folder_id='161pryZMzKGWawRZ2wV5qStfuK0R_OIcq'

file_name=get_filename(path_image)

tags = get_tags_as_string(labels)

file_upload(drive_service, file_name, path_image, folder_id, tags)


#print(response)

#print(drive_service, file_name, path_image, folder_id, tags)
