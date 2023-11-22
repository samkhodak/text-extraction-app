from utilities.image import encode_image
from flask import render_template, redirect, request, url_for
from flask.views import MethodView


class Results(MethodView):
    """
    A class derived from MethodView to represent a presenter for the results.html view. 
    """
    
    def post(self):
        """
        Processes the POST from index.html and renders the results.html page after doing conversions. 
        """
        image = request.files.get('image', '')
        encoded_image = encode_image(image)

        array_of_blocks = []
        array_of_translated = []
        array_of_romanized = []
        translated_audio = None
        # Put this in a dictionary?
        return render_template('results.html', original_image=encoded_image.decode('utf-8'), blocks=array_of_blocks, 
                               translated_blocks=array_of_translated, romanized_blocks=array_of_romanized, translated_audio=translated_audio)

 

    

