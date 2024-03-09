#!/usr/bin/python3
"""Defining Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representing an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

