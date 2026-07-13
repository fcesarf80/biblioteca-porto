import tkinter as tk
from tkinter import ttk


class TopBar(tk.Frame):

    HEIGHT = 70

    def __init__(
        self,
        master,
        on_theme_change
    ):

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

        self.combo_tema = ttk.Combobox(
            self,
            values=(
                "Porto",
                "Natal",
                "São João"
            ),
            state="readonly"
        )

        self.combo_tema.current(0)

        self.combo_tema.bind(
            "<<ComboboxSelected>>",
            lambda event: on_theme_change(
                self.combo_tema.get()
            )
        )

        self.combo_tema.set("Porto")

        self.combo_tema.place(
            x=760,
            y=20,
            width=150,
            height=30
        )
