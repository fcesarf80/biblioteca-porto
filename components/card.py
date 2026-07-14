import tkinter as tk
from PIL import Image, ImageTk


class Card(tk.Frame):

    def __init__(
        self,
        master,
        x,
        y,
        width,
        height,
        image_path=None,
        command=None
    ):

        super().__init__(
            master,
            width=width,
            height=height,
            bg="#ECECEC",
            highlightthickness=0,
            bd=0
        )
        self.place(
            x=x,
            y=y
        )

        if image_path:

            imagem = Image.open(image_path)
            imagem = imagem.resize((width, height))

            self.imagem = ImageTk.PhotoImage(imagem)

            self.background = tk.Label(
                self,
                image=self.imagem,
                bd=0
            )

            self.background.place(
                x=0,
                y=0,
                relwidth=1,
                relheight=1
            )

        self.label_valor = tk.Label(
            self,
            text="0",
            font=("Segoe UI", 28, "bold"),
            bg="#FDF9F0",
            fg="#1E3A8A"
        )

        self.label_valor.place(
            relx=0.5,
            y=25,
            anchor="n"
        )

        self.label_titulo = tk.Label(
            self,
            text="",
            font=("Segoe UI", 10),
            bg="#FDF9F0",
            fg="#475569"
        )

        self.label_titulo.place(
            relx=0.5,
            y=78,
            anchor="n"
        )

        self.button = tk.Button(
            self,
            command=command,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
            bg=self["bg"],
            activebackground=self["bg"]
        )

        self.button.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        self.button.lower()

    def set_data(
        self,
        titulo,
        valor
    ):

        self.label_titulo.config(
            text=titulo
        )

        self.label_valor.config(
            text=str(valor)
        )