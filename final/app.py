"""
khod2
This is a web app to extract text from images and view operations on it. 
"""


import flask
from flask.views import MethodView
from index import Index 
from results import Results

app = flask.Flask(__name__)

app.add_url_rule('/', 
                 view_func=Index.as_view('index'), 
                 methods=['GET'])

app.add_url_rule('/results',
                 view_func=Results.as_view('results'),
                 methods=['GET', 'POST'])


if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)


