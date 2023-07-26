import bl_upper


def lifetime():
    while True:
        print("List of commands: ")
        print("1 - read, 2 - filter, 3 - search, 4 - sort, q - quit")
        res = input("Enter command: ")
        if res == "q":
            break
        if res == "1":
            bl_upper.read_logs()
        elif res == "2":
            bl_upper.filter_logs()
        elif res == "3":
            bl_upper.search_logs()
        elif res == "4":
            pass
        # print(res)
