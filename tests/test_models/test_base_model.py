#!/usr/bin/python3
"""A unittest of the module base_module"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A test case of the class test BaseModel"""

    model = BaseModel()

    def test___str__(self):
        """A test for the print instance format string"""

        self.assertRegex(TestBaseModel.model.__str__(),
        "/^\[\w+\]\s\(([a-f0-9]{4,12}\-{0,1}){5}\)\s\{(?:\'\S+\'\:\s*\S+)*\}$")

    def test_to_dict(self):
        """A test for the method to_dict()"""

        dict_copy = TestBaseModel.model.__dict__.copy()
        dict_copy.update({'__class__': "BaseModel"})
        self.assertIn({'__class__': "BaseModel"}, TestBaseModel.model.to_dict())
        self.assertDictEqual(dict_copy, TestBaseModel.model.to_dict())

    def test_save(self):
        """A test for the method save()"""

        time_before_saving = TestBaseModel.model.updated_at
        TestBaseModel.model.save()
        time_after_saving = TestBaseModel.model.updated_at

        self.assertNotEqual(time_before_saving, time_after_saving)

if __name__ == '__main__':
    unittest.main()
