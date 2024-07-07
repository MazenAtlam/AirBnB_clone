"""
module's amentiy test file
"""
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """
    class defining testing methods for Amenity class
    """
    def setUp(self):
        """
        Method to prepare test fixture
        """
        self.a1 = Amenity(name="my_name")

    def test_object_attributes(self):
        """
        Testing object attributes
        """
        self.assertIsInstance(self.a1.name, str)
        self.assertEqual(self.a1.name, "my_name")
