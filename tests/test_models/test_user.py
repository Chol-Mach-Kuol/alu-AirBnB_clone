#!/usr/bin/python3
"""Unit tests for the User class."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def test_inherits_base_model(self):
        """Test that User inherits from BaseModel."""
        self.assertIsInstance(User(), BaseModel)

    def test_class_attributes(self):
        """Test that User has the required class attributes."""
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_instance_creation(self):
        """Test that a User instance can be created."""
        u = User()
        self.assertIsNotNone(u.id)

    def test_str_representation(self):
        """Test __str__ shows User class name."""
        u = User()
        self.assertIn("[User]", str(u))

    def test_to_dict(self):
        """Test that to_dict returns User as __class__."""
        u = User()
        d = u.to_dict()
        self.assertEqual(d["__class__"], "User")

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        import models.user as m
        self.assertIsNotNone(m.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring."""
        self.assertIsNotNone(User.__doc__)


if __name__ == "__main__":
    unittest.main()
