"""
module's user test file
"""
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """
    class defining testing methods for user class
    """
    def setUp(self):
        """
        Method to prepare test fixture
        """
        self.u1 = User(email="my_email")

    def test_object_attributes(self):
        """
        Testing object attributes
        """
        self.assertIsInstance(self.u1.email, str)
        self.assertEqual(self.u1.email, "my_email")
        self.assertIsInstance(self.u1.password, str)
        self.assertEqual(self.u1.password, "")
        self.assertIsInstance(self.u1.first_name, str)
        self.assertEqual(self.u1.first_name, "")
        self.assertIsInstance(self.u1.last_name, str)
        self.assertEqual(self.u1.last_name, "")
