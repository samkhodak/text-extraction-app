"""
This file contains all the functions for each main app feature from GCP's ML libraries (Vision, Translate)
"""

from google.cloud import vision, translate
from utilities.constants import SUPPORTED_LANGUAGES
import string
import traceback
import logging
import os, requests

def romanize_text(text: str):
    """
    Receives extracted text and romanizes it, assuming the text is able to be romanized.
    :param text: str
    :return: dictionary including romanized text and detected language.
    """

    # Request service account access token from GCP metadata service
    access_token = get_service_access_token()

    # With the access token, make a POST request to the romanization REST API.
    project_id = os.getenv("PROJECT_ID")
    romanization_url = f"https://translation.googleapis.com/v3/projects/{project_id}/locations/us-central1:romanizeText"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    text_content = {
        "contents": text
    }
    # Make post request and raise exception if API returns a bad status code.
    response = requests.post(romanization_url, headers=headers, json=text_content)
    response.raise_for_status() 
    logging.info(response)

    response_dict = response.json().get("romanizations")
    logging.info(response_dict)

    if (not response_dict):
        raise ValueError("The program was not able to romanize the language of the text in the image. Please try a different image.")

    # As of now, the API only returns one text in its list, so we use [0].
    romanized_text = response_dict[0].get("romanizedText")
    detected_lang_code = response_dict[0].get("detectedLanguageCode")
    supported_languages = SUPPORTED_LANGUAGES
    lang_name = [lang["name"] for lang in supported_languages if lang["code"] == detected_lang_code]

    return dict(
        romanized_text=romanized_text, 
        detected_lang_code=detected_lang_code,
        detected_lang_name=lang_name[0],
    )


def get_service_access_token():
    """
    Retrieves an hour-long access token for the default service account from GCP's metadata service.
    :return: access token string
    """

    auth_url = "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token"
    auth_headers = {
        "Metadata-Flavor": "Google",
    }
    token = requests.get(auth_url, headers=auth_headers)
    token_dict = token.json()
    access_token = token_dict.get("access_token")
    if (not access_token):
        raise PermissionError("Access token for service account was not found in response from Google metadata service.")

    return access_token


def auto_translate_text(text: str, language_code: str):
    """
    Receives extracted text and translates it to the target language using 
    translate API's auto language detection.
    :param text: str
    :param language_code: str
    :return: dictionary including translated text and detected language.
    """
    project_id = os.getenv("PROJECT_ID")
    project_parent = f"projects/{project_id}/locations/us-central1"

    translate_client = translate.TranslationServiceClient()
    result = translate_client.translate_text(
        request={
            "parent": project_parent,
            "contents": [text],
            "mime_type": "text/plain",
            "target_language_code": language_code,
        }
    ).translations

    supported_languages = SUPPORTED_LANGUAGES
    detected_lang_code = result[0].detected_language_code
    translated_text = result[0].translated_text
    lang_name = [lang["name"] for lang in supported_languages if lang["code"] == detected_lang_code]
    
    # It's alright to use result[0] since we don't support more than one string passed to the translation.
    return dict(
        translated_text = translated_text,
        detected_lang_code = detected_lang_code,
        detected_lang_name = lang_name[0],
    )




def detect_main_language(text: str):
    """
    Detects what language a piece of text is mainly in, in order to send to translation.
    :param text: str
    :return: list of top language codes
    """
    project_id = os.getenv("PROJECT_ID")
    location = os.getenv("LOCATION")
    project_parent = f"projects/{project_id}/locations/{location}"

    try:
        translate_client = translate.TranslationServiceClient()
        detected_languages = translate_client.detect_language(
            content=text,
            parent=project_parent,
            mime_type="text/plain",
        ).languages

        return [lang.language_code for lang in detected_languages]


    except Exception as exception:
        logging.error(traceback.format_exc())
        exception_message = str(exception)
        print(exception_message)



def text_extraction(image_bytes: bytes): 
    """
    Takes in an image and extracts any text from it.
    :param image_bytes: bytes
    """

    # with statement avoids the need for a try-catch/close and opens the file path
    # with open(local_path, "rb") as image_file:
    #     undetected_image = image_file.read()

    undetected_image = image_bytes 

    vision_client = vision.ImageAnnotatorClient()
    vision_image = vision.Image(content = undetected_image)

    detected_response = vision_client.text_detection(image = vision_image)

    annotations = detected_response.text_annotations
    if (not annotations):
        raise ValueError("No text could be extracted from this image. Make sure the image has text!")
    text = annotations[0].description
    return text
