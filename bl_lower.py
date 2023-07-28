def out_red_bold(text):
    return f"\033[31m\033[1m{text}\033[0m"


def out_green_bg(text):
    return f"\033[42m{text}\033[0m"


def out_blue_bg(text):
    return f"\033[44m{text}\033[0m"


def out_blue(text):
    return f"\033[34m{text}\033[0m"


def out_green(text):
    return f"\033[32m{text}\033[0m"


def out_yellow(text):
    return f"\033[33m{text}\033[0m"


def out_red(text):
    return f"\033[31m{text}\033[0m"


def out_italics(text):
    return f"\033[3m{text}\033[0m"
