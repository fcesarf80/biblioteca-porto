import tkinter as tk
from tkinter import ttk


class TopBar(tk.Frame):

    HEIGHT = 30

    def __init__(
        self,
        master,
        on_theme_change
    ):

        super().__init__(
            master,
            bg=master.cget("bg"),
            bd=0,
            highlightthickness=0
        )

        self.place(
            x=1080,
            y=15,
            width=150,
            height=30
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
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )
