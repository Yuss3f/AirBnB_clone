#!/usr/bin/python3
'''A module creating a Amenity class'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Class to manage amenity objects'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializing attributes for the Amenity class'''
        super().__init__(*args, **kwargs)

