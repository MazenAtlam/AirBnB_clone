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

    def __str__(self):
        """Print the instance in a formated string
        The format is [<class name>] (<self.id>) <self.__dict__>"""

        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the instance attribute updated_at with the save datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert the instance attribute into dict format"""

        obj_dict = self.__dict__.copy()
        obj_dict.update({'__class__': self.__class__.__name__})
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
