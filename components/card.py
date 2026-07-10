import tkinter as tk


class Card(tk.Frame):

    def __init__(
        self,
        master,
        x,
        y,
        width,
        height,
        command=None
    ):

        super().__init__(
            master,
            width=width,
            height=height,
            highlightthickness=0,
            bd=0
        )

        self.place(
            x=x,
            y=y
        )

        self.button = tk.Button(
            self,
            command=command,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2"
        )

        self.button.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )