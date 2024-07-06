"""
module's state test file
"""
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """
    class defining testing methods for state class
    """
    def setUp(self):
        """
        Method to prepare test fixture
        """
        self.s1 = State(name="my_name")

    def test_object_attributes(self):
        """
        Testing object attributes
        """
        self.assertIsInstance(self.s1.name, str)
        self.assertEqual(self.s1.name, "my_name")
