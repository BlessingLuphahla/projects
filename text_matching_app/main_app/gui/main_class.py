from abc import ABC, abstractmethod


class MainClass(ABC):
    @abstractmethod
    def __init__(self, master):
        # setting up the master
        self.master = master
        self.master.title('Redd Axe Text Analyser'.upper())
        self.master.geometry('2000x2000')
        self.master_bg_color = '#1e1e1e'
        self.master.config(bg=self.master_bg_color)

        # setting Up Constants
        self.top_level_lasting_period = 90_000
