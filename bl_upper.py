"""
This module contains functions that perform various operations on log
files, such as reading, filtering, searching, and sorting logs.
"""


from bl_lower import (
    out_blue,
    out_blue_bg,
    out_green,
    out_italics,
    out_red,
    out_red_bold,
    out_yellow,
)


def input_file_name():
    """
    Takes user input for a file name and returns the input as a string.
    """
    res = input("Enter file name: ")
    print()
    return res


def commands():
    """
    Print a list of commands and prompt the user for input.
    """
    print(out_blue_bg("List of commands:"), "\n")
    print(
        out_blue("\t1 - read"),
        out_blue("\t2 - filter"),
        out_blue("\t3 - search"),
        out_blue("\t4 - sort"),
        out_blue("\tq - quit"),
        out_blue("\t0 - reset filters\n"),
    )
    res = input("Enter command: ")
    if res not in ["1", "2", "3", "4", "q", "0"]:
        print()
        print(out_red_bold("ERROR! Command not found"), "\n")
    else:
        return res


logs = []


def read_logs(file_name):
    """
    Reads logs from the specified file and stores them in a global variable.
    """
    log_file = file_name
    try:
        with open(log_file, "r") as f:
            global log
            log = "".join([f.read()]).split("\n")
            print(
                out_blue_bg(
                    f"I'm reading logs from {out_italics(log_file)}{out_blue_bg(' ')}{out_blue_bg('for you: ')}"
                )
            )
            print()
            for i in log:
                print("\t", i)
                logs.append(i)
            print()
    except FileNotFoundError:
        print(out_red_bold("ERROR! File not found"), "\n")


def filter_logs(logg):
    """
    Filter the logs based on the user's input.
    """
    if logg == []:
        print()
        return print(out_red_bold("ERROR! Read log file first"), "\n")
    INFO = [i for i in logg if "INFO" in i]
    WARNING = [i for i in logg if "WARNING" in i]
    ERROR = [i for i in logg if "ERROR" in i]
    print("Enter filter:")
    res = input(
        f"\t{out_green('i - INFO')}, \t{out_yellow('w - WARNING')}, \t{out_red('e - ERROR')}: "
    )
    print()
    logg.clear()
    if res == "i":
        print(out_green("INFO:"), "\n")
        for i in INFO:
            print("\t", i)
            logg.append(i)
    elif res == "w":
        print(out_yellow("WARNING:"), "\n")
        for i in WARNING:
            print("\t", i)
            logg.append(i)
    elif res == "e":
        print(out_red("ERROR:"), "\n")
        for i in ERROR:
            print("\t", i)
            logg.append(i)
    print()


def search_logs(logg):
    """
    Searches for a given query in the log files.
    """
    if logg == []:
        print()
        return print(out_red_bold("ERROR! Read log file first"), "\n")
    res = input("Enter search: ")
    logs = logg.copy()
    logg.clear()
    print()
    print(out_blue_bg(f"Search query for {out_italics(res)}{out_blue_bg(':')}"), "\n")
    res = res.lower()
    for i in logs:
        if res in i.lower():
            print("\t", i)
            logg.append(i)
    print()


def sort_logs(logg):
    """
    Sorts the logs in either ascending or descending order.
    """
    if logg == []:
        print()
        return print(out_red_bold("ERROR! Read log file first"), "\n")
    logs_ascending = sorted(logg)
    logs_descending = sorted(logg, reverse=True)
    print("Enter sort: ")
    res = input(out_blue("\ta - ascending, \td - descending: "))
    logg.clear()
    print()
    if res == "a":
        print(out_blue_bg("Ascending order:"), "\n")
        for i in logs_ascending:
            print("\t", i)
            logg.append(i)
    elif res == "d":
        print(out_blue_bg("Descending order:"), "\n")
        for i in logs_descending:
            print("\t", i)
            logg.append(i)
    print()


def reset_filters(logg):
    """
    Resets the filters of the given logg.
    """
    if logg == []:
        print()
        return print(out_red_bold("ERROR! Read log file first"), "\n")
    logg.clear()
    print()
    print(out_blue_bg("Reset filters:"), "\n")
    for i in log:
        logg.append(i)
    for i in logg:
        print("\t", i)
    print()
