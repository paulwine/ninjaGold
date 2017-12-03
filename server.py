from flask import Flask, redirect, request, session, flash, render_template
import random

app = Flask(__name__)

app.secret_key = "SECRETS"

@app.route('/')
def index():
    return render_template("index.html")

app.run(debug=True)