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
        elif res == "1":
            bl_upper.read_logs(bl_upper.input_file_name())
        elif res == "2":
            bl_upper.filter_logs(bl_upper.logs)
        elif res == "3":
            bl_upper.search_logs(bl_upper.logs)
        elif res == "4":
            bl_upper.sort_logs(bl_upper.logs)
        elif res == "0":
            bl_upper.reset_filters(bl_upper.logs)
