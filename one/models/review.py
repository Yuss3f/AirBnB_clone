#!/usr/bin/python3
'''A module creating a Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Class to manage review objects'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''Initializing attributes for the review class'''
        super().__init__(*args, **kwargs)

