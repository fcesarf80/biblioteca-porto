from components.table import Table

from services.livro_service import LivroService

from views.base_module_view import BaseModuleView


class LivrosView(BaseModuleView):

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
            "livros"
        )

        self.livro_service = LivroService()

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
            x=270,
            y=300,
            width=985,
            height=330
        )

        self.carregar_livros()

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
                "Sim" if livro.disponivel else "Não"
            )
        )