#!/usr/bin/python3
"""
This is console module
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Our HBNB command class
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """ If this method is overriddes, the built in emptyline
            function which repeats the last nonempty command entered.
        """
        return

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()
