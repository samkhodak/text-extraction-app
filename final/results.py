from utilities.image import encode_image
from utilities.ml_functions import text_detection, detect_handwriting_update_later
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
        detected_text = session.get("detected_text")
        print("encoded img => ", encoded_image)
        print("original detected text => ", detected_text)

        if ((not encoded_image) or (not detected_text)):
            return redirect(url_for('index'))

        array_of_translated = []
        array_of_romanized = []

        return render_template('results.html', original_image=encoded_image.decode('utf-8'), original_extracted_text=detected_text, 
                               translated_blocks=array_of_translated, romanized_blocks=array_of_romanized)

    
    def post(self):
        """
        Processes the POST from index.html and renders the results.html page after doing conversions. 
        """
        image = request.files['image']
        image_bytes = request.files['image'].read()
        encoded_image = encode_image(image)
        detected_string = text_detection(image_bytes)
        # detect_handwriting_update_later(image_bytes)

        session["image_bytes"] = encoded_image
        session["detected_text"] = detected_string

        array_of_translated = []
        array_of_romanized = []
        # Put this in a dictionary?
        return render_template('results.html', original_image=encoded_image.decode('utf-8'), original_extracted_text=detected_string, 
                               translated_blocks=array_of_translated, romanized_blocks=array_of_romanized)

 

    

