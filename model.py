from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# class User(db.Model):
#     """User of website"""
#     __tablename__ = "users"

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     fname = db.Column(db.String(64))
#     lname = db.Column(db.String(64))
#     email = db.Column(db.String(64))
#     password = db.Column(db.String(64))

#     def __repr__(self):
#         """Provide helpful representation when printed"""
#         return "<User user_id={} fname={} lname={}>".format(self.user_id,
#                                                         self.fname, self.lname)

class Blog(db.Model):
    """Blogs users uplaod"""
    __tablename__ = "blogs"

    blog_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    #Define relationship to user
    # user = db.relationship("User", backref="blogs")

    def __repr__(self):
        """Provide helpful representation when printed"""
        return "<Blog blog_id={} title={}>".format(self.blog_id, self.title)


def example_data():
    blog = Blog(title="Example Post", description="This is example post for testing", date="November 6 2018")

    db.session.add(blog)
    db.session.commit()

##############################################################################
# Helper functions

def connect_to_db(app, db_uri='postgresql:///blog'):
    """Connect the database to Flask app."""

    # Configure to use PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."