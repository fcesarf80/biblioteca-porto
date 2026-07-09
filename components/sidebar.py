import tkinter as tk
from components.sidebar_button import SidebarButton


class Sidebar(tk.Frame):

    WIDTH = 250

    def __init__(self, master):

        super().__init__(
            master,
            width=self.WIDTH,
            bg="#1E293B"
        )

        self.place(
            x=0,
            y=0,
            relheight=1
        )

        self.dashboard_button = SidebarButton(
            self,
            text="Dashboard"
        )

        self.dashboard_button.place(
            x=15,
            y=30
        )