"""
This module contains functions that color the text in the console.
"""


def out_red_bold(text):
    """
    Formats the given text as bold and red.
    """
    return f"\033[31m\033[1m{text}\033[0m"


def out_green_bg(text):
    """
    Returns the given text with a green background.
    """
    return f"\033[42m{text}\033[0m"


def out_blue_bg(text):
    """
    Returns the input text with a blue background in the console.
    """
    return f"\033[44m{text}\033[0m"


def out_blue(text):
    """
    Returns the given text formatted in blue color.
    """
    return f"\033[34m{text}\033[0m"


def out_green(text):
    """
    Returns the given text formatted in green color.
    """
    return f"\033[32m{text}\033[0m"


def out_yellow(text):
    """
    Returns the given text formatted in yellow color.
    """
    return f"\033[33m{text}\033[0m"


def out_red(text):
    """
    Returns the given text formatted in red color.
    """
    return f"\033[31m{text}\033[0m"


def out_italics(text):
    """
    Returns the given text formatted in italics.
    """
    return f"\033[3m{text}\033[0m"
