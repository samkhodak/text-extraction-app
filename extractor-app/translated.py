from flask import render_template, session, request, redirect, url_for
from flask.views import MethodView
from utilities.ml_features import auto_translate_text
import logging, traceback

class Translated(MethodView):
    """
    A class derived from MethodView to represent a presenter for the translated.html view. 
    """

    def post(self):
        """
        Translates the extracted text to the selected language and renders the page.
        """
        try:
            detected_text = session.get("extracted_text")
            if (not detected_text):
                return redirect(url_for('index'))

            detected_language = ""
            translated_text = ""

            target_language = request.form.get("language")

            translated_dict = auto_translate_text(detected_text, target_language)

            detected_language = translated_dict.get("detected_lang_name")
            translated_text = translated_dict.get("translated_text")

        except Exception as exception:
            logging.error(traceback.format_exc())
            exception_message = str(exception)
            print(exception_message)
            translated_text = "An error occurred, sorry! Please try again later, or with a different image."
            detected_language = ""

        return render_template('translated.html', title="Translated results", extracted_text=detected_text, translated_text=translated_text, detected_language=detected_language)