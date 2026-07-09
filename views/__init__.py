import tkinter as tk

from PIL import Image, ImageTk

from theme.theme_manager import ThemeManager
from theme.config import WINDOW_WIDTH, WINDOW_HEIGHT


class BaseView(tk.Frame):

    def __init__(self, master, background):

        super().__init__(master)

        self.place(
            x=0,
            y=0,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT
        )

        self.screen_manager = ScreenManager()

        self.screen_manager.show(
            DashboardView,
            self.root
        )