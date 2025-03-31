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
        Processes the POST request from the form and inserts it into the database; 
        Redirects to index. 
        """
        model = gbmodel.get_model()
        model.insert_quote(request.form['person'], request.form['source'], int(request.form['rating']), request.form['quote'])
        return redirect(url_for('index'))
