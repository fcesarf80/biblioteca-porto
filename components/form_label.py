import tkinter as tk


class FormLabel(tk.Label):

    DEFAULT_FONT = ("Segoe UI", 10, "normal")
    DEFAULT_FOREGROUND = "#05148e"
    DEFAULT_BACKGROUND = "#F0F0F0"

    def __init__(
        self,
        master,
        text,
        x,
        y,
        width=90,
        font=DEFAULT_FONT,
        foreground=DEFAULT_FOREGROUND,
        background=DEFAULT_BACKGROUND,
        anchor="w"
    ):

        super().__init__(
            master,
            text=text,
            font=font,
            fg=foreground,
            bg=background,
            anchor=anchor
        )

        self.place(
            x=x,
            y=y,
            width=width
        )