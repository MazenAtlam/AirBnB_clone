"""
module's review test file
"""
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """
    class defining testing methods for review class
    """
    def setUp(self):
        """
        Method to prepare test fixture
        """
        self.r1 = Review(text="text")

    def test_object_attributes(self):
        """
        Testing object attributes
        """
        self.assertIsInstance(self.r1.place_id, str)
        self.assertIsInstance(self.r1.user_id, str)
        self.assertIsInstance(self.r1.text, str)

        self.assertEqual(self.r1.text, "text")
        self.assertEqual(self.r1.user_id, '')
        self.assertEqual(self.r1.place_id, "")
