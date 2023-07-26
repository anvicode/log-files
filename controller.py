import bl_upper


def bl_upper_lifetime():
    while True:
        command = bl_upper.lifetime()
        bl_upper.lifetime()
        if command == "0":
            break
