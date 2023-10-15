from flask import render_template
from flask.views import MethodView

class Quotes(MethodView):
    """
    A class derived from MethodView to represent a presenter for the quotes.html view. 
    """

    def get(self):
        """
        To be completed.
        """
        return render_template('quotes.html')
