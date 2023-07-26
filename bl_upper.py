def input_file_name():
    res = input("Enter file name: ")
    return res


def read_logs():
    log_file = input_file_name()
    with open(log_file, "r") as f:
        logs = "".join([f.read()]).split("\n")
        print(f"{log_file} logs: ")
        for i in logs:
            print("\t", i)


def filter_logs():
    # log_file = input_file_name()
    log_file = "log_file.log"
    with open(log_file, "r") as f:
        logs = "".join([f.read()]).split("\n")
        print(f"{log_file} logs: ")
        # print(logs)
        INFO = [i for i in logs if "INFO" in i]
        WARNING = [i for i in logs if "WARNING" in i]
        ERROR = [i for i in logs if "ERROR" in i]
        print("Enter filter:")
        res = input("i - INFO, w - WARNING, e - ERROR: ")
        if res == "i":
            for i in INFO:
                print("\t", i)
        elif res == "w":
            for i in WARNING:
                print("\t", i)
        elif res == "e":
            for i in ERROR:
                print("\t", i)
        # print(INFO)
        # print(WARNING)
        # print(ERROR)
        # for i in logs:
        #     print("\t", i)


def search_logs():
    log_file = "log_file.log"
    with open(log_file, "r") as f:
        logs = "".join([f.read()]).split("\n")
        print(f"{log_file} logs: ")
        res = input("Enter search: ").lower()
        for i in logs:
            if res in i.lower():
                print("\t", i)


def sort_logs():
    pass
