#!/usr/bin/python3
"""A unittest of the module base_module"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A test case of the class test BaseModel"""

    model = BaseModel()

    def test_save(self):
        """A test for the method save()"""

        time_before_saving = TestBaseModel.model.updated_at
        TestBaseModel.model.save()
        time_after_saving = TestBaseModel.model.updated_at

        self.assertNotEqual(time_before_saving, time_after_saving)

if __name__ == '__main__':
    unittest.main()
