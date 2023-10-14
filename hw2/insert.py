from flask import render_template, redirect, request, url_for
from flask.views import MethodView

class Insert(MethodView):
    """
    A class derived from MethodView to represent a presenter for the insert.html view. 

    ...

    Methods
    ----------
    get(self):
        Renders the insert.html page.

    post(self):
        ----         
    """

    def get(self):
      return render_template('insert.html')
  
    def post(self):
      """
      Will be completed later.
      """
      return redirect(url_for('index'))