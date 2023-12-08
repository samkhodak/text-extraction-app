from flask import render_template, session, request, redirect, url_for
from flask.views import MethodView
from utilities.ml_features import romanize_text
import requests, logging, traceback

class Romanized(MethodView):
    """
    A class derived from MethodView to represent a presenter for the romanized.html view. 
    """

    def post(self):
        """
        Romanizes the extracted text if possible, then renders the resulting romanized page.
        """

        extracted_text = session.get("extracted_text")
        if (not extracted_text):
            return redirect(url_for('index'))

        romanized_text = ""

        try:
            romanized_dict = romanize_text(extracted_text)
            romanized_text = romanized_dict.get("romanized_text")

        except ValueError as v_error:
            logging.error(v_error)
            romanized_text = str(v_error)
        except requests.exceptions.HTTPError as error:
            logging.error(error)
            romanized_text =  "The program was not able to romanize the language of the text in the image. Please try a different image."
        except Exception as exception:
            logging.error(traceback.format_exc())
            exception_message = str(exception)
            print(exception_message)
            romanized_text = "Something went wrong. Please try again later, or with a different image."
        finally:
            return render_template('romanized.html', title="Romanized results", extracted_text=extracted_text, romanized_text=romanized_text)