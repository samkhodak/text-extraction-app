from flask import render_template
from flask.views import MethodView

class Index(MethodView):
    """
    A class derived from MethodView to represent a presenter for the index.html view. 

    ...

    Methods
    ----------
    get(self):
        Renders the index.html page.
    """

    def get(self):
      print("index.py")
      return render_template('index.html')