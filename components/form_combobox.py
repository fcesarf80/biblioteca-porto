import tkinter as tk
from tkinter import ttk


class FormComboBox(ttk.Combobox):

    DEFAULT_FONT = ("Segoe UI", 10)

    style_created = False

    def __init__(
        self,
        master,
        values,
        x,
        y,
        width
    ):

        if not FormComboBox.style_created:

            style = ttk.Style(master)

            style.theme_use("default")

            style.configure(
                "Custom.TCombobox",
                foreground="black",
                fieldbackground="white",
                background="white",
                insertcolor="black",
                borderwidth=1,
                relief="solid"
            )

            style.map(
                "Custom.TCombobox",
                fieldbackground=[("readonly", "white")],
                background=[("readonly", "white")],
                foreground=[("readonly", "black")]
            )

            FormComboBox.style_created = True

        super().__init__(
            master,
            values=values,
            state="readonly",
            font=self.DEFAULT_FONT,
            style="Custom.TCombobox"
        )

        self.place(
            x=x,
            y=y,
            width=width,
            height=28
        )

    def get_value(self):

        return self.get()

    def set_value(
        self,
        value
    ):

        self.set(value)

    def set_values(
        self,
        values
    ):

        self["values"] = values

    def clear(self):

        self.set("")