#!/usr/bin/python3
"""A module includes a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class containing properties of Review object"""
    place_id = ''
    user_id = ''
    text = ''
