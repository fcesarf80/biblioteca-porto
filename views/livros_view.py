from components.action_button import ActionButton
from components.form_entry import FormEntry
from components.form_label import FormLabel
from components.table import Table
from models.livro import Livro
from services.livro_service import LivroService
from views.base_module_view import BaseModuleView


class LivrosView(BaseModuleView):

    def __init__(self, master, theme, screen_manager):

        super().__init__(master, theme, screen_manager, "livros")

        self.livro_service = LivroService()

        #
        # Layout Constants
        #

        FORM_LABEL_X = 470
        FORM_ENTRY_X = 570

        FORM_LABEL_WIDTH = 90
        FORM_ENTRY_WIDTH = 305
        FORM_QUANTITY_WIDTH = 100

        FORM_TITLE_Y = 115
        FORM_AUTHOR_Y = 148
        FORM_CATEGORY_Y = 181
        FORM_QUANTITY_Y = 214

        TABLE_X = 270
        TABLE_Y = 300
        TABLE_WIDTH = 985
        TABLE_HEIGHT = 330

        self.label_titulo = FormLabel(
            self,
            text="Título:",
            x=FORM_LABEL_X,
            y=FORM_TITLE_Y,
            width=FORM_LABEL_WIDTH,
        )

        self.entry_titulo = FormEntry(
            self, x=FORM_ENTRY_X, y=FORM_TITLE_Y, width=FORM_ENTRY_WIDTH
        )

        self.label_autor = FormLabel(
            self,
            text="Autor:",
            x=FORM_LABEL_X,
            y=FORM_AUTHOR_Y,
            width=FORM_LABEL_WIDTH,
        )

        self.entry_autor = FormEntry(
            self, x=FORM_ENTRY_X, y=FORM_AUTHOR_Y, width=FORM_ENTRY_WIDTH
        )

        self.label_categoria = FormLabel(
            self,
            text="Categoria:",
            x=FORM_LABEL_X,
            y=FORM_CATEGORY_Y,
            width=FORM_LABEL_WIDTH,
        )

        self.entry_categoria = FormEntry(
            self, x=FORM_ENTRY_X, y=FORM_CATEGORY_Y, width=FORM_ENTRY_WIDTH
        )

        self.label_quantidade = FormLabel(
            self,
            text="Quantidade:",
            x=FORM_LABEL_X,
            y=FORM_QUANTITY_Y,
            width=FORM_LABEL_WIDTH,
        )

        self.entry_quantidade = FormEntry(
            self, x=FORM_ENTRY_X, y=FORM_QUANTITY_Y, width=FORM_QUANTITY_WIDTH
        )

        #
        # Tabela
        #

        self.table = Table(
            self,
            columns=(
                ("ID", 110, "center"),
                ("Título", 200, "w"),
                ("Autor", 170, "w"),
                ("Categoria", 110, "w"),
                ("Ano", 90, "center"),
                ("ISBN", 150, "center"),
                ("Disponível", 130, "center"),
            ),
            x=TABLE_X,
            y=TABLE_Y,
            width=TABLE_WIDTH,
            height=TABLE_HEIGHT,
        )

        self.carregar_livros()

        self.table.bind("<<TreeviewSelect>>", self.selecionar_livro)

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
            command=self.adicionar_livro,
        )

        self.button_edit = ActionButton(
            self,
            text="Editar",
            x=BUTTON_EDIT_X,
            y=BUTTON_Y,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            background="#E6D5B8",
            command=self.editar_livro,
        )

        self.button_remove = ActionButton(
            self,
            text="Remover",
            x=BUTTON_REMOVE_X,
            y=BUTTON_Y,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            background="#F4B6C2",
            command=self.remover_livro,
        )

        self.button_search = ActionButton(
            self,
            text="Pesquisar",
            x=BUTTON_SEARCH_X,
            y=BUTTON_Y,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            background="#9AD99A",
            command=self.pesquisar_livro,
        )

    def carregar_livros(self):
        self.table.clear()
        livros = self.livro_service.listar()

        for livro in livros:
            self.table.add_row(
                (
                    livro.id,
                    livro.titulo,
                    livro.autor,
                    livro.categoria,
                    livro.ano,
                    livro.isbn,
                    "Sim" if livro.disponivel else "Não",
                )
            )

    def adicionar_livro(self):

        livro = Livro(
            id=self.livro_service.proximo_id(),
            titulo=self.entry_titulo.get_value(),
            autor=self.entry_autor.get_value(),
            categoria=self.entry_categoria.get_value(),
            ano=2026,
            isbn="",
            disponivel=True,
        )

        self.livro_service.adicionar(livro)

        self.carregar_livros()

        self.entry_titulo.clear()
        self.entry_autor.clear()
        self.entry_categoria.clear()
        self.entry_quantidade.clear()

    def editar_livro(self):

        if not hasattr(self, "livro_id"):
            return

        livro = Livro(
            id=self.livro_id,
            titulo=self.entry_titulo.get_value(),
            autor=self.entry_autor.get_value(),
            categoria=self.entry_categoria.get_value(),
            ano=2026,
            isbn="",
            disponivel=True,
        )

        self.livro_service.editar(livro)

        self.carregar_livros()

        self.entry_titulo.clear()
        self.entry_autor.clear()
        self.entry_categoria.clear()
        self.entry_quantidade.clear()

        del self.livro_id

    def remover_livro(self):

        if not hasattr(self, "livro_id"):
            return

        self.livro_service.remover(self.livro_id)

        self.carregar_livros()

        self.entry_titulo.clear()
        self.entry_autor.clear()
        self.entry_categoria.clear()
        self.entry_quantidade.clear()

        del self.livro_id

    def pesquisar_livro(self):

        texto = self.entry_titulo.get_value().strip()

        if not texto:
            texto = self.entry_autor.get_value().strip()

        livros = self.livro_service.pesquisar(texto)

        self.table.clear()

        for livro in livros:

            self.table.add_row(
                (
                    livro.id,
                    livro.titulo,
                    livro.autor,
                    livro.categoria,
                    livro.ano,
                    livro.isbn,
                    "Sim" if livro.disponivel else "Não"
                )
            )

    def selecionar_livro(self, event):

        item = self.table.selection()

        if not item:
            return

        valores = self.table.item(item[0], "values")

        self.livro_id = valores[0]
        self.entry_titulo.set_value(valores[1])
        self.entry_autor.set_value(valores[2])
        self.entry_categoria.set_value(valores[3])

        self.entry_quantidade.set_value("1")
