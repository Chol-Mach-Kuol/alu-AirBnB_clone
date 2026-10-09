#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State class."""

    def test_inherits_base_model(self):
        """Test that State inherits from BaseModel."""
        self.assertIsInstance(State(), BaseModel)

    def test_class_attributes(self):
        """Test that State has the required class attributes."""
        self.assertEqual(State.name, "")

    def test_str_representation(self):
        """Test __str__ shows State class name."""
        s = State()
        self.assertIn("[State]", str(s))

    def test_to_dict(self):
        """Test that to_dict returns State as __class__."""
        s = State()
        self.assertEqual(s.to_dict()["__class__"], "State")

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        import models.state as m
        self.assertIsNotNone(m.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring."""
        self.assertIsNotNone(State.__doc__)


if __name__ == "__main__":
    unittest.main()
