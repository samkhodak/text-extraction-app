from flask import render_template, session, request
from flask.views import MethodView

class Translated(MethodView):
    """
    A class derived from MethodView to represent a presenter for the index.html view. 
    """

    def post(self):
        """
        Renders the index.html page. TODO
        """
        detected_text = session.get("detected_text")
        final_language = request.form["language"]
        print("text: ", detected_text)
        print("language: ", final_language)

        return render_template('translated.html')