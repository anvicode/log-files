from bl_lower import read_logs
from gui import get_user_command


def lifetime():
    command = get_user_command()
    while True:
        if command == "0":
            return command
        if command == "1":
            # logs = read_logs
            return read_logs()
        else:
            print("Unknown command")
            command = get_user_command()


def read_all_logs():
    read_logs()
