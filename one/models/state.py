#!/usr/bin/python3
'''A module creating a User class'''
from models.base_model import BaseModel


class State(BaseModel):
    '''Class to manage state objects'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializing attributes for the State class'''
        super().__init__(*args, **kwargs)

