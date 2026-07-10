import tkinter as tk


class QuickActionButton(tk.Frame):

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
            bg="#48E65E",
            highlightbackground="#0B6E1A",
            highlightthickness=2,
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