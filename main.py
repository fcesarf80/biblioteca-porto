import tkinter as tk

from theme.config import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    WINDOW_TITLE
)

from views.dashboard_view import DashboardView
from utils.screen_manager import ScreenManager


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

        self.screen_manager = ScreenManager()

        self.screen_manager.show(
            DashboardView,
            self.root
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