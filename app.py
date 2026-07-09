import tkinter as tk

from theme.config import (
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)

from utils.screen_manager import ScreenManager
from views.dashboard_view import DashboardView
from theme.config import CURRENT_THEME
from theme.theme_manager import ThemeManager


class App:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(WINDOW_TITLE)
        self.root.geometry(
            self.centralizar_janela(
                WINDOW_WIDTH,
                WINDOW_HEIGHT
            )
        )

        self.root.resizable(False, False)

        self.theme = ThemeManager(CURRENT_THEME)

        self.screen_manager = ScreenManager()
        self.screen_manager.show(
            DashboardView,
            self.root
        )

    def centralizar_janela(
        self,
        largura,
        altura
    ):

        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2

        return f"{largura}x{altura}+{x}+{y}"

    def run(self):

        self.root.mainloop()