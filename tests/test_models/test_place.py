"""
module's place test file
"""
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """
    class defining testing methods for place class
    """
    def setUp(self):
        """
        Method to prepare test fixture
        """
        self.p1 = Place(name="my_name", user_id='user_id',
                        city_id='city_id', latitude=23.5,
                        amenity_ids=["1", "2"], max_guest=3)

    def test_object_attributes(self):
        """
        Testing object attributes
        """
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p1.city_id, str)
        self.assertIsInstance(self.p1.user_id, str)
        self.assertIsInstance(self.p1.description, str)
        self.assertIsInstance(self.p1.number_rooms, int)
        self.assertIsInstance(self.p1.max_guest, int)
        self.assertIsInstance(self.p1.price_by_night, int)
        self.assertIsInstance(self.p1.number_bathrooms, int)
        self.assertIsInstance(self.p1.longitude, float)
        self.assertIsInstance(self.p1.latitude, float)
        self.assertIsInstance(self.p1.amenity_ids, list)

        self.assertEqual(self.p1.name, "my_name")
        self.assertEqual(self.p1.city_id, "city_id")
        self.assertEqual(self.p1.user_id, "user_id")
        self.assertEqual(self.p1.description, '')
        self.assertEqual(self.p1.number_rooms, 0)
        self.assertEqual(self.p1.max_guest, 3)
        self.assertEqual(self.p1.price_by_night, 0)
        self.assertEqual(self.p1.number_bathrooms, 0)
        self.assertEqual(self.p1.longitude, 0.0)
        self.assertEqual(self.p1.latitude, 23.5)
        self.assertEqual(self.p1.amenity_ids, ["1", "2"])
