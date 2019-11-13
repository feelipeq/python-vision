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
    update_dict_with_response_time,
    json_format_to_es
)

from imagesvision.image.search_images import (
    get_filename,
    search_file_recursive
)

from imagesvision.date.datetime import(
    get_current_timestamp_formated
)

from imagesvision.monitoring.esmonitoring import (
    send_to_es,
    initiate_es
)


import time

logger = logging.getLogger(__name__)
extensions=['*.jpg','*.jpeg','*.png']
search_folder="/home/osboxes/Pictures"
folder_id='161pryZMzKGWawRZ2wV5qStfuK0R_OIcq'

files=search_file_recursive(extensions,search_folder)

for path_image in files:

    start=time.time()
    content = get_binary_image(path_image)
    client = get_vision_instance()
    image = get_vision_object(content)
    labels = get_vision_labels(client, image)
    texts = get_vision_text(client, image)
    labels = translate_google_labels(labels)
    response = format_dict_response(path_image, labels, texts)
    vision_time=time.time() - start


    start=time.time()
    drive_service = google_drive_auth()
    file_name=get_filename(path_image)
    tags = get_tags_as_string(labels)
    tags+=str(texts)
    file_upload(drive_service, file_name, path_image, folder_id, tags)
    drive_time=time.time() - start

    response=update_dict_with_response_time(response,vision_time,drive_time)

    logger.info(response)

    timestamp=get_current_timestamp_formated()

    json_response=json_format_to_es(response,timestamp)
    elastic = initiate_es()
    send_to_es(json_response,elastic)

    #print(drive_service, file_name, path_image, folder_id, tags)
