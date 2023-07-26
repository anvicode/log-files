def read_logs():
    with open("log_file.log", "r") as f:
        file = "".join([f.read()]).split("\n")
        # print(file)
        for i in range(len(file)):
            print(file[i])


def next_step():
    print("\t   What do you want to do?")
    info()


def info():
    print("The following commands are available to you:")
    print("1. Read all logs")
    print("0. Exit")
