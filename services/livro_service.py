from models.livro import Livro
from services.csv_service import CSVService


class LivroService:

    FILE_PATH = "data/livros.csv"

    FIELDNAMES = (
        "id",
        "titulo",
        "autor",
        "categoria",
        "ano",
        "isbn",
        "disponivel"
    )

    def __init__(self):

        self.csv_service = CSVService(
            self.FILE_PATH
        )

    def listar(self):

        registros = self.csv_service.read()

        livros = []

        for registro in registros:

            livros.append(
                Livro(
                    id=registro["id"],
                    titulo=registro["titulo"],
                    autor=registro["autor"],
                    categoria=registro["categoria"],
                    ano=int(registro["ano"]),
                    isbn=registro["isbn"],
                    disponivel=(
                        registro["disponivel"] == "True"
                    )
                )
            )

        return livros

    def buscar_por_id(
        self,
        livro_id
    ):

        for livro in self.listar():

            if livro.id == livro_id:

                return livro

        return None

    def proximo_id(self):

        livros = self.listar()

        if not livros:

            return "0001"

        ultimo_id = max(
            int(livro.id)
            for livro in livros
        )

        return f"{ultimo_id + 1:04d}"

    def adicionar(
        self,
        livro
    ):

        registros = self.csv_service.read()

        registros.append(
            {
                "id": livro.id,
                "titulo": livro.titulo,
                "autor": livro.autor,
                "categoria": livro.categoria,
                "ano": livro.ano,
                "isbn": livro.isbn,
                "disponivel": str(livro.disponivel)
            }
        )

        self.csv_service.write(
            registros,
            self.FIELDNAMES
        )

    def editar(
        self,
        livro
    ):

        registros = self.csv_service.read()

        for registro in registros:

            if registro["id"] == livro.id:

                registro["titulo"] = livro.titulo
                registro["autor"] = livro.autor
                registro["categoria"] = livro.categoria
                registro["ano"] = livro.ano
                registro["isbn"] = livro.isbn
                registro["disponivel"] = str(
                    livro.disponivel
                )

                break

        self.csv_service.write(
            registros,
            self.FIELDNAMES
        )

    def remover(
        self,
        livro_id
    ):

        registros = self.csv_service.read()

        registros = [
            registro
            for registro in registros
            if registro["id"] != livro_id
        ]

        self.csv_service.write(
            registros,
            self.FIELDNAMES
        )

    def pesquisar(
        self,
        texto
    ):

        texto = texto.lower().strip()

        livros = self.listar()

        if not texto:

            return livros

        return [
            livro
            for livro in livros
            if (
                texto in livro.titulo.lower()
                or texto in livro.autor.lower()
            )
        ]