from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "SECRETSECRETSECRET"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Show homepage"""

    return render_template("homepage.html")



if __name__ == "__main__":

    app.debug = True
    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)
    app.run(host="0.0.0.0")