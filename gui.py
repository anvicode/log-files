"""
This module contains greetings() and bye() messages.
"""
from bl_lower import out_blue_bg, out_green_bg


def greetings():
    """
    A function that prints a greeting message for user.
    """
    print(out_green_bg("""~~~~~Greetings! I am ready to read logs for you!~~~~~"""))
    print()


def bye():
    """
    Prints a farewell message and asks for confirmation from user
    before exiting the program.
    """
    print()
    print(out_blue_bg("You are leaving... "), end="")
    res = input(f"{out_blue_bg('Are you sure? (y/n)')} ")
    if res == "y":
        print()
        print(out_blue_bg("Bye!"), "\n")
    else:
        print()
        print(out_green_bg("Great! Glad you staying!"), "\n")
    return res
