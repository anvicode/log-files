# open the file


def read_all_logs():
    with open("log_file.log", "r") as f:
        print(f.read())
