"""
khod2
This is a web app to store and modify famous quotes.
"""


import flask
from flask.views import MethodView
from index import Index 
from quotes import Quotes
from insert import Insert

app = flask.Flask(__name__)

app.add_url_rule('/', 
                 view_func=Index.as_view('index'), 
                 methods=["GET"])

app.add_url_rule('/quotes',
                 view_func=Quotes.as_view('quotes'),
                 methods=['GET'])

app.add_url_rule('/insert',
                 view_func=Insert.as_view('insert'),
                 methods=['GET', 'POST'])


if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)


