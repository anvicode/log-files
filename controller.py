import bl_upper


def lifetime():
    while True:
        print("List of commands: ")
        print("1 - read, 2 - filter, 3 - search, 4 - sort, q - quit")
        print("0 - reset filters")
        res = input("Enter command: ")
        if res == "q":
            break
        if res == "1":
            bl_upper.read_logs(bl_upper.input_file_name())
        if res == "2":
            bl_upper.filter_logs(bl_upper.logs)
        if res == "3":
            bl_upper.search_logs(bl_upper.logs)
        if res == "4":
            bl_upper.sort_logs(bl_upper.logs)
        if res == "0":
            bl_upper.reset_filters(bl_upper.logs)
