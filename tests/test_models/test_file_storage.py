#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_all_returns_same_object(self):
        """Test that all() returns the __objects dict consistently."""
        self.assertIs(storage.all(), storage.all())

    def test_new_adds_object(self):
        """Test that new() adds an object to __objects."""
        obj = BaseModel()
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, storage.all())

    def test_new_key_format(self):
        """Test that new() uses <ClassName>.<id> as key."""
        obj = User()
        key = "User.{}".format(obj.id)
        self.assertIn(key, storage.all())

    def test_save_creates_file(self):
        """Test that save() creates the JSON file."""
        obj = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_file_is_valid_json(self):
        """Test that the saved file contains valid JSON."""
        obj = BaseModel()
        storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertIsInstance(data, dict)

    def test_save_contains_object(self):
        """Test that saved file contains the stored object."""
        obj = BaseModel()
        obj.save()
        key = "BaseModel.{}".format(obj.id)
        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertIn(key, data)

    def test_reload_restores_objects(self):
        """Test that reload() restores objects from file."""
        obj = BaseModel()
        obj.save()
        key = "BaseModel.{}".format(obj.id)
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(key, new_storage.all())

    def test_reload_restores_correct_class(self):
        """Test that reload() restores objects as correct class instances."""
        obj = User()
        obj.save()
        key = "User.{}".format(obj.id)
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIsInstance(new_storage.all()[key], User)

    def test_reload_no_file(self):
        """Test that reload() does not raise if file doesn't exist."""
        s = FileStorage()
        s._FileStorage__file_path = "nonexistent_xyz.json"
        try:
            s.reload()
        except Exception as e:
            self.fail("reload() raised an exception: {}".format(e))

    def test_reload_all_classes(self):
        """Test that reload() handles all supported classes."""
        classes = [BaseModel, User, State, City, Amenity, Place, Review]
        objs = [cls() for cls in classes]
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.assertIn(key, new_storage.all())

    def test_file_path_is_string(self):
        """Test that __file_path is a string."""
        self.assertIsInstance(
            FileStorage._FileStorage__file_path, str)

    def test_objects_is_dict(self):
        """Test that __objects is a dictionary."""
        self.assertIsInstance(
            FileStorage._FileStorage__objects, dict)

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        import models.engine.file_storage as m
        self.assertIsNotNone(m.__doc__)
        self.assertGreater(len(m.__doc__), 1)

    def test_class_docstring(self):
        """Test that the class has a docstring."""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertGreater(len(FileStorage.__doc__), 1)

    def test_method_docstrings(self):
        """Test that all methods have docstrings."""
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)


if __name__ == "__main__":
    unittest.main()
