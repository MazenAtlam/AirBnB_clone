#!/usr/bin/python3
"""A module includes a BaseModel class"""

import uuid
from datetime import datetime


class BaseModel:
    """A class that defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialize the instance attributes"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Print the instance in a formated string
        The format is [<class name>] (<self.id>) <self.__dict__>"""

        return '[{}] ({}) {}'.format(self.to_dict().get('__class__'),
                                     self.id, self.__dict__)

    def save(self):
        """Updates the instance attribute updated_at with the save datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert the instance attribute into dict format"""

        new_dict = self.__dict__.copy()
        new_dict.update(
            {'__class__': str(self.__class__).split('.')[1].strip("'>")})

        return new_dict
