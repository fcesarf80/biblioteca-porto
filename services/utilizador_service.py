from models.utilizador import Utilizador
from services.csv_service import CSVService


class UtilizadorService:

    FILE_PATH = "data/utilizadores.csv"

    FIELDNAMES = (
        "id",
        "nome",
        "email",
        "contato"
    )

    def __init__(self):

        self.csv_service = CSVService(
            self.FILE_PATH
        )

    def listar(self):

        registros = self.csv_service.read()

        utilizadores = []

        for registro in registros:

            utilizadores.append(
                Utilizador(
                    id=registro["id"],
                    nome=registro["nome"],
                    email=registro["email"],
                    contato=registro["contato"]
                )
            )

        return utilizadores

    def buscar_por_id(
        self,
        utilizador_id
    ):

        for utilizador in self.listar():

            if utilizador.id == utilizador_id:

                return utilizador

        return None

    def proximo_id(self):

        utilizadores = self.listar()

        if not utilizadores:

            return "0001"

        ultimo_id = max(
            int(utilizador.id)
            for utilizador in utilizadores
        )

        return f"{ultimo_id + 1:04d}"

    def adicionar(
        self,
        utilizador
    ):

        registros = self.csv_service.read()

        registros.append(
            {
                "id": utilizador.id,
                "nome": utilizador.nome,
                "email": utilizador.email,
                "contato": utilizador.contato
            }
        )

        self.csv_service.write(
            registros,
            self.FIELDNAMES
        )

    def editar(
        self,
        utilizador
    ):

        registros = self.csv_service.read()

        for registro in registros:

            if registro["id"] == utilizador.id:

                registro["nome"] = utilizador.nome
                registro["email"] = utilizador.email
                registro["contato"] = utilizador.contato

                break

        self.csv_service.write(
            registros,
            self.FIELDNAMES
        )

    def remover(
        self,
        utilizador_id
    ):

        registros = self.csv_service.read()

        registros = [
            registro
            for registro in registros
            if registro["id"] != utilizador_id
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

        utilizadores = self.listar()

        if not texto:

            return utilizadores

        return [
            utilizador
            for utilizador in utilizadores
            if (
                texto in utilizador.nome.lower()
                or texto in utilizador.email.lower()
                or texto in utilizador.contato.lower()
            )
        ]