#!/usr/bin/python3
"""This module instantiates the storage object for the application."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
