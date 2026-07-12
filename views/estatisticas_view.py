from components.form_label import FormLabel
from services.emprestimo_service import EmprestimoService
from services.livro_service import LivroService
from services.utilizador_service import UtilizadorService

from views.base_module_view import BaseModuleView


class EstatisticasView(BaseModuleView):

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
            "estatisticas"
        )

        self.emprestimo_service = EmprestimoService()
        self.livro_service = LivroService()
        self.utilizador_service = UtilizadorService()

        #
        # Layout
        #

        LABEL_X = 420
        VALUE_X = 690

        LABEL_WIDTH = 220
        VALUE_WIDTH = 80

        Y_OFFSET = 10   # <<< ALTERE SOMENTE ESTE VALOR

        FormLabel(
            self,
            text="Total de Livros:",
            x=LABEL_X,
            y=170 + Y_OFFSET,
            width=LABEL_WIDTH
        )

        FormLabel(
            self,
            text="Total de Utilizadores:",
            x=LABEL_X,
            y=220 + Y_OFFSET,
            width=LABEL_WIDTH
        )

        FormLabel(
            self,
            text="Total de Empréstimos:",
            x=LABEL_X,
            y=270 + Y_OFFSET,
            width=LABEL_WIDTH
        )

        FormLabel(
            self,
            text="Empréstimos Ativos:",
            x=LABEL_X,
            y=320 + Y_OFFSET,
            width=LABEL_WIDTH
        )

        FormLabel(
            self,
            text="Livros Disponíveis:",
            x=LABEL_X,
            y=370 + Y_OFFSET,
            width=LABEL_WIDTH
        )

        FormLabel(
            self,
            text="Livros Emprestados:",
            x=LABEL_X,
            y=420 + Y_OFFSET,
            width=LABEL_WIDTH
        )

        self.label_total_livros = FormLabel(
            self,
            text="0",
            x=VALUE_X,
            y=170 + Y_OFFSET,
            width=VALUE_WIDTH
        )

        self.label_total_utilizadores = FormLabel(
            self,
            text="0",
            x=VALUE_X,
            y=220 + Y_OFFSET,
            width=VALUE_WIDTH
        )

        self.label_total_emprestimos = FormLabel(
            self,
            text="0",
            x=VALUE_X,
            y=270 + Y_OFFSET,
            width=VALUE_WIDTH
        )

        self.label_total_emprestimos_ativos = FormLabel(
            self,
            text="0",
            x=VALUE_X,
            y=320 + Y_OFFSET,
            width=VALUE_WIDTH
        )

        self.label_total_disponiveis = FormLabel(
            self,
            text="0",
            x=VALUE_X,
            y=370 + Y_OFFSET,
            width=VALUE_WIDTH
        )

        self.label_total_livros_emprestados = FormLabel(
            self,
            text="0",
            x=VALUE_X,
            y=420 + Y_OFFSET,
            width=VALUE_WIDTH
        )

        self.carregar_estatisticas()

    def carregar_estatisticas(self):

        livros = self.livro_service.listar()
        utilizadores = self.utilizador_service.listar()
        emprestimos = self.emprestimo_service.listar()

        total_livros = len(livros)
        total_utilizadores = len(utilizadores)
        total_emprestimos = len(emprestimos)

        emprestimos_ativos = sum(
            1
            for emprestimo in emprestimos
            if emprestimo.ativo
        )

        livros_disponiveis = sum(
            1
            for livro in livros
            if livro.disponivel
        )

        livros_emprestados = (
            total_livros - livros_disponiveis
        )

        self.label_total_livros.config(
            text=str(total_livros)
        )

        self.label_total_utilizadores.config(
            text=str(total_utilizadores)
        )

        self.label_total_emprestimos.config(
            text=str(total_emprestimos)
        )

        self.label_total_emprestimos_ativos.config(
            text=str(emprestimos_ativos)
        )

        self.label_total_disponiveis.config(
            text=str(livros_disponiveis)
        )

        self.label_total_livros_emprestados.config(
            text=str(livros_emprestados)
        )