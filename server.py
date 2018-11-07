from flask import Flask, render_template, request, redirect, url_for

from datetime import datetime
from jinja2 import StrictUndefined
from model import connect_to_db, db, Blog

app = Flask(__name__)
app.secret_key = "SECRETSECRETSECRET"
app.jinja_env.undefined = StrictUndefined

posts = [
    {
        'title': 'Blog Post 1',
        'description': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'title': 'Blog Post 2',
        'description': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
def homepage():
    """Show homepage"""

    return render_template("homepage.html", posts=posts)




if __name__ == "__main__":

    app.debug = True
    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)
    app.run(host="0.0.0.0")