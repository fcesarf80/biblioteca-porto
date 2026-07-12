import tkinter as tk
from tkinter import ttk


class FormComboBox(ttk.Combobox):

    DEFAULT_FONT = ("Segoe UI", 10)

    def __init__(
        self,
        master,
        values,
        x,
        y,
        width
    ):

        super().__init__(
            master,
            values=values,
            state="readonly",
            font=self.DEFAULT_FONT
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