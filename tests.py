from os import name
import unittest
from app import app, db
from app.models import User, Task

class UserModelCase(unittest.TestCase):
    """
    Testcase for the User model
    """
    def setUp(self):
        """
        Set up database temporarily
        """
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        """
        Destroy temporary database
        """
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        """
        Test password hashing methods
        """
        u = User(username="Bruno")
        u.set_password('Bruno')
        self.assertTrue(u.check_password('Bruno'))
        self.assertFalse(u.check_password('NotBruno'))

# Implement system testing concept learnt today
class AppTestCase(unittest.TestCase):
    """
    System test for our core app routes
    """
    def test_index(self):
        with app.test_client() as c:
            response = c.get('/')

            self.assertEqual(response.status_code, 302)


if __name__ == "__main__":
    unittest.main(verbosity=2)