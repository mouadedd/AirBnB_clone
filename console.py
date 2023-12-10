#!/usr/bin/python3
"""Define the project's console"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Define the command interpreter"""
    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "State",
                 "City", "Place", "Amenity", "Review"}

    def do_quit(self, arg):
        """Quit to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        print("")
        return True

    def emptyline(self):
        """pass when an empty line recieved"""
        pass

    def do_create(self, arg):
        """ Create a new class instance and print its id
        """
        arg_len = shlex.split(arg)
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_len[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation
        of an instance based on the class name and id.
        """
        arg_len = shlex.split(arg)
        objdict = storage.all()
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_len) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_len[0], arg_len[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg_len[0], arg_len[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        arg_len = shlex.split(arg)
        objdict = storage.all()
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_len) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_len[0], arg_len[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arg_len[0], arg_len[1])]
            storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances
        based or not on the class name."""
        arg_len = shlex.split(arg)
        if len(arg_len) > 0 and arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_len = []
            for obj in storage.all().values():
                if len(arg_len) > 0 and arg_len[0] == obj.__class__.__name__:
                    obj_len.append(obj.__str__())
                elif len(arg_len) == 0:
                    obj_len.append(obj.__str__())
            print(obj_len)

    def do_update(self, arg):
        """Update instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)."""
        arg_len = shlex.split(arg)
        objdict = storage.all()

        if len(arg_len) == 0:
            print("** class name missing **")
            return False
        if arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_len) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_len[0], arg_len[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arg_len) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_len) == 3:
            try:
                type(eval(arg_len[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_len) == 4:
            obj = objdict["{}.{}".format(arg_len[0], arg_len[1])]
            if arg_len[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_len[2]])
                obj.__dict__[arg_len[2]] = valtype(arg_len[3])
            else:
                obj.__dict__[arg_len[2]] = arg_len[3]
        elif type(eval(arg_len[2])) == dict:
            obj = objdict["{}.{}".format(arg_len[0], arg_len[1])]
            for key, value in eval(arg_len[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key])
                        in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
