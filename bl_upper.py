def read_all_logs():
    with open("log_file.log", "r") as f:
        print(f.read())


def read_line():
    with open("log_file.log", "r") as f:
        file = "".join([f.read()])
        file = file.split("\n")
        # file = "\n".join(file)
        for i in range(len(file)):
            print(file[i])
        # print(f.readline())
