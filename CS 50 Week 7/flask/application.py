from flask import Flask, redirect, render_template, session, url_for

app = Flask(__name__)

@app.route("/") # if the request is / then send back to the homepage.
def index():
    return render_template("index.html")
