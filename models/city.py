#!/usr/bin/python3
"""This module defines the City class for the AirBnB clone project."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City with state_id and name attributes."""

    state_id = ""
    name = ""
