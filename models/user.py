#!/usr/bin/python3
"""A module includes a User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class containing properties of user object"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
