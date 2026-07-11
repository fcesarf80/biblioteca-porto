from components.action_button import ActionButton
from components.form_entry import FormEntry
from components.form_label import FormLabel
from components.table import Table
from models.utilizador import Utilizador
from services.utilizador_service import UtilizadorService
from views.base_module_view import BaseModuleView


class UtilizadoresView(BaseModuleView):

    def __init__(self, master, theme, screen_manager):

        super().__init__(master, theme, screen_manager, "utilizadores")

        self.utilizador_service = UtilizadorService()

        TABLE_ID_WIDTH = 50
        TABLE_NAME_WIDTH = 260
        TABLE_EMAIL_WIDTH = 390
        TABLE_CONTACT_WIDTH = 180

        columns = (
            ("ID", TABLE_ID_WIDTH, "center"),
            ("Nome", TABLE_NAME_WIDTH, "w"),
            ("Email", TABLE_EMAIL_WIDTH, "w"),
            ("Contato", TABLE_CONTACT_WIDTH, "center"),
        )

        #
        # Layout Constants
        #

        FORM_LABEL_X = 470
        FORM_ENTRY_X = 570

        FORM_LABEL_WIDTH = 90
        FORM_ENTRY_WIDTH = 305
        FORM_QUANTITY_WIDTH = 100

        FORM_NAME_Y = 115
        FORM_EMAIL_Y = 148
        FORM_CONTACT_Y = 181

        TABLE_X = 270
        TABLE_Y = 300
        TABLE_WIDTH = 985
        TABLE_HEIGHT = 330

        self.label_nome = FormLabel(
            self,
            text="Nome:",
            x=FORM_LABEL_X,
            y=FORM_NAME_Y,
            width=FORM_LABEL_WIDTH,
        )

        self.entry_nome = FormEntry(
            self, x=FORM_ENTRY_X, y=FORM_NAME_Y, width=FORM_ENTRY_WIDTH
        )

        self.label_email = FormLabel(
            self,
            text="Email:",
            x=FORM_LABEL_X,
            y=FORM_EMAIL_Y,
            width=FORM_LABEL_WIDTH,
        )

        self.entry_email = FormEntry(
            self, x=FORM_ENTRY_X, y=FORM_EMAIL_Y, width=FORM_ENTRY_WIDTH
        )

        self.label_contato = FormLabel(
            self,
            text="Contato:",
            x=FORM_LABEL_X,
            y=FORM_CONTACT_Y,
            width=FORM_LABEL_WIDTH,
        )

        self.entry_contato = FormEntry(
            self, x=FORM_ENTRY_X, y=FORM_CONTACT_Y, width=FORM_ENTRY_WIDTH
        )

        #
        # Tabela
        #

        self.table = Table(
            self,
            columns=(
                ("ID", 180, "center"),
                ("Nome", 300, "w"),
                ("Email", 300, "w"),
                ("Contato", 100, "w"),
            ),
            x=TABLE_X,
            y=TABLE_Y,
            width=TABLE_WIDTH,
            height=TABLE_HEIGHT,
        )

        self.carregar_utilizadores()

        self.table.bind("<<TreeviewSelect>>", self.selecionar_utilizador)

        #
        # Botões
        #

        BUTTON_Y = 650

        BUTTON_WIDTH = 120
        BUTTON_HEIGHT = 40

        BUTTON_ADD_X = 470
        BUTTON_EDIT_X = 600
        BUTTON_REMOVE_X = 730
        BUTTON_SEARCH_X = 860

        self.button_add = ActionButton(
            self,
            text="Adicionar",
            x=BUTTON_ADD_X,
            y=BUTTON_Y,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            background="#79B8F3",
            command=self.adicionar_utilizador,
        )

        self.button_edit = ActionButton(
            self,
            text="Editar",
            x=BUTTON_EDIT_X,
            y=BUTTON_Y,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            background="#E6D5B8",
            command=self.editar_utilizador,
        )

        self.button_remove = ActionButton(
            self,
            text="Remover",
            x=BUTTON_REMOVE_X,
            y=BUTTON_Y,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            background="#F4B6C2",
            command=self.remover_utilizador,
        )

        self.button_search = ActionButton(
            self,
            text="Pesquisar",
            x=BUTTON_SEARCH_X,
            y=BUTTON_Y,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            background="#9AD99A",
            command=self.pesquisar_utilizador,
        )

    def carregar_utilizadores(self):

        self.table.clear()

        utilizadores = self.utilizador_service.listar()

        for utilizador in utilizadores:

            self.table.add_row(
                (
                    utilizador.id,
                    utilizador.nome,
                    utilizador.email,
                    utilizador.contato,
                )
            )

    def selecionar_utilizador(self, event):

        item = self.table.selection()

        if not item:
            return

        valores = self.table.item(item[0], "values")

        self.utilizador_id = valores[0]

        self.entry_nome.set_value(valores[1])
        self.entry_email.set_value(valores[2])
        self.entry_contato.set_value(valores[3])

    def adicionar_utilizador(self):

        utilizador = Utilizador(
            id=self.utilizador_service.proximo_id(),
            nome=self.entry_nome.get_value(),
            email=self.entry_email.get_value(),
            contato=self.entry_contato.get_value(),
        )

        self.utilizador_service.adicionar(utilizador)

        self.carregar_utilizadores()

        self.entry_nome.clear()
        self.entry_email.clear()
        self.entry_contato.clear()

    def editar_utilizador(self):

        if not hasattr(self, "utilizador_id"):
            return

        utilizador = Utilizador(
            id=self.utilizador_id,
            nome=self.entry_nome.get_value(),
            email=self.entry_email.get_value(),
            contato=self.entry_contato.get_value(),
        )

        self.utilizador_service.editar(utilizador)

        self.carregar_utilizadores()

        self.entry_nome.clear()
        self.entry_email.clear()
        self.entry_contato.clear()

        del self.utilizador_id

    def remover_utilizador(self):

        if not hasattr(self, "utilizador_id"):
            return

        self.utilizador_service.remover(self.utilizador_id)

        self.carregar_utilizadores()

        self.entry_nome.clear()
        self.entry_email.clear()
        self.entry_contato.clear()

        del self.utilizador_id

    def pesquisar_utilizador(self):

        texto = self.entry_nome.get_value().strip()

        if not texto:
            texto = self.entry_email.get_value().strip()

        if not texto:
            texto = self.entry_contato.get_value().strip()

        utilizadores = self.utilizador_service.pesquisar(texto)

        self.table.clear()

        for utilizador in utilizadores:

            self.table.add_row(
                (
                    utilizador.id,
                    utilizador.nome,
                    utilizador.email,
                    utilizador.contato,
                )
            )
