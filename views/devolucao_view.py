from datetime import datetime

from components.action_button import ActionButton
from components.table import Table

from services.emprestimo_service import EmprestimoService
from services.livro_service import LivroService
from services.utilizador_service import UtilizadorService

from views.base_module_view import BaseModuleView


class DevolucaoView(BaseModuleView):

    def __init__(
        self,
        master,
        theme,
        screen_manager
    ):

        super().__init__(
            master,
            theme,
            screen_manager,
            "devolucao"
        )

        self.emprestimo_service = EmprestimoService()
        self.livro_service = LivroService()
        self.utilizador_service = UtilizadorService()

        self.table = Table(
            self,
            columns=(
                ("ID", 70, "center"),
                ("Livro", 280, "w"),
                ("Utilizador", 240, "w"),
                ("Empréstimo", 140, "center"),
                ("Prevista", 140, "center"),
            ),
            x=320,
            y=460,
            width=900,
            height=300,
        )

        self.table.bind(
            "<<TreeviewSelect>>",
            self.selecionar_emprestimo
        )

        self.button_devolver = ActionButton(
            self,
            text="Devolver",
            x=700,
            y=620,
            width=140,
            height=40,
            background="#F4B6C2",
            command=self.devolver_emprestimo
        )

        self.carregar_emprestimos()

    def selecionar_emprestimo(self, event):

        item = self.table.selection()

        if not item:
            return

        valores = self.table.item(
            item[0],
            "values"
        )

        self.emprestimo_id = valores[0]

    def devolver_emprestimo(self):

        if not hasattr(self, "emprestimo_id"):
            return

        emprestimo = self.emprestimo_service.buscar_por_id(
            self.emprestimo_id
        )

        if emprestimo is None:
            return

        emprestimo.ativo = False

        emprestimo.data_devolucao = (
            datetime.today().strftime("%d/%m/%Y")
        )

        self.emprestimo_service.editar(
            emprestimo
        )

        livro = self.livro_service.buscar_por_id(
            emprestimo.livro_id
        )

        if livro:

            livro.disponivel = True

            self.livro_service.editar(
                livro
            )

        self.carregar_emprestimos()

        del self.emprestimo_id

    def carregar_emprestimos(self):

        self.table.clear()

        emprestimos = self.emprestimo_service.listar()

        for emprestimo in emprestimos:

            if not emprestimo.ativo:
                continue

            livro = self.livro_service.buscar_por_id(
                emprestimo.livro_id
            )

            utilizador = self.utilizador_service.buscar_por_id(
                emprestimo.utilizador_id
            )

            self.table.add_row(
                (
                    emprestimo.id,
                    livro.titulo if livro else "",
                    utilizador.nome if utilizador else "",
                    emprestimo.data_emprestimo,
                    emprestimo.data_prevista,
                )
            )
