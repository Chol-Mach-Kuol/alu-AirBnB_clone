#!/usr/bin/python3
"""This module defines the Review class for the AirBnB clone project."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review with place_id, user_id, and text attributes."""

    place_id = ""
    user_id = ""
    text = ""
