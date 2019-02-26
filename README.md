# Simple Blog
Using Python/Django or Flask, create a simple blogging application. The home page should show a list of blog posts, with the ability to click into the details of the post. The following views/functionality are expected:
<br>
*List view of posts
*Detail view of post
*Create a post (just title + description + created date) (**look at django forms)
*Edit a post
*Posts should persist using a database to store them
*You can use Bootstrap (http://getbootstrap.com/) to style your markup or material design (https://github.com/FezVrasta/bootstrap-material-design) if you prefer.

## Table of Contents

* [Tech Stack](#tech-stack)
* [Features](#features)
* [Setup/Installation](#installation)
* [Looking Ahead](#future)

## <a name="tech-stack"></a>Tech Stack

__Frontend:__ HTML, CSS, Bootstrap, Jinja <br>
__Backend:__ Python, Flask, PostgreSQL, SQLAlchemy<br>

## <a name="features"></a> Features

Can Create a post by clicking Create on NavBar <br>
After filling in information for Title, Description, Date, and clicking submit, new post is displayed in homepage<br>
Can view details of the post and edit a post by clicking on the Title of the post <br>
After clicking Edit Post, data from the post will already appear in place and can edit/update post <br>
Updated post will appear on homepage <br><br>
<img src="/static/blog.gif">

## <a name="installation"></a>Setup/Installation

Requirements:

- PostgreSQL
- Python 2.7

To have this app running on your local computer, please follow the below steps:

Clone repository:
```
$ git clone https://github.com/tuongviatruong/blog.git
```
Create a virtual environment:
```
$ virtualenv env
```
Activate the virtual environment:
```
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```

Create database 'blog'.
```
$ createdb blog
```
Create your database tables.
```
$ python -i model.py
Connected to DB.
>>> db.create_all()

```
Run the app from the command line.
```
$ python server.py
```

## <a name='future'></a> Looking Ahead
* Add more testing
* Add more styling to make site look better
* Add login/register- so different users can add to blog
