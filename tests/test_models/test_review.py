#!/usr/bin/python3
"""Unit tests for the Review class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class."""

    def test_inherits_base_model(self):
        """Test that Review inherits from BaseModel."""
        self.assertIsInstance(Review(), BaseModel)

    def test_class_attributes(self):
        """Test that Review has the required class attributes."""
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

    def test_str_representation(self):
        """Test __str__ shows Review class name."""
        r = Review()
        self.assertIn("[Review]", str(r))

    def test_to_dict(self):
        """Test that to_dict returns Review as __class__."""
        r = Review()
        self.assertEqual(r.to_dict()["__class__"], "Review")

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        import models.review as m
        self.assertIsNotNone(m.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring."""
        self.assertIsNotNone(Review.__doc__)


if __name__ == "__main__":
    unittest.main()
