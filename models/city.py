#!/usr/bin/python3
"""A module creating a User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class to manage city objects"""

    state_id = ""
    name = ""

