from models.emprestimo import Emprestimo
from services.csv_service import CSVService


class EmprestimoService:

    FILE_PATH = "data/emprestimos.csv"

    FIELDNAMES = (
        "id",
        "livro_id",
        "utilizador_id",
        "data_emprestimo",
        "data_prevista",
        "data_devolucao",
        "ativo"
    )

    def __init__(self):

        self.csv_service = CSVService(
            self.FILE_PATH
        )

    def listar(self):

        registros = self.csv_service.read()

        emprestimos = []

        for registro in registros:

            emprestimos.append(
                Emprestimo(
                    id=registro["id"],
                    livro_id=registro["livro_id"],
                    utilizador_id=registro["utilizador_id"],
                    data_emprestimo=registro["data_emprestimo"],
                    data_prevista=registro["data_prevista"],
                    data_devolucao=registro["data_devolucao"],
                    ativo=(
                        registro["ativo"] == "True"
                    )
                )
            )

        return emprestimos

    def buscar_por_id(
        self,
        emprestimo_id
    ):

        for emprestimo in self.listar():

            if emprestimo.id == emprestimo_id:

                return emprestimo

        return None

    def proximo_id(self):

        emprestimos = self.listar()

        if not emprestimos:

            return "0001"

        ultimo_id = max(
            int(emprestimo.id)
            for emprestimo in emprestimos
        )

        return f"{ultimo_id + 1:04d}"

    def adicionar(
        self,
        emprestimo
    ):

        registros = self.csv_service.read()

        registros.append(
            {
                "id": emprestimo.id,
                "livro_id": emprestimo.livro_id,
                "utilizador_id": emprestimo.utilizador_id,
                "data_emprestimo": emprestimo.data_emprestimo,
                "data_prevista": emprestimo.data_prevista,
                "data_devolucao": emprestimo.data_devolucao,
                "ativo": str(emprestimo.ativo)
            }
        )

        self.csv_service.write(
            registros,
            self.FIELDNAMES
        )

    def editar(
        self,
        emprestimo
    ):

        registros = self.csv_service.read()

        for registro in registros:

            if registro["id"] == emprestimo.id:

                registro["livro_id"] = emprestimo.livro_id
                registro["utilizador_id"] = emprestimo.utilizador_id
                registro["data_emprestimo"] = emprestimo.data_emprestimo
                registro["data_prevista"] = emprestimo.data_prevista
                registro["data_devolucao"] = emprestimo.data_devolucao
                registro["ativo"] = str(emprestimo.ativo)

                break

        self.csv_service.write(
            registros,
            self.FIELDNAMES
        )

    def remover(
        self,
        emprestimo_id
    ):

        registros = self.csv_service.read()

        registros = [
            registro
            for registro in registros
            if registro["id"] != emprestimo_id
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

        emprestimos = self.listar()

        if not texto:

            return emprestimos

        return [
            emprestimo
            for emprestimo in emprestimos
            if (
                texto in emprestimo.livro_id.lower()
                or texto in emprestimo.utilizador_id.lower()
            )
        ]