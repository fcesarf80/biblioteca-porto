import tkinter as tk
from PIL import Image, ImageTk
from theme.config import WINDOW_HEIGHT, WINDOW_WIDTH


class BaseView(tk.Frame):

    def __init__(self, master, theme, background):

        super().__init__(
            master,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            bd=0,
            highlightthickness=0,
        )

        self.place(x=0, y=0)

        self.theme = theme

        caminho = self.theme.get_background(background)

        print(caminho)
        print(caminho.exists())

        imagem = Image.open(caminho)
        imagem = imagem.resize((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.background = ImageTk.PhotoImage(imagem)

        self.canvas = tk.Canvas(
            self,
            bg="red",
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            bd=0,
            highlightthickness=0,
        )
        self.canvas.place(x=0, y=0)

        self.canvas.create_image(0, 0, image=self.background, anchor="nw")
        
        self.canvas.image = self.background
