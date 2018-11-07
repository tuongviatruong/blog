import unittest

from server import app
from model import connect_to_db, db, Blog, example_data

class Tests(unittest.TestCase):
    """Tests for site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("Sample Blog Post", result.data)
        self.assertIn("Create", result.data)


class TestsDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True



        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()


    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_example_data(self):
        result = self.client.get("/")
        self.assertIn("Example Post", result.data)
        self.assertIn("This is example post for testing", result.data)


if __name__ == "__main__":
    unittest.main()