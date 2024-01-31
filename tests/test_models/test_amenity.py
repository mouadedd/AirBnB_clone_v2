#!/usr/bin/python3
"""test for amenity"""
import os
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Amenity class tests"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.amenity = Amenity()
        cls.amenity.name = "WiFi"

    @classmethod
    def teardown(cls):
        """check teardown"""
        del cls.amenity

    def tearDown(self):
        """check teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring_amenity(self):
        """test if docstrings exist"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_amenity(self):
        """chekcing for amenity attributes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_amenity(self):
        """test for subclass amenity"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_amenity(self):
        """test for attribute type"""
        self.assertEqual(type(self.amenity.name), str)

    def test_save_amenity(self):
        """test if data saved"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_amenity(self):
        """test the dictionary"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
