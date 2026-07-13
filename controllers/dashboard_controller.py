from services.livro_service import LivroService
from services.utilizador_service import UtilizadorService
from services.emprestimo_service import EmprestimoService


class DashboardController:

    def __init__(self):

        self.livro_service = LivroService()
        self.utilizador_service = UtilizadorService()
        self.emprestimo_service = EmprestimoService()

    def total_livros(self):

        return len(
            self.livro_service.listar()
        )

    def total_utilizadores(self):

        return len(
            self.utilizador_service.listar()
        )

    def total_emprestimos(self):

        return len(
            self.emprestimo_service.listar()
        )

    def total_ativos(self):

        return sum(
            1
            for emprestimo in self.emprestimo_service.listar()
            if emprestimo.ativo
        )

    def atualizar_dashboard(
        self,
        card_livros,
        card_utilizadores,
        card_emprestimos,
        card_historico
    ):

        card_livros.set_data(
            "Livros",
            self.total_livros()
        )

        card_utilizadores.set_data(
            "Utilizadores",
            self.total_utilizadores()
        )

        card_emprestimos.set_data(
            "Empréstimos",
            self.total_emprestimos()
        )

        card_historico.set_data(
            "Ativos",
            self.total_ativos()
        )
