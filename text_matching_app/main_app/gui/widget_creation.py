from button_commands import ButtonCommands
from package_utils import *
from widget_styling import *


class Widgets(MainClass):

    @staticmethod
    def create_entries() -> None:

        # Setting up Entries

        rows = [0, 1, 2, 3]
        names = [

            'location_entry', 'regex_entry', 'regex_date_entry',
            'name_regex_match'
        ]

        for row, name in zip(rows, names):
            entry_bar = Entry(cnf=entry_bar_settings(), name=name)
            entry_bar.grid(row=row, cnf=entry_grid_settings())

    def create_labels(self) -> None:
        # Setting up Labels

        rows = [0, 1, 2, 3, 7]
        columns = [0, 0, 0, 0, 1]

        names = [

            'location_label', 'regex_label', 'regex_date_label',
            'regex_name_label', 'main_label'

        ]
        texts = [text.upper() for text in
                 [

                     f'Enter The Location {chr(129304) * 4}: ',
                     f'Enter The Regex {chr(129304) * 5} : ',
                     f'Enter The Regex For Date {chr(129304)} : ',
                     f'Enter The Regex For Name {chr(129304)} : ',
                     self.__main_label_text()
                 ]
                 ]

        for row, name, text, column in zip(rows, names, texts, columns):
            entry_bar = Label(text=text, cnf=label_settings(self), name=name)
            entry_bar.grid(row=row, column=column, cnf=label_grid_settings())

        # setting up main Label

    def create_buttons(self) -> None:
        # Setting up Buttons

        commands = [

            self.commands.clear_all, lambda: print(23),  # TODO deal with this
            self.commands.location_browse, self.commands.default_values,
            self.commands.information_panel, lambda: self.master.quit(),
            lambda: self.commands.invoke_top_level('REDD AXE usage information')

        ]

        rows = [5, 6, 5, 5, 6, 6, 8]
        columns = [0, 0, 1, 2, 1, 2, 0]
        columnspans = [1, 1, 1, 1, 1, 1, 2]

        names = [

            'clear_button', 'run_button', 'browse_location_button',
            'default_button', 'top_level_button', 'exit_button', 'usage_button'

        ]
        texts = [text.upper() for text in
                 [

                     f'Clear All {chr(129397) * 3}',
                     f'Run App {chr(129392) * 3}',
                     f'Browse Location',
                     f'Default values {chr(129392)}',
                     f'Information {chr(129392) * 2}',
                     f'Exit App {chr(129402) * 3}',
                     f'click  me  i  am  the  Usage  Button  {chr(129327) * 3}'

                 ]
                 ]

        for row, name, text, column, command, columnspan in zip(
                rows, names, texts, columns, commands, columnspans
        ):
            button = Button(text=text, cnf=button_settings(), name=name, command=command)
            button.grid(row=row, column=column, columnspan=columnspan, cnf=button_grid_settings())

    def widget_customise(self) -> None:
        self.master.children['main_label'].configure(font=('helvetica', 18), fg='red')
        self.master.children['usage_button'].configure(

            font=('impact', 30), padx=200

        )
        self.master.children['exit_button'].configure(bg='#f22')

    def __init__(self, master) -> None:
        super().__init__(master)

        # setting up command
        self.commands = ButtonCommands(self.master)

        # setting up widgets

        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.widget_customise()

        self.put_menus()

    def put_menus(self) -> None:
        menu = Menu(master=self.master, bg='black', font=('impact', 20))
        menu.configure(bg='#1e1e1e', font=('impact', 20))
        self.master.config(menu=menu)

        # TODO edit the functions for these guys please you not done
        #  and fix this bullshit code here

        font_settings_menu = Menu(cnf=menu_configuration())
        font_settings_menu.configure(cnf=menu_settings())
        menu.add_cascade(label='font settings'.upper(), menu=font_settings_menu)

        color_settings_menu = Menu(cnf=menu_configuration())
        color_settings_menu.configure(cnf=menu_settings())
        menu.add_cascade(label='Color settings'.upper(), menu=color_settings_menu)

        self.create_font_settings_menu(menu=font_settings_menu)
        self.create_color_settings_menu(menu=color_settings_menu)

    def create_font_settings_menu(self, menu: Menu):
        labels = [label.upper() for label in
                  [

                      'change button font',
                      'change entry font',
                      'change label font'

                  ]
                  ]
        commands = [

            self.commands.font_changes,
            self.commands.font_changes,
            self.commands.font_changes

        ]

        for label, command in zip(labels, commands):
            menu.add_command(label=label, command=command)

    def create_color_settings_menu(self, menu: Menu):
        labels = [label.upper() for label in
                  [

                      'change background color', 'change the button colors',
                      'change the entry bar colors',
                      'change the label bar colors'

                  ]
                  ]
        commands = [

            self.commands.change_master_color, self.commands.change_button_color,
            self.commands.change_entry_color, self.commands.change_label_color

        ]

        for label, command in zip(labels, commands):
            menu.add_command(label=label, command=command)

    @staticmethod
    def __main_label_text():
        welcome = f'This application was created by REDD AXE  {chr(129304)} {chr(129293) * 3} !!!!!'
        warning = f'Please Click The Usage Button Before Use {chr(129301) * 3}'

        newlines = '\n' * 1

        return welcome + newlines + warning
