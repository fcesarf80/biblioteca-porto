import tkinter as tk
from PIL import Image, ImageTk


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
        image_path=None,
        command=None
    ):

        super().__init__(
            master,
            width=width,
            height=height,
            bd=0,
            highlightthickness=0
        )

        self.place(x=x, y=y)

        if image_path:
            imagem = Image.open(image_path)
            imagem = imagem.resize((width, height))
            self.imagem = ImageTk.PhotoImage(imagem)
        else:
            self.imagem = None

        self.button = tk.Button(
            self,
            image=self.imagem,
            command=command,
            relief="flat",
            bd=0,
            highlightthickness=0,
            cursor="hand2",
            borderwidth=0
        )

        self.button.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        self.button.lift()