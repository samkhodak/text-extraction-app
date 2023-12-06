from utilities.image import encode_image
from utilities.ml_features import text_extraction
from utilities.constants import SUPPORTED_LANGUAGES
from flask import render_template, redirect, request, url_for, session
from flask.views import MethodView

class Results(MethodView):
    """
    A class derived from MethodView to represent a presenter for the results.html view. 
    """

    def get(self):
        """
        Renders the results.html page when the user wants to return to it with the image and detected text from session info.
        """
        encoded_image = session.get("image_bytes")
        extracted_string = session.get("extracted_text")

        if ((not encoded_image) or (not extracted_string)):
            return redirect(url_for('index'))
        
        array_of_translated = []
        array_of_romanized = []

        return render_template('results.html', title="Results", original_image=encoded_image.decode('utf-8'), extracted_text=extracted_string, 
                            languages=SUPPORTED_LANGUAGES, romanized_blocks=array_of_romanized)

    def post(self):
        """
        Processes the POST from index.html and renders the results.html page after doing conversions. 
        """
        image = request.files['image']
        image_bytes = request.files['image'].read()
        encoded_image = encode_image(image)
        extracted_string = text_extraction(image_bytes)

        session["image_bytes"] = encoded_image
        session["extracted_text"] = extracted_string

        # TESTING
        # top_language_codes = detect_main_language(detected_string)
        # print(top_language_codes)

        
        
        array_of_translated = []
        array_of_romanized = []
        # Put this in a dictionary?
        return render_template('results.html', title="Results", original_image=encoded_image.decode('utf-8'), extracted_text=extracted_string, 
                             languages=SUPPORTED_LANGUAGES, romanized_blocks=array_of_romanized)

 

    

