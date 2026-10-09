#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import unittest
import os
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

    def test_str_format(self):
        """Test __str__ matches [<class>] (<id>) <dict> format."""
        obj = BaseModel()
        expected = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected)

    def test_save_updates_updated_at(self):
        """Test that save() updates updated_at."""
        obj = BaseModel()
        old = obj.updated_at
        obj.save()
        self.assertGreaterEqual(obj.updated_at, old)

    def test_save_persists_to_file(self):
        """Test that save() writes to the JSON file."""
        obj = BaseModel()
        obj.save()
        self.assertTrue(os.path.exists("file.json"))

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

    def test_to_dict_iso_format(self):
        """Test that to_dict() uses correct ISO format for datetimes."""
        obj = BaseModel()
        d = obj.to_dict()
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        try:
            datetime.strptime(d["created_at"], fmt)
            datetime.strptime(d["updated_at"], fmt)
        except ValueError:
            self.fail("datetime not in correct ISO format")

    def test_to_dict_contains_id(self):
        """Test that to_dict() includes id."""
        obj = BaseModel()
        d = obj.to_dict()
        self.assertIn("id", d)
        self.assertEqual(d["id"], obj.id)

    def test_to_dict_type(self):
        """Test that to_dict() returns a dict."""
        obj = BaseModel()
        self.assertIsInstance(obj.to_dict(), dict)

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

    def test_from_dict_created_at_is_datetime(self):
        """Test that created_at is datetime when reconstructed from dict."""
        obj = BaseModel()
        d = obj.to_dict()
        obj2 = BaseModel(**d)
        self.assertIsInstance(obj2.created_at, datetime)

    def test_from_dict_updated_at_is_datetime(self):
        """Test that updated_at is datetime when reconstructed from dict."""
        obj = BaseModel()
        d = obj.to_dict()
        obj2 = BaseModel(**d)
        self.assertIsInstance(obj2.updated_at, datetime)

    def test_kwargs_empty(self):
        """Test that empty kwargs creates a new instance normally."""
        obj = BaseModel(**{})
        self.assertIsInstance(obj.id, str)

    def test_new_instance_in_storage(self):
        """Test that a new instance is added to storage."""
        from models import storage
        obj = BaseModel()
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, storage.all())

    def test_kwargs_instance_not_in_storage(self):
        """Test that kwargs-created instance is NOT added to storage again."""
        from models import storage
        obj = BaseModel()
        count_before = len(storage.all())
        d = obj.to_dict()
        BaseModel(**d)
        self.assertEqual(len(storage.all()), count_before)

    def test_id_is_string(self):
        """Test that id is a string."""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        import models.base_model as m
        self.assertIsNotNone(m.__doc__)
        self.assertGreater(len(m.__doc__), 1)

    def test_class_docstring(self):
        """Test that the class has a docstring."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertGreater(len(BaseModel.__doc__), 1)

    def test_method_docstrings(self):
        """Test that all methods have docstrings."""
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)


if __name__ == "__main__":
    unittest.main()
