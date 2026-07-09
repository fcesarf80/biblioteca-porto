import tkinter as tk


class SidebarButton(tk.Button):

    def __init__(
        self,
        master,
        text,
        command=None
    ):

        super().__init__(
            master,
            text=text,
            command=command,
            relief="flat",
            borderwidth=0,
            cursor="hand2",
            anchor="w",
            padx=20,
            font=("Segoe UI", 11)
        )

        self.configure(
            width=20,
            height=2
        )