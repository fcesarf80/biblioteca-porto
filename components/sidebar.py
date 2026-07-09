import tkinter as tk


class Sidebar(tk.Frame):

    WIDTH = 250

    def __init__(self, master):

        super().__init__(
            master,
            width=self.WIDTH,
            bg="#1E293B"
        )

        self.place(
            x=0,
            y=0,
            relheight=1
        )