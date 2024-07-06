#!/usr/bin/python3
"""A unittest of the module base_module"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A test case of the class test BaseModel"""

    mod1 = BaseModel()

    def test___init__(self):
        """A test for the constructor (instance creation)"""

        inst_args = TestBaseModel.mod1.to_dict()
        mod2 = BaseModel(**inst_args)
        self.assertNotIn('__class__', mod2.__dict__)
        self.assertIsInstance(mod2.created_at, datetime)
        self.assertIsInstance(mod2.updated_at, datetime)

    def test___str__(self):
        """A test for the print instance format string"""

        pattern = "^"+"\\"+"s*"+"\\"+"["+"\\"+"w+"+"\\"+"]"+"\\"+"s*"+"\\"
        pattern += "(([a-f0-9]{4,12}"+"\\"+"-{0,1}){5}"+"\\"+")"+"\\"+"s*"+"\\"
        pattern += "{(?:"+"\\"+"s*"+"\\"+"\'{0,1}"+"\\"+"w+"+"\\"+"\'{0,1}"
        pattern += "\\"+":{0,1}"+"\\"+"s*"+"\\"+"S+"+"\\"+",{0,1})*"+"\\"+"}$"
        self.assertRegex(TestBaseModel.mod1.__str__(), pattern)

    def test_to_dict(self):
        """A test for the method to_dict()"""

        self.assertIn('__class__', TestBaseModel.mod1.to_dict())

    def test_save(self):
        """A test for the method save()"""

        time_before_saving = TestBaseModel.mod1.updated_at
        TestBaseModel.mod1.save()
        time_after_saving = TestBaseModel.mod1.updated_at

        self.assertNotEqual(time_before_saving, time_after_saving)


if __name__ == '__main__':
    unittest.main()
