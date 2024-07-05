#!/usr/bin/python3
"""A module includes a BaseModel class"""

import uuid
from datetime import datetime


class BaseModel:
    """A class that defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialize the instance attributes"""

        self.created_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        self.__dict__.update(
            {'__class__': str(self.__class__).split('.')[1].strip("'>")})


    def __str__(self):
        """Print the instance in a formated string
        The format is [<class name>] (<self.id>) <self.__dict__>"""

        obj_dict = self.to_dict().copy()
        return '[{}] ({}) {}'.format(obj_dict.get('__class__'),
                                     self.id, obj_dict.pop('__class__'))

    def save(self):
        """Updates the instance attribute updated_at with the save datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert the instance attribute into dict format"""

        return self.__dict__
