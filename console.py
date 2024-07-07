#!/usr/bin/python3
"""
Module Defining the command line interpreter
"""
import cmd
from models.engine.file_storage import FileStorage
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.user import User


class HBNHCommand(cmd.Cmd):
    """
    Command Interpreter class
    Defines features and options
    delivered by the CLI
    """
    prompt = '(hbnb) '

    available_models = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def do_quit(self, line) -> bool:
        """Quit command to exit the program
        """
        return (True)

    def do_EOF(self, line) -> bool:
        """EOF Condition exits the program
        """
        print()
        return (True)

    def emptyline(self):
        """
        empty line + Enter
        Shouldnt do anything
        """
        pass

    def do_create(self, line):
        """creates new instance of the model
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNHCommand.available_models:
            print("** class doesn't exist **")
        else:
            new_instance = HBNHCommand.available_models[line]()
            BaseModel.save(new_instance)
            print(new_instance.id)

    def do_show(self, line):
        """Prints string representation
of an instance based
on class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split(" ")
            cls_name = args[0]
            if cls_name not in HBNHCommand.available_models:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                given_id = args[1]
                for obj in FileStorage.all(None).values():
                    if obj.id == given_id:
                        print(obj)
                        return
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on
class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split(" ")
            cls_name = args[0]
            if cls_name not in HBNHCommand.available_models:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                given_id = args[1]
                saved_objects = FileStorage.all(None)
                for key, val in saved_objects.items():
                    if val.id == given_id:
                        del saved_objects[key]
                        return
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation
of all instances based or not
on class name
        """
        list_to_print = []
        if not line:
            for obj in FileStorage.all(None).values():
                list_to_print.append(str(obj))
        elif line in HBNHCommand.available_models:
            for obj in FileStorage.all(None).values():
                if (obj.__class__.__name__ == line):
                    list_to_print.append(str(obj))
        else:
            print("** class doesn't exist **")
            return
        print(list_to_print)

    def do_update(self, line):
        """updates an instance
based on class name and id
by adding new attribute
or updating existing one
        """
        import re

        if not line:
            print("** class name missing **")
            return
        pattern = r'"\w+\s+\w+"'
        result = re.sub(pattern, lambda match:
                        match.group(0).replace(" ", "_"), line)
        args = result.split(" ")
        cls_name = args[0]
        if cls_name not in HBNHCommand.available_models:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        given_id = args[1]
        obj_to_update = None
        for obj in FileStorage.all(None).values():
            if obj.id == given_id:
                obj_to_update = obj
                break
        if obj_to_update is None:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        value = args[3]
        attr = args[2]
        if value.startswith('"'):
            value = value[1:-1]
        elif value.find(".") != -1:
            value = float(value)
        elif value.isnumeric():
            value = int(value)
        setattr(obj_to_update, attr, value)
        BaseModel.save(obj_to_update)


if __name__ == '__main__':
    HBNHCommand().cmdloop()
