"""
khod2
This is a web app to extract text from images and perform AI-powered text operations on it. 
"""
from romanized import Romanized
import flask
import uuid
from flask_session import Session
from index import Index 
from results import Results
from translated import Translated

app = flask.Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


app.add_url_rule('/', 
                 view_func=Index.as_view('index'), 
                 methods=['GET'])

app.add_url_rule('/results',
                 view_func=Results.as_view('results'),
                 methods=['GET', 'POST'])

app.add_url_rule('/translated',
                 view_func=Translated.as_view('translated'),
                 methods=['POST'])

app.add_url_rule('/romanized',
                 view_func=Romanized.as_view('romanized'),
                 methods=['POST'])


if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)


