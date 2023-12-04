from flask import render_template, session, request, redirect, url_for
from flask.views import MethodView

class Translated(MethodView):
    """
    A class derived from MethodView to represent a presenter for the index.html view. 
    """

    def post(self):
        """
        Renders the index.html page. TODO
        """

        encoded_image = session.get("image_bytes")
        detected_text = session.get("detected_text")
        if ((not encoded_image) or (not detected_text)):
            return redirect(url_for('index'))

        final_language = request.form["language"]
        print("text: ", detected_text)
        print("language: ", final_language)

        return render_template('translated.html')