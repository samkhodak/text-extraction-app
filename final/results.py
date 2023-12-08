from utilities.image import encode_image
from utilities.ml_features import text_extraction
from utilities.constants import SUPPORTED_LANGUAGES
from flask import render_template, redirect, request, url_for, session
from flask.views import MethodView
import logging, traceback

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
        
        return render_template('results.html', title="Results", original_image=encoded_image.decode('utf-8'), extracted_text=extracted_string, 
                            languages=SUPPORTED_LANGUAGES)

    def post(self):
        """
        Processes the POST from index.html and renders the results.html page after doing conversions. 
        """
        try:
            error_message = None
            image = request.files['image']
            image_bytes = request.files['image'].read()
            encoded_image = encode_image(image)
            extracted_string = text_extraction(image_bytes)

            session["image_bytes"] = encoded_image
            session["extracted_text"] = extracted_string

        # When we know there are no proper words to extract
        except ValueError as v_error:
            logging.error(v_error)
            error_message = str(v_error)
        # Any other errors from API
        except Exception as exception:
            logging.error(traceback.format_exc())
            exception_message = str(exception)
            print(exception_message)
            error_message = "Something went wrong. Please try again later, or with a different image."
        finally:
            logging.info("ERROR MESSAGE AT FINALLY: ", error_message)
            if (error_message):
                # Make sure there is no extracted text stored in the session.
                if (session.get("extracted_text") is not None):
                    session.pop("extracted_text")
                return render_template('results.html', title="Results", original_image = encoded_image.decode('utf-8'), error_message=error_message)
            else:
                return render_template('results.html', title="Results", original_image=encoded_image.decode('utf-8'), extracted_text=extracted_string, 
                                        languages=SUPPORTED_LANGUAGES)
                # Put in a dictionary?
                
        

 

    

