import tkinter as tk


class TopBar(tk.Frame):

    HEIGHT = 70

    def __init__(self, master):

        super().__init__(
            master,
            height=self.HEIGHT,
            bg="#334155"
        )

        self.place(
            x=250,
            y=0,
            relwidth=1,
            width=-250
        )