#!/usr/bin/python3
"""A unittest of the module file_storage"""

import unittest
from models import storage
from models.base_model import BaseModel
from models.city import City


class TestBaseModel(unittest.TestCase):
    """A test case of the class FileStorage"""

    def test___file_path(self):
        """A test for the private attribute __file_path"""

        with self.assertRaises(AttributeError):
            file = storage.__file_path

    def test___objects(self):
        """A test for the private attribute __objects"""

        with self.assertRaises(AttributeError):
            all_objects = storage.__objects

    def test_all(self):
        """A test for the method all(self)"""

        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        mod1 = BaseModel()
        all_objects = storage.all()
        self.assertIn(mod1, all_objects.values())

    def test_new(self):
        """A test for the method new(self, obj)"""

        test = BaseModel()
        all_objects = storage.all()
        self.assertIn(test, all_objects.values())

    def test_save(self):
        """A test for the method save(self)"""

        import os

        if os.path.isfile('file.json'):
            os.remove('file.json')

        self.assertFalse(os.path.isfile('file.json'))
        mod3 = BaseModel()
        mod3.save()
        self.assertTrue(os.path.isfile('file.json'))

    def test_reload(self):
        """A test for the method reload(self)"""

        import os

        if os.path.isfile('file.json'):
            os.remove('file.json')

        self.assertFalse(os.path.isfile('file.json'))
        storage.reload()  # Not raises any errors also file does not exist
