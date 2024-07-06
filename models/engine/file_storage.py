#!/usr/bin/python3
"""A module of the file storage class"""

import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Get all the objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Sets the obj in __objects with key <obj class name>.id"""

        FileStorage.__objects.update(
            {obj.__class__.__name__ + '.' + str(obj.id): obj})

    def save(self):
        """Serializes __objects to the JSON file"""

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            all_objects = FileStorage.__objects.copy()
            for key, value in all_objects.items():
                all_objects[key] = value.to_dict()

            json.dump(all_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        - If the __file_path does not exist, nothing will be done
        """
        from ..base_model import BaseModel
        from ..user import User
        from ..place import Place
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..review import Review

        try:
            with open(FileStorage.__file_path, encoding='utf-8') as file:
                all_objects = {}
                all_objects = json.load(file)
                for key, value in all_objects.items():
                    cls = eval(value['__class__'])
                    FileStorage.__objects[key] = cls(**value)

        except FileNotFoundError:
            pass
