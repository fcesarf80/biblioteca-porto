import tkinter as tk


class BibliotecaPortoApp:

    LARGURA = 1280
    ALTURA = 720

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Biblioteca Porto")

        self.root.geometry(
            self.centralizar_janela(
                self.LARGURA,
                self.ALTURA
            )
        )

        self.root.resizable(False, False)

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