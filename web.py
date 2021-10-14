from flask import Flask;
from flask import render_template;
from flask_bootstrap import Bootstrap;
from markupsafe import escape;
app = Flask(__name__);
@app.route("/")
def index():
    return "<p>Index Page</p>";
@app.route("/hello")
def hello_world():
    return "<p>Hello World</p>";
@app.route("/<name>")
def hello(name):
    return f"<p>Hello, {escape(name)}</p>";
@app.route("/temp")
def temp():
    return render_template('temp.html');