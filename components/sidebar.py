import tkinter as tk

from components.sidebar_button import SidebarButton


class Sidebar(tk.Frame):

    WIDTH = 250

    BUTTONS = [
        ("Dashboard", None),
        ("Livros", None),
        ("Utilizadores", None),
        ("Empréstimos", None),
        ("Devolução", None),
        ("Ativos", None),
        ("Histórico", None),
        ("CSV", None),
        ("Estatísticas", None),
    ]

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

        self.buttons = []

        self.criar_botoes()

    def criar_botoes(self):

        y = 30

        for texto, comando in self.BUTTONS:

            botao = SidebarButton(
                self,
                text=texto,
                command=comando
            )

            botao.place(
                x=15,
                y=y
            )

            self.buttons.append(botao)

            y += 55