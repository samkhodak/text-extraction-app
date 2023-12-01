from utilities.image import encode_image
from utilities.ml_functions import text_detection, detect_handwriting_update_later
from flask import render_template, redirect, request, url_for
from flask.views import MethodView
import base64
from werkzeug.utils import secure_filename
import tempfile
import os
from PIL import Image
import io
class Results(MethodView):
    """
    A class derived from MethodView to represent a presenter for the results.html view. 
    """
    
    def post(self):
        """
        Processes the POST from index.html and renders the results.html page after doing conversions. 
        """
        image = request.files['image']
        image_bytes = request.files['image'].read()
        # print(second_image)
        print(type(image_bytes))
        encoded_image = encode_image(image)
        detected_string = text_detection(image_bytes)
        detect_handwriting_update_later(image_bytes)

        array_of_translated = []
        array_of_romanized = []
        translated_audio = None
        # Put this in a dictionary?
        return render_template('results.html', original_image=encoded_image.decode('utf-8'), original_extracted_text=detected_string, 
                               translated_blocks=array_of_translated, romanized_blocks=array_of_romanized, translated_audio=translated_audio)

 

    

