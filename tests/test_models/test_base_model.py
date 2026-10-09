#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_instance_attributes(self):
        """Test that a new instance has id, created_at, updated_at."""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_unique_ids(self):
        """Test that two instances have different ids."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_str(self):
        """Test __str__ output format."""
        obj = BaseModel()
        s = str(obj)
        self.assertIn("[BaseModel]", s)
        self.assertIn(obj.id, s)

    def test_save_updates_updated_at(self):
        """Test that save() updates updated_at."""
        obj = BaseModel()
        old = obj.updated_at
        obj.save()
        self.assertGreaterEqual(obj.updated_at, old)

    def test_to_dict_contains_class(self):
        """Test that to_dict() includes __class__ key."""
        obj = BaseModel()
        d = obj.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")

    def test_to_dict_datetime_strings(self):
        """Test that to_dict() converts datetimes to ISO strings."""
        obj = BaseModel()
        d = obj.to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_from_dict(self):
        """Test creating a BaseModel from a dictionary."""
        obj = BaseModel()
        obj.name = "test"
        d = obj.to_dict()
        obj2 = BaseModel(**d)
        self.assertEqual(obj.id, obj2.id)
        self.assertEqual(obj.name, obj2.name)
        self.assertIsInstance(obj2.created_at, datetime)
        self.assertIsNot(obj, obj2)

    def test_from_dict_no_class_attr(self):
        """Test that __class__ is not set as an instance attribute."""
        obj = BaseModel()
        d = obj.to_dict()
        obj2 = BaseModel(**d)
        self.assertNotIn("__class__", obj2.__dict__)

    def test_kwargs_empty(self):
        """Test that empty kwargs creates a new instance normally."""
        obj = BaseModel(**{})
        self.assertIsInstance(obj.id, str)

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        import models.base_model as m
        self.assertIsNotNone(m.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring."""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_method_docstrings(self):
        """Test that all methods have docstrings."""
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)


if __name__ == "__main__":
    unittest.main()
