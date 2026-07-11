import tkinter as tk


class ActionButton(tk.Button):

    DEFAULT_FONT = ("Segoe UI", 10, "bold")
    DEFAULT_FOREGROUND = "#FFFFFF"
    DEFAULT_BORDER = 0

    def __init__(
        self,
        master,
        text,
        x,
        y,
        width,
        height,
        background,
        command
    ):

        super().__init__(
            master,
            text=text,
            font=self.DEFAULT_FONT,
            fg=self.DEFAULT_FOREGROUND,
            bg=background,
            bd=self.DEFAULT_BORDER,
            activebackground=background,
            activeforeground=self.DEFAULT_FOREGROUND,
            cursor="hand2",
            command=command
        )

        self.place(
            x=x,
            y=y,
            width=width,
            height=height
        )