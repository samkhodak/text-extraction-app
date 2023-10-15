from flask import render_template, redirect, request, url_for
from flask.views import MethodView
# We can import gbmodel folder because it is now a package with the init.py
import gbmodel

class Insert(MethodView):
    """
    A class derived from MethodView to represent a presenter for the insert.html view. 
    """
    def get(self):
      """ Renders the insert.html page."""
      return render_template('insert.html')
  
    def post(self):
        """
        Processes the POST request from the form, then redirects to index. 
        """
        model = gbmodel.get_model()
        # model.insert_quote("To be or not to be...", "William Shakespeare", "Hamlet", 9)
        return redirect(url_for('index'))
