"""
module's city test file
"""
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """
    class defining testing methods for city class
    """
    def setUp(self):
        """
        Method to prepare test fixture
        """
        self.c1 = City(name="my_name", id="my_id")

    def test_object_attributes(self):
        """
        Testing object attributes
        """
        self.assertIsInstance(self.c1.name, str)
        self.assertIsInstance(self.c1.id, str)
        self.assertEqual(self.c1.name, "my_name")
        self.assertEqual(self.c1.id, "my_id")
