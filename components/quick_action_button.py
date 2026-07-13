import tkinter as tk


class QuickActionButton(tk.Frame):

    def __init__(
        self,
        master,
        x,
        y,
        width,
        height,
        icon="",
        text="",
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

        self.label_icon = tk.Label(
            self,
            text=icon,
            bg="#48E65E",
            fg="white",
            font=("Segoe UI Emoji", 28)
        )

        self.label_icon.place(
            relx=0.5,
            y=18,
            anchor="n"
        )

        self.label_text = tk.Label(
            self,
            text=text,
            bg="#48E65E",
            fg="white",
            font=("Segoe UI", 8)
        )

        self.label_text.place(
            relx=0.5,
            y=68,
            anchor="n"
        )

        self.button = tk.Button(
            self,
            command=command,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
            bg="#48E65E",
            activebackground="#48E65E"
        )

        self.button.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        self.button.lower()