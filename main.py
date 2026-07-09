import tkinter as tk

from theme.config import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    WINDOW_TITLE
)

from views.dashboard_view import DashboardView
from PIL import Image, ImageTk

from theme.theme_manager import ThemeManager


class BibliotecaPortoApp:

    LARGURA = WINDOW_WIDTH
    ALTURA = WINDOW_HEIGHT

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(WINDOW_TITLE)

        self.root.geometry(
            self.centralizar_janela(
                self.LARGURA,
                self.ALTURA
            )
        )

        self.root.resizable(False, False)

        self.theme = ThemeManager()

        caminho = self.theme.get_background("bg_01_dashboard.png")

        imagem = Image.open(caminho)
        imagem = imagem.resize((self.LARGURA, self.ALTURA))

        self.background = ImageTk.PhotoImage(imagem)

        self.label_background = tk.Label(
            self.root,
            image=self.background
        )

        self.label_background.place(
            x=0,
            y=0,
            width=self.LARGURA,
            height=self.ALTURA
        )

    def centralizar_janela(self, largura, altura):

        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2

        return f"{largura}x{altura}+{x}+{y}"

    def executar(self):

        self.root.mainloop()


if __name__ == "__main__":

    app = BibliotecaPortoApp()
    app.executar()