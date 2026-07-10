from models.livro import Livro
from services.csv_service import CSVService


class LivroService:

    FILE_PATH = "data/livros.csv"

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