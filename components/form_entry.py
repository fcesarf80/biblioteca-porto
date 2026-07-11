import tkinter as tk


class FormEntry(tk.Entry):

    DEFAULT_FONT = ("Segoe UI", 10)
    DEFAULT_FOREGROUND = "#2F2F2F"
    DEFAULT_BACKGROUND = "#FFFFFF"
    DEFAULT_BORDER = 1

    def __init__(
        self,
        master,
        x,
        y,
        width,
        height=28,
        font=DEFAULT_FONT,
        foreground=DEFAULT_FOREGROUND,
        background=DEFAULT_BACKGROUND,
        border=DEFAULT_BORDER,
        justify="left"
    ):

        super().__init__(
            master,
            font=font,
            fg=foreground,
            bg=background,
            bd=border,
            justify=justify
        )

        self.place(
            x=x,
            y=y,
            width=width,
            height=height
        )

    def get_value(self):

        return self.get().strip()

    def set_value(
        self,
        value
    ):

        self.delete(
            0,
            tk.END
        )

        self.insert(
            0,
            value
        )

    def clear(self):

        self.delete(
            0,
            tk.END
        )