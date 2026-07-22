import tkinter as tk
from components.form_label import FormLabel
from components.table import Table
from services.emprestimo_service import EmprestimoService
from services.livro_service import LivroService
from services.utilizador_service import UtilizadorService
from views.base_module_view import BaseModuleView


class HistoricoView(BaseModuleView):

    def __init__(self, master, theme, screen_manager):

        super().__init__(master, theme, screen_manager, "historico")

        self.emprestimo_service = EmprestimoService()
        self.livro_service = LivroService()
        self.utilizador_service = UtilizadorService()

        #
        # Tabela (Coordenadas alinhadas com o painel central)
        #
        self.table = Table(
            self,
            columns=(
                ("ID", 70, "center"),
                ("Livro", 280, "w"),
                ("Utilizador", 240, "w"),
                ("Empréstimo", 130, "center"),
                ("Prevista", 130, "center"),
                ("Devolução", 130, "center"),
                ("Status", 120, "center"),
            ),
            x=290,  # Recuado para alinhar à esquerda
            y=320,
            width=1100,  # Expandido para usar a largura total disponível
            height=180,
        )

        self.table.bind("<<TreeviewSelect>>", self.selecionar_emprestimo)

        #
        # Botões
        #
        BUTTON_Y = 650
        BUTTON_WIDTH = 120
        BUTTON_HEIGHT = 40

        BUTTON_ADD_X = 470
        BUTTON_EDIT_X = 600
        BUTTON_RETURN_X = 730
        BUTTON_SEARCH_X = 860

        self.carregar_emprestimos()

    def carregar_emprestimos(self):

        self.table.clear()
        emprestimos = self.emprestimo_service.listar()

        for emprestimo in emprestimos:

            livro = self.livro_service.buscar_por_id(emprestimo.livro_id)
            utilizador = self.utilizador_service.buscar_por_id(
                emprestimo.utilizador_id
            )

            # Obtém a data de devolução real se existir no modelo, senão deixa vazio
            data_devolvido = (
                getattr(emprestimo, "data_devolucao_real", "")
                if not emprestimo.ativo
                else "-"
            )

            # Corrigido: Agora envia exatamente 7 parâmetros para corresponder às colunas
            self.table.add_row(
                (
                    emprestimo.id,
                    livro.titulo if livro else "",
                    utilizador.nome if utilizador else "",
                    emprestimo.data_emprestimo,
                    emprestimo.data_devolucao,
                    data_devolvido,
                    "Ativo" if emprestimo.ativo else "Devolvido",
                )
            )

    def selecionar_emprestimo(self, event):
        pass
