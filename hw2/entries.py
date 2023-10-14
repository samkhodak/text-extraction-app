from flask import render_template
from flask.views import MethodView

class Entries(MethodView):
    """
    A class derived from MethodView to represent a presenter for the entries.html view. 

    ...

    Methods
    ----------
    get(self):
        Renders the entries.html page.
    """

    def get(self):
        return render_template('entries.html')
