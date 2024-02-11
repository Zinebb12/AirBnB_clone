#!/usr/bin/python3
""" Module for the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self):
        """Exits console"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """"Provide help to quit the program"""
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
