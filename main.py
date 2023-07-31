"""
This file contains the implementation of a command-line interface (CLI)
for log file operations.

The CLI provides a set of commands that allow users to perform various
operations on log files, such as reading, filtering, searching, and sorting. 

Usage:
    $ python main.py
"""
import controller
import gui


def main():
    """
    Execute the main function.
    """
    gui.greetings()
    controller.lifetime()


if __name__ == "__main__":
    main()
