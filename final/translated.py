from flask import render_template, session, request, redirect, url_for
from flask.views import MethodView
from utilities.ml_features import auto_translate_text

class Translated(MethodView):
    """
    A class derived from MethodView to represent a presenter for the translated.html view. 
    """

    def post(self):
        """
        Translates the extracted text to the selected language and renders the page.
        """

        # encoded_image = session.get("image_bytes")
        detected_text = session.get("extracted_text")
        if (not detected_text):
            return redirect(url_for('index'))

        target_language = request.form["language"]

        translated_dict = auto_translate_text(detected_text, target_language)
        detected_language = translated_dict["detected_lang_name"]
        translated_text = translated_dict["translated_text"]

        return render_template('translated.html', extracted_text=detected_text, translated_text=translated_text, detected_language=detected_language)