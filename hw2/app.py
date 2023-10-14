"""
khod2
This is a web app to store and modify famous quotes.
"""


import flask
from flask.views import MethodView
from index import Index 
from entries import Entries
from insert import Insert

app = flask.Flask(__name__)

app.add_url_rule('/', 
                 view_func=Index.as_view('index'), 
                 methods=["GET"])

app.add_url_rule('/entries',
                 view_func=Entries.as_view('entries'),
                 methods=['GET'])

app.add_url_rule('/insert',
                 view_func=Insert.as_view('insert'))



if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)


