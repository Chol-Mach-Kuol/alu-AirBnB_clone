#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def test_inherits_base_model(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertIsInstance(Amenity(), BaseModel)

    def test_class_attributes(self):
        """Test that Amenity has the required class attributes."""
        self.assertEqual(Amenity.name, "")

    def test_str_representation(self):
        """Test __str__ shows Amenity class name."""
        a = Amenity()
        self.assertIn("[Amenity]", str(a))

    def test_to_dict(self):
        """Test that to_dict returns Amenity as __class__."""
        a = Amenity()
        self.assertEqual(a.to_dict()["__class__"], "Amenity")

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        import models.amenity as m
        self.assertIsNotNone(m.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring."""
        self.assertIsNotNone(Amenity.__doc__)


if __name__ == "__main__":
    unittest.main()
