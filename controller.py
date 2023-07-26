import bl_upper


def read():
    return bl_upper.read_logs()


def lifetime():
    # res = bl_upper.info()
    res = input(
        "--> 1. Read\n--> 2. Filter\n--> 3. Search\n--> 4. Sort\n--> 0. Exit\n--> h. Info\n--> "
    )

    while True:
        if res == "0":
            break
        if res == "1":
            read()
        elif res == "h":
            bl_upper.info()
