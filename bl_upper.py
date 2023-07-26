import gui


def read_logs():
    with open(gui.file_name(), "r") as f:
        logs = "".join([f.read()]).split("\n")
        for i in logs:
            print(i)


def info():
    """
    Prompts the user to input a choice from a menu and returns the input.
    """
    return input(
        "--> 1. Read\n--> 2. Filter\n--> 3. Search\n--> 4. Sort\n--> 0. Exit\n--> h. Info\n--> "
    )
