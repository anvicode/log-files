import controller
import gui


def main():
    gui.greetings()
    controller.bl_upper_read_all_logs()
    controller.bl_upper_read_line()


if __name__ == "__main__":
    main()
