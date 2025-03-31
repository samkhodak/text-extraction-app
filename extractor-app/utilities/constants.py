"""
This file saves constants for easy use in all app files.
"""
import os
from google.cloud import translate
import logging
import traceback


def get_languages():
    """
    Gets a list of available languages to translate to from the translate API. 
    :return: list of language dictionaries
    """
    project_id = os.getenv("PROJECT_ID")
    project_parent = f"projects/{project_id}"
    try:
        translate_client = translate.TranslationServiceClient()
        supported_languages = translate_client.get_supported_languages(display_language_code="en", parent=project_parent).languages
        language_names = [dict(code=language_dict.language_code, name=language_dict.display_name) for language_dict in supported_languages]
        return language_names


    except Exception as exception:
        logging.error(traceback.format_exc())
        exception_message = str(exception)
        print(exception_message)
        return None

# Constant for all files to use one list of supported languages per runtime. 
SUPPORTED_LANGUAGES = get_languages()