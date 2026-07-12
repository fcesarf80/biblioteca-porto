from datetime import datetime, timedelta
from components.action_button import ActionButton
from components.form_combobox import FormComboBox
from components.form_entry import FormEntry
from components.form_label import FormLabel
from components.table import Table
from models.emprestimo import Emprestimo
from services.emprestimo_service import EmprestimoService
from services.livro_service import LivroService
from services.utilizador_service import UtilizadorService
from views.base_module_view import BaseModuleView

class EmprestimosView(BaseModuleView):

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
            "emprestimos"
        )

        self.emprestimo_service = EmprestimoService()
        self.livro_service = LivroService()
        self.utilizador_service = UtilizadorService()

        #
        # Layout
        #

        FORM_LABEL_X = 470
        FORM_FIELD_X = 670

        FORM_LABEL_WIDTH = 90
        FORM_FIELD_WIDTH = 305

        FORM_BOOK_Y = 115
        FORM_USER_Y = 148
        FORM_DATE_Y = 181
        FORM_RETURN_Y = 214

        TABLE_X = 270
        TABLE_Y = 300
        TABLE_WIDTH = 1100
        TABLE_HEIGHT = 330

        #
        # Labels
        #

        FormLabel(
            self,
            text="Livro:",
            x=FORM_LABEL_X,
            y=FORM_BOOK_Y,
            width=FORM_LABEL_WIDTH
        )

        FormLabel(
            self,
            text="Utilizador:",
            x=FORM_LABEL_X,
            y=FORM_USER_Y,
            width=FORM_LABEL_WIDTH
        )

        FormLabel(
            self,
            text="Empréstimo:",
            x=FORM_LABEL_X,
            y=FORM_DATE_Y,
            width=FORM_LABEL_WIDTH
        )

        FormLabel(
            self,
            text="Prevista:",
            x=FORM_LABEL_X,
            y=FORM_RETURN_Y,
            width=FORM_LABEL_WIDTH
        )

        #
        # Campos
        #

        self.combo_livro = FormComboBox(
            self,
            values=[],
            x=FORM_FIELD_X,
            y=FORM_BOOK_Y,
            width=FORM_FIELD_WIDTH
        )

        self.combo_utilizador = FormComboBox(
            self,
            values=[],
            x=FORM_FIELD_X,
            y=FORM_USER_Y,
            width=FORM_FIELD_WIDTH
        )

        self.entry_data = FormEntry(
            self,
            x=FORM_FIELD_X,
            y=FORM_DATE_Y,
            width=FORM_FIELD_WIDTH
        )

        self.entry_prevista = FormEntry(
            self,
            x=FORM_FIELD_X,
            y=FORM_RETURN_Y,
            width=FORM_FIELD_WIDTH
        )

        #
        # Tabela
        #

        self.table = Table(
            self,
            columns=(
                ("ID", 70, "center"),
                ("Livro", 280, "w"),
                ("Utilizador", 240, "w"),
                ("Empréstimo", 130, "center"),
                ("Prevista", 130, "center"),
                ("Status", 120, "center"),
            ),
            x=TABLE_X,
            y=TABLE_Y,
            width=TABLE_WIDTH,
            height=TABLE_HEIGHT,
        )

        self.table.bind(
            "<<TreeviewSelect>>",
            self.selecionar_emprestimo
        )

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

        self.button_add = ActionButton(
            self,
            text="Emprestar",
            x=BUTTON_ADD_X,
            y=BUTTON_Y,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            background="#79B8F3",
            command=self.adicionar_emprestimo
        )

        self.button_edit = ActionButton(
            self,
            text="Editar",
            x=BUTTON_EDIT_X,
            y=BUTTON_Y,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            background="#E6D5B8",
            command=self.editar_emprestimo
        )

        self.button_return = ActionButton(
            self,
            text="Devolver",
            x=BUTTON_RETURN_X,
            y=BUTTON_Y,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            background="#F4B6C2",
            command=self.devolver_emprestimo
        )

        self.button_search = ActionButton(
            self,
            text="Pesquisar",
            x=BUTTON_SEARCH_X,
            y=BUTTON_Y,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            background="#9AD99A",
            command=self.pesquisar_emprestimo
        )

        self.carregar_livros()
        self.carregar_utilizadores()

        hoje = datetime.today()

        self.entry_data.set_value(
            hoje.strftime("%d/%m/%Y")
        )

        self.entry_prevista.set_value(
            (
                hoje + timedelta(days=7)
            ).strftime("%d/%m/%Y")
        )

        self.carregar_emprestimos()

    def carregar_livros(self):

        self.livros = self.livro_service.listar()

        self.combo_livro.set_values(
            [
                livro.titulo
                for livro in self.livros
                if livro.disponivel
            ]
        )

    def carregar_utilizadores(self):

        self.utilizadores = (
            self.utilizador_service.listar()
        )

        self.combo_utilizador.set_values(
            [
                utilizador.nome
                for utilizador in self.utilizadores
            ]
        )

    def carregar_emprestimos(self):

        self.table.clear()

        emprestimos = (
            self.emprestimo_service.listar()
        )

        for emprestimo in emprestimos:

            livro = self.livro_service.buscar_por_id(
                emprestimo.livro_id
            )

            utilizador = (
                self.utilizador_service.buscar_por_id(
                    emprestimo.utilizador_id
                )
            )

            self.table.add_row(
                (
                    emprestimo.id,
                    livro.titulo if livro else "",
                    utilizador.nome if utilizador else "",
                    emprestimo.data_emprestimo,
                    emprestimo.data_prevista,
                    "Ativo"
                    if emprestimo.ativo
                    else "Devolvido"
                )
            )

    def selecionar_emprestimo(self, event):

        item = self.table.selection()

        if not item:
            return

        valores = self.table.item(
            item[0],
            "values"
        )

        self.emprestimo_id = valores[0]

        self.combo_livro.set_value(
            valores[1]
        )

        self.combo_utilizador.set_value(
            valores[2]
        )

        self.entry_data.set_value(
            valores[3]
        )

        self.entry_prevista.set_value(
            valores[4]
        )

    def adicionar_emprestimo(self):

        titulo = self.combo_livro.get_value()
        nome = self.combo_utilizador.get_value()

        if not titulo or not nome:
            return

        livro = next(
            (
                livro
                for livro in self.livros
                if livro.titulo == titulo
            ),
            None
        )

        utilizador = next(
            (
                utilizador
                for utilizador in self.utilizadores
                if utilizador.nome == nome
            ),
            None
        )

        if livro is None or utilizador is None:
            return

        emprestimo = Emprestimo(
            id=self.emprestimo_service.proximo_id(),
            livro_id=livro.id,
            utilizador_id=utilizador.id,
            data_emprestimo=self.entry_data.get_value(),
            data_prevista=self.entry_prevista.get_value(),
            data_devolucao="",
            ativo=True
        )

        self.emprestimo_service.adicionar(
            emprestimo
        )

        livro.disponivel = False

        self.livro_service.editar(
            livro
        )

        self.carregar_livros()
        self.carregar_emprestimos()

        self.combo_livro.clear()
        self.combo_utilizador.clear()

    def editar_emprestimo(self):
        pass

    def devolver_emprestimo(self):

        if not hasattr(self, "emprestimo_id"):
            return

        emprestimo = self.emprestimo_service.buscar_por_id(
            self.emprestimo_id
        )

        if emprestimo is None:
            return

        emprestimo.ativo = False

        emprestimo.data_devolucao = datetime.today().strftime(
            "%d/%m/%Y"
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

        self.carregar_livros()
        self.carregar_emprestimos()

        del self.emprestimo_id

    def pesquisar_emprestimo(self):
        pass