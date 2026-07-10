import tkinter as tk


class ActivityPanel(tk.Frame):

    def __init__(
        self,
        master,
        x,
        y,
        width,
        height
    ):

        super().__init__(
            master,
            width=width,
            height=height,
            bg="#48E65E",
            highlightbackground="#0B6E1A",
            highlightthickness=2,
            bd=0
        )

        self.place(
            x=x,
            y=y
        )