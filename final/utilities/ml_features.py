from google.cloud import vision, translate
from utilities.constants import SUPPORTED_LANGUAGES
import string
import traceback
import logging
import os, json, requests

def romanize_text(text: str):
    """
    Receives extracted text and romanizes it, assuming the text is able to be romanized.
    :return: dictionary including romanized text and detected language.
    """
    try:
        # Request service account access token from GCP metadata service
        auth_url = "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token"
        auth_headers = {
            "Metadata-Flavor": "Google",
        }
        token = requests.get(auth_url, headers=auth_headers)
        token_dict = token.json()
        access_token = token_dict["access_token"]

        # With the access token, make a POST request to the romanization REST API.
        project_id = os.getenv("PROJECT_ID")
        location = os.getenv("location")
        romanization_url = f"https://translation.googleapis.com/v3/projects/{project_id}/locations/{location}:romanizeText"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        text_content = {
                    "contents": text
        }
        romanization_result = requests.post(romanization_url, headers=headers, json=text_content)
        romanized_dict = romanization_result.json()
        print(romanized_dict)
        romanized_text = romanized_dict["romanizedText"]
        detected_lang_code = romanized_dict["detectedLanguageCode"]

        print("Romanized text: ", romanized_text)
        print("Language code: ", detected_lang_code)

    except Exception as exception:
        logging.error(traceback.format_exc())
        exception_message = str(exception)
        print(exception_message)



def auto_translate_text(text: str, language_code: str):
    """
    Receives extracted text and translates it to the target language using 
    translate API's auto language detection.
    :return: dictionary including translated text and detected language.
    """
    project_id = os.getenv("PROJECT_ID")
    location = os.getenv("LOCATION")
    project_parent = f"projects/{project_id}/locations/{location}"

    try:
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
        lang_name = [lang["name"] for lang in supported_languages if lang["code"] == detected_lang_code]
        
        # It's alright to use result[0] since we don't support more than one string passed to the translation.
        return dict(
            translated_text = result[0].translated_text, 
            detected_lang_code = detected_lang_code,
            detected_lang_name = lang_name[0],
        )

    except Exception as exception:
        logging.error(traceback.format_exc())
        exception_message = str(exception)
        print(exception_message)
        return "An error has occurred. Please try again later!"



def detect_main_language(text: str):
    """
    Detects what language a piece of text is mainly in, in order to send to translation.
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

    # with statement avoids the need for a try-catch/close and opens the file path
    # with open(local_path, "rb") as image_file:
    #     undetected_image = image_file.read()
    undetected_image = image_bytes 

    try: 
        vision_client = vision.ImageAnnotatorClient()
        vision_image = vision.Image(content = undetected_image)

        detected_response = vision_client.text_detection(image = vision_image)

        annotations = detected_response.text_annotations
        if (not annotations):
            raise Exception("No text could be extracted from this image. Make sure the image has text!")
        text = annotations[0].description
        return text

    except Exception as exception:
        logging.error(traceback.format_exc())
        exception_message = str(exception)

        # return "An error has occurred. Please try again later."
        return exception_message



def detect_handwriting_update_later(image_bytes): 
    vision_client = vision.ImageAnnotatorClient()

    # with statement avoids the need for a try-catch/close and oVjpens the file path
    # with open(path, "rb") as image_file:
    #     undetected_image = image_file.read()

    undetected_image = image_bytes

    vision_image = vision.Image(content = undetected_image)

    detected_response = vision_client.document_text_detection(image = vision_image)

    final_image_text = page_to_string(detected_response.full_text_annotation.pages)    

    print(final_image_text)


def page_to_string(text_pages):
    for page in text_pages:
        for block in page.blocks:
            block_text = "BLOCK: "
            for paragraph in block.paragraphs:
                paragraph_text = ""
                for word in paragraph.words:
                    one_word = "".join([symbol.text for symbol in word.symbols])
                    if (one_word in string.punctuation):
                        paragraph_text += one_word 
                    else:
                        paragraph_text += f'{one_word} '
                block_text += paragraph_text
            print(block_text)



