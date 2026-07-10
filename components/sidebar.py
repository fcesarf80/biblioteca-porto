import tkinter as tk

from components.sidebar_button import SidebarButton

class Sidebar(tk.Frame):

    WIDTH = 250

    MENU_ITEMS = [
        "Dashboard",
        "Livros",
        "Utilizadores",
        "Empréstimos",
        "Devolução",
        "Ativos",
        "Histórico",
        "CSV",
        "Estatísticas",
    ]

    def __init__(
        self,
        master,
        on_menu_click
    ):
        super().__init__(master)

        self.on_menu_click = on_menu_click

        self.place(x=0, y=0, width=self.WIDTH, relheight=1)

        self.menu_buttons = []

        self.criar_botoes()

    def criar_botoes(self):
        y = 30

        for texto in self.MENU_ITEMS:
            
            botao = SidebarButton(
                self,
                text=texto,
                command=lambda nome=texto: self.on_menu_click(nome)
            )

            botao.place(x=15, y=y)

            self.menu_buttons.append(botao)

            y += 55
