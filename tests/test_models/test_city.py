#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def test_inherits_base_model(self):
        """Test that City inherits from BaseModel."""
        self.assertIsInstance(City(), BaseModel)

    def test_class_attributes(self):
        """Test that City has the required class attributes."""
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def test_str_representation(self):
        """Test __str__ shows City class name."""
        c = City()
        self.assertIn("[City]", str(c))

    def test_to_dict(self):
        """Test that to_dict returns City as __class__."""
        c = City()
        self.assertEqual(c.to_dict()["__class__"], "City")

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        import models.city as m
        self.assertIsNotNone(m.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring."""
        self.assertIsNotNone(City.__doc__)


if __name__ == "__main__":
    unittest.main()
