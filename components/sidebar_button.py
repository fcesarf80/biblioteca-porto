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
            highlightthickness=0,
            cursor="hand2",
            anchor="w",
            padx=15,
            font=("Segoe UI", 11, "bold"),
            bg="#FFFFFF",
            activebackground="#F5F5F5",
            fg="#0D47A1",
            activeforeground="#0D47A1"
        )

        self.configure(
            width=20,
            height=2
        )