from tkinter import colorchooser, filedialog
from package_utils import *
from text_labels import text_for_information_panel
from confirmations import confirm
from widget_styling import information_label_settings


class ButtonCommands(MainClass):

    def __init__(self, master):
        super().__init__(master)

    def change_master_color(self):
        color = colorchooser.askcolor(initialcolor=self.master_bg_color)
        color = str(color[1])

        self.master.config(bg=color)

        for _, child in self.master.children.items():
            if isinstance(child, Label):
                child.configure(cnf={'bg': color})

    def change_button_color(self):
        color = colorchooser.askcolor(initialcolor='yellow')
        color = str(color[1])

        if color is None:
            color = '#000000'

        for _, child in self.master.children.items():
            if isinstance(child, Button):

                if color == '#000000':
                    child.configure(cnf={'bg': color, 'fg': 'white'})

                else:
                    child.configure(cnf={'bg': color, 'fg': '#000000'})

    def change_entry_color(self):
        color = colorchooser.askcolor(initialcolor=self.master_bg_color)
        color = str(color[1])

        for _, child in self.master.children.items():
            if isinstance(child, Entry):
                if color == '#000000':
                    child.configure(cnf={'bg': color, 'fg': 'white'})

                else:
                    child.configure(cnf={'bg': color, 'fg': '#000000'})

    def change_label_color(self):
        color = colorchooser.askcolor(initialcolor=self.master_bg_color)
        color = str(color[1])

        for _, child in self.master.children.items():
            if isinstance(child, Label):
                child.configure(cnf={'fg': color})

    def font_changes(self) -> None:
        options = [str(i) for i in range(15, 30 + 1)]
        selected_size = StringVar()
        selected_size.set('30')

        top_level = self.invoke_top_level('font size', '150x120', bg='#fff')

        option_menu = OptionMenu(top_level, selected_size, *options,
                                 command=lambda value: self.change_button_font_size(value))
        option_menu.grid(row=0, column=0, pady=(22, 0), padx=(22, 0))
        option_menu.configure(bg='#000', font=('impact', 40), fg='#fff')

        return None

    def change_button_font_size(self, value):

        for name, child in self.master.children.items():
            if 'button' in name:
                child.configure(cnf={'font': ('impact', value)})

    def invoke_top_level(self, title: str, geometry: str = '1000x800', bg=None):

        if bg is None:
            bg = self.master_bg_color

        top_level = Toplevel(master=self.master)
        top_level.config(bg=bg)
        top_level.geometry(geometry)
        top_level.title(title.upper())

        return top_level

    def information_panel(self) -> None:
        top_level = self.invoke_top_level('redd axe information panel', geometry='800x600')
        # Setting Up Frame

        main_top_level_frame = Frame(master=top_level, bg='white', width=2000)
        main_top_level_frame.grid()

        # setting Up Labels

        label = Label(

            master=main_top_level_frame, text=text_for_information_panel(),
            bg=self.master_bg_color, cnf=information_label_settings()
        )

        label.grid()

        top_level.after(self.top_level_lasting_period, self.remove_top_levels)

        return None

    def default_values(self) -> None:
        response = confirm('do you wanna put default values')
        if response:
            self.__clear_entries()
            defaults = [

                r'C:\Users',
                r'[\s:.,*\d}\\!?+/><]',
                r'\d{4}/\d{2}/\d{2},\s\d{2}:\d{2}',
                ' REDD AXE:'

            ]

            entries = [entry for entry in self.master.children.values() if isinstance(entry, Entry)]

            for child, default in zip(entries, defaults):

                if isinstance(child, Entry):
                    child: Entry
                    child.insert(0, default)

        return None

    def remove_top_levels(self) -> None:
        for name, child in tuple(self.master.children.items()):
            if 'toplevel' in name.lower():
                child.destroy()

        return None

    def __clear_entries(self):
        for child in self.master.children.values():
            if isinstance(child, Entry):
                child: Entry
                child.delete(0, END)

    def clear_all(self) -> None:
        response = confirm('Do you wanna clear All of The entry Bars')
        if response:
            self.remove_top_levels()
            self.__clear_entries()

        return None

    def location_browse(self) -> None:

        self.remove_top_levels()
        location = filedialog.askopenfilename(title='CLick Me')

        self.master.children['location_entry'].delete(0, END)
        self.master.children['location_entry'].insert(END, location)

        return None

    def collect_information(self) -> Tuple:
        information = []

        for child in self.master.children.values():
            if isinstance(child, Entry):
                info = child.get()
                information.append(info)

        print(information)

        return tuple(information)
