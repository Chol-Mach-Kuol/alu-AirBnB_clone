#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up test fixtures."""
        self.storage = storage

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new() adds an object to __objects."""
        obj = BaseModel()
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        """Test that save() creates the JSON file."""
        obj = BaseModel()
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_reload_consistency(self):
        """Test that saved objects can be reloaded."""
        obj = BaseModel()
        obj.name = "test_reload"
        obj.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, new_storage.all())

    def test_reload_no_file(self):
        """Test that reload() does not raise if file doesn't exist."""
        s = FileStorage()
        s._FileStorage__file_path = "nonexistent_file.json"
        try:
            s.reload()
        except Exception as e:
            self.fail("reload() raised an exception: {}".format(e))

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        import models.engine.file_storage as m
        self.assertIsNotNone(m.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring."""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_method_docstrings(self):
        """Test that all methods have docstrings."""
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)


if __name__ == "__main__":
    unittest.main()
