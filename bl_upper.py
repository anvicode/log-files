def input_file_name():
    res = input("Enter file name: ")
    return res


logs = []


def read_logs(file_name):
    # log_file = input_file_name()
    log_file = file_name
    with open(log_file, "r") as f:
        global log
        log = "".join([f.read()]).split("\n")
        print(f"{log_file} logs: ")
        for i in log:
            print("\t", i)
            logs.append(i)
    # print(logs)
    # print(log)
    # return logs
    # print(logs)


def filter_logs(logg):
    if logg == []:
        return print("ERROR! Read log file first")
    # print(logg)
    INFO = [i for i in logg if "INFO" in i]
    WARNING = [i for i in logg if "WARNING" in i]
    ERROR = [i for i in logg if "ERROR" in i]
    print("Enter filter:")
    res = input("i - INFO, w - WARNING, e - ERROR: ")
    logg.clear()
    if res == "i":
        for i in INFO:
            print("\t", i)
            logg.append(i)
    elif res == "w":
        for i in WARNING:
            print("\t", i)
            logg.append(i)
    elif res == "e":
        for i in ERROR:
            print("\t", i)
            logg.append(i)
    # log_file = input_file_name()
    # log_file = "log_file.log"
    # with open(log_file, "r") as f:
    #     logs = "".join([f.read()]).split("\n")
    #     print(f"{log_file} logs: ")
    #     print(logs)
    #     INFO = [i for i in logs if "INFO" in i]
    #     WARNING = [i for i in logs if "WARNING" in i]
    #     ERROR = [i for i in logs if "ERROR" in i]
    #     print("Enter filter:")
    #     res = input("i - INFO, w - WARNING, e - ERROR: ")
    #     if res == "i":
    #         for i in INFO:
    #             print("\t", i)
    #     elif res == "w":
    #         for i in WARNING:
    #             print("\t", i)
    #     elif res == "e":
    #         for i in ERROR:
    #             print("\t", i)


def search_logs(logg):
    if logg == []:
        return print("ERROR! Read log file first")
    # print(logg)
    res = input("Enter search: ").lower()
    logs = logg.copy()
    logg.clear()
    for i in logs:
        if res in i.lower():
            print("\t", i)
            logg.append(i)
    # log_file = "log_file.log"
    # with open(log_file, "r") as f:
    #     logs = "".join([f.read()]).split("\n")
    #     print(f"{log_file} logs: ")
    #     res = input("Enter search: ").lower()
    #     for i in logs:
    #         if res in i.lower():
    #             print("\t", i)


def sort_logs(logg):
    if logg == []:
        return print("ERROR! Read log file first")
    # print(logg)
    logs_ascending = sorted(logg)
    logs_descending = sorted(logg, reverse=True)
    print("Enter sort: ")
    res = input("a - ascending, d - descending: ")
    logg.clear()
    if res == "a":
        for i in logs_ascending:
            print("\t", i)
            logg.append(i)
    elif res == "d":
        for i in logs_descending:
            print("\t", i)
            logg.append(i)
    # log_file = "log_file.log"
    # with open(log_file, "r") as f:
    #     logs_ascending = sorted("".join([f.read()]).split("\n"))
    #     logs_descending = sorted(logs_ascending, reverse=True)
    #     print("Enter sort: ")
    #     res = input("a - ascending, d - descending: ")
    #     print(f"{log_file} logs: ")
    #     if res == "a":
    #         for i in logs_ascending:
    #             print("\t", i)
    #     elif res == "d":
    #         for i in logs_descending:
    #             print("\t", i)


def reset_filters(logg):
    if logg == []:
        return print("ERROR! Read log file first")
    logg.clear()
    for i in log:
        logg.append(i)
    # print(logg)
    for i in logg:
        print("\t", i)
