#!/usr/bin/python3
"""AirBnB_clone Console Module"""

import cmd


import models

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

import json


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter for AirBnB Clone

    Attributes:
        prompt (str): command prompt prefix string
        cmd (Cmd): command line interpreter
        models (dict): dictionary of available models
        parsebale_commands (list): list of commands
                that are parseable by precmd.
    """
    prompt = "(hbnb) "
    cmd = cmd.Cmd()

    models = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    parsebale_commands = [
        "destroy",
        "update",
    ]

    def precmd(self, arg):
        """Pre Command to handle Parseable class.method()"""
        if "." in arg and len(arg.split(".", 1)) == 2 \
                and arg.split(".", 1)[1].split("(", 1)[0].strip() \
                in self.parsebale_commands:
            [model, command] = arg.split(".")
            [command, other_args] = command[:-1].split("(", 1)
            if command != "update":
                other_args.replace("\"", "").replace(",", " ")
            else:
                if "{" in other_args:
                    obj = other_args.split("{", 1)[1].split("}", 1)[
                        0].replace(" ", "").replace("'", "\"")
                    other_args = other_args.split("{", 1)[0].replace(
                        ",", " ").replace("\"", "") + " {" + obj + "}"
            line = "{} {} {}".format(command, model, other_args)
            return line
        return arg

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Handles empty line"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of Available Models
            and saves it to JSON file
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.models:
            print("** class doesn't exist **")
        else:
            new_instance = self.models[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
        else:
            splitted = arg.strip().split()
            if splitted[0] not in self.models:
                print("** class doesn't exist **")
            elif len(splitted) < 2:
                print("** instance id missing **")
            else:
                instance_id = splitted[1]
                key = "{}.{}".format(splitted[0], instance_id)
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances of a class"""
        class_name = arg.split('.')[0]
        if class_name in self.models:
            instances = models.storage.all(self.models[class_name])
            print(instances)
        else:
            print("** class doesn't exist **")
    def do_count(self, arg):
        """Counts the number of instances of a class"""
        class_name = arg.split('.')[0]
        if class_name in self.models:
            instances = models.storage.all(self.models[class_name])
            print(len(instances))
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            splitted = arg.strip().split()
            if splitted[0] not in self.models:
                print("** class doesn't exist **")
            elif len(splitted) < 2:
                print("** instance id missing **")
            else:
                instance_id = splitted[1]
                instance_key = "{}.{}".format(splitted[0], instance_id)
                if instance_key in models.storage.all():
                    del models.storage.all()[instance_key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            splitted = arg.strip().split()
            if splitted[0] not in self.models:
                print("** class doesn't exist **")
            elif len(splitted) < 2:
                print("** instance id missing **")
            else:
                instance_id = splitted[1].replace("\"", "")
                instance_key = "{}.{}".format(splitted[0], instance_id)
                if instance_key not in models.storage.all():
                    print("** no instance found **")
                else:
                    if len(splitted) < 3:
                        print("** attribute name missing **")
                    elif len(splitted) < 4:
                        if "{" in splitted[2] and "}" in splitted[2]:
                            try:
                                update_obj = json.loads(splitted[2])
                                for object_key, value in update_obj.items():
                                    setattr(models.storage.all()[instance_key],
                                            object_key, value)
                                models.storage.save()
                            except Exception as e:
                                print(e)
                        else:
                            print("** value missing **")
                    else:
                        setattr(models.storage.all()[instance_key],
                                splitted[2].replace("\"", ""),
                                splitted[3].replace("\"", ""))
                        models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
