from components.form_label import FormLabel
from components.table import Table

from services.emprestimo_service import EmprestimoService
from services.livro_service import LivroService
from services.utilizador_service import UtilizadorService

from views.base_module_view import BaseModuleView

class HistoricoView(BaseModuleView):

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
            "historico"
        )

        self.emprestimo_service = EmprestimoService()
        self.livro_service = LivroService()
        self.utilizador_service = UtilizadorService()
                
        #
        # Tabela
        #

        self.table = Table(
            self,
            columns=(
                ("ID", 200, "w"),
                ("Livro", 210, "w"),
                ("Utilizador", 195, "w"),
                ("Empréstimo", 190, "w"),
                ("Prevista", 80, "w"),
                ("Devolução", 120, "center"),
                ("Status", 110, "center"),
            ),
            x=320,
            y=260,
            width=900,
            height=355,
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
        
        self.carregar_emprestimos()  

    def carregar_emprestimos(self):

        self.table.clear()

        emprestimos = self.emprestimo_service.listar()

        for emprestimo in emprestimos:
            
            livro = self.livro_service.buscar_por_id(
                emprestimo.livro_id
            )

            utilizador = self.utilizador_service.buscar_por_id(
                emprestimo.utilizador_id
            )

            self.table.add_row(
            (
                emprestimo.id,
                livro.titulo if livro else "",
                utilizador.nome if utilizador else "",
                emprestimo.data_emprestimo,
                emprestimo.data_devolucao,
                "Ativo" if emprestimo.ativo else "Devolvido",
            )
        )

    def selecionar_emprestimo(self, event):
        pass