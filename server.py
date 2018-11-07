from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

from datetime import datetime
from jinja2 import StrictUndefined
from model import connect_to_db, db, Blog

app = Flask(__name__)
app.secret_key = "SECRETSECRETSECRET"

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def homepage():
    """Show homepage with one blog already shown, show all in database after creating post"""
    posts = Blog.query.all()
    return render_template("homepage.html", posts=posts)

@app.route('/create', methods=["GET", "POST"])
def create_form():
    """"Create a post and add to database"""
    form = BlogForm()
    if form.validate_on_submit():
        post = Blog(title=form.title.data,description=form.description.data,date=form.date.data)
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    return render_template("create_form.html", title="Create a Post", form=form)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    """Shows one post when clicked"""
    post = Blog.query.get(blog_id)

    return render_template('post.html', post=post)

@app.route('/post/<int:blog_id>/edit', methods=["GET", "POST"])
def edit_post(blog_id):
    """Edit post with data and edit database"""
    post = Blog.query.get(blog_id)

    form = BlogForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.description = form.description.data
        post.date= form.date.data
        db.session.commit()
        return redirect(url_for('post', blog_id=post.blog_id))

    form.title.data = post.title
    form.description.data = post.description
    form.date.data = post.date

    return render_template("create_form.html", title="Edit Post", form=form)


if __name__ == "__main__":

    app.debug = True
    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)
    app.run(host="0.0.0.0")