#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def test_inherits_base_model(self):
        """Test that Place inherits from BaseModel."""
        self.assertIsInstance(Place(), BaseModel)

    def test_class_attributes(self):
        """Test that Place has the required class attributes."""
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

    def test_str_representation(self):
        """Test __str__ shows Place class name."""
        p = Place()
        self.assertIn("[Place]", str(p))

    def test_to_dict(self):
        """Test that to_dict returns Place as __class__."""
        p = Place()
        self.assertEqual(p.to_dict()["__class__"], "Place")

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        import models.place as m
        self.assertIsNotNone(m.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring."""
        self.assertIsNotNone(Place.__doc__)


if __name__ == "__main__":
    unittest.main()
