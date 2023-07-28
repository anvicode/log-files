import bl_upper
import gui


def lifetime():
    while True:
        res = bl_upper.commands()
        if res == "q":
            quit = gui.bye()
            if quit == "y":
                break
            else:
                continue
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
