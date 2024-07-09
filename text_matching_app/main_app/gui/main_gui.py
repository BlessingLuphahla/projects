from sys import exit
from widget_creation import Widgets
from tkinter import Tk


def main() -> None:
    try:

        root = Tk()
        Widgets(root)
        root.mainloop()

    except KeyboardInterrupt:
        print('you chose to exit')
        exit(0)

    return None


if __name__ == '__main__':
    main()
