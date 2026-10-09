#!/usr/bin/python3
"""This module defines the Place class for the AirBnB clone project."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a Place with location, capacity, and pricing attributes."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
