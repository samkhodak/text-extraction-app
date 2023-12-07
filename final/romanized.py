from flask import render_template, session, request, redirect, url_for
from flask.views import MethodView
from utilities.ml_features import romanize_text

class Romanized(MethodView):
    """
    A class derived from MethodView to represent a presenter for the romanized.html view. 
    """

    def post(self):
        """
        Romanizes the extracted text if possible, then renders the resulting romanized page.
        """

        detected_text = session.get("extracted_text")
        if (not detected_text):
            return redirect(url_for('index'))
        
        romanize_text(detected_text)
        
        romanized_text = ""

        return render_template('romanized.html', title="Romanized results", extracted_text=detected_text, romanized_text=romanized_text)