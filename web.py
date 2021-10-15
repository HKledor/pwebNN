from flask import Flask;
from flask import render_template;
from flask_bootstrap import Bootstrap;
from markupsafe import escape;
app = Flask(__name__);
#@app.route("/")
#def index():
#    return "<p>Index Page</p>";
@app.route("/contact")
def hello_world():
    return "<p>Contact Me @ Kledor00@gmail.com</p>";
@app.route("/")
def index():
    return render_template('home.html');
@app.route("/bio")
def bio():
    return "<p>BIO</p>";
@app.route("/projects")
def projects():
    return "<p>PROJECTS</p>";

