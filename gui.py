from bl_lower import out_blue_bg, out_green_bg


def greetings():
    # print("\033[31mGreetings! I am ready to read logs for you!\033[0m")
    print(out_green_bg("""~~~~~Greetings! I am ready to read logs for you!~~~~~"""))
    print()


def bye():
    print()
    print(out_blue_bg("You are leaving... "), end="")
    res = input(f"{out_blue_bg('Are you sure? (y/n)')} ")
    if res == "y":
        print()
        print(out_blue_bg("Bye!"), "\n")
    else:
        print()
        print(out_green_bg("Great! Glad you staying!"), "\n")
    return res
