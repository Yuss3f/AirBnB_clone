#!/usr/bin/python3
'''A module creating a User class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Class to manage user objects'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''Initializing attributes for the User class'''
        super().__init__(*args, **kwargs)

