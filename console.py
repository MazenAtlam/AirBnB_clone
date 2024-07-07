#!/usr/bin/python3
"""
Module Defining the command line interpreter
"""
import cmd


class HBNHCommand(cmd.Cmd):
    """
    Command Interpreter class
    Defines features and options
    delivered by the CLI
    """
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNHCommand().cmdloop()
