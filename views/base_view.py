import tkinter as tk

from PIL import Image, ImageTk

from theme.config import WINDOW_WIDTH, WINDOW_HEIGHT
from theme.theme_manager import ThemeManager


class BaseView(tk.Frame):

    def __init__(self, master, background):

        super().__init__(master)

        self.place(
            x=0,
            y=0,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT
        )

        self.theme = ThemeManager()

        caminho = self.theme.get_background(background)

        imagem = Image.open(caminho)
        imagem = imagem.resize((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.background = ImageTk.PhotoImage(imagem)

        self.label_background = tk.Label(
            self,
            image=self.background
        )

        self.label_background.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )