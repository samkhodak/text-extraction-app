from flask import render_template
from flask.views import MethodView

class Index(MethodView):
    """
    A class derived from MethodView to represent a presenter for the index.html view. 
    """

    def get(self):
        """
        Renders the index.html page.
        """
        return render_template('index.html', title="Image text extractor")