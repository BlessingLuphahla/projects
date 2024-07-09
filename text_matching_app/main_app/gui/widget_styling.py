from tkinter import SUNKEN, CENTER


def button_settings() -> dict:
    return {

        'width': 16, 'font': ('impact', 30), 'borderwidth': 10,
        'fg': 'black', 'bg': '#ffa', 'highlightbackground': 'blue',
        'activebackground': 'black', 'activeforeground': 'white',
        'highlightthickness': 2, 'anchor': CENTER

    }


def button_grid_settings() -> dict:
    return {

        'padx': (200, 0), 'pady': (50, 0)

    }


def menu_settings() -> dict:
    return {

        'font': ('impact', 20), 'bg': 'black', 'fg': 'white',

    }


def entry_bar_settings() -> dict:
    return {

        'width': 45, 'font': ('helvetica', 36), 'relief': SUNKEN, 'borderwidth': 10,
        'border': 3, 'fg': '#1e1e1e', 'bg': '#ffa', 'highlightthickness': 4

    }


def entry_grid_settings() -> dict:
    return {

        'padx': (0, 0), 'pady': (40, 0), 'column': 1, 'columnspan': 2

    }


def label_settings(self) -> dict:
    return {

        'font': ('impact', 28),
        'fg': 'white', 'bg': self.master_bg_color

    }


def label_grid_settings() -> dict:
    return {

        'padx': (20, 0), 'pady': (40, 0)

    }


def menu_configuration():
    return {

        'tearoff': 0

    }


def information_label_settings():
    return {

        'font': ('helvetica', 20),
        'fg': 'white',

    }
