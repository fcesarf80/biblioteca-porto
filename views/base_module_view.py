from views.base_view import BaseView

from components.sidebar import Sidebar
from components.topbar import TopBar


class BaseModuleView(BaseView):

    def __init__(
        self,
        master,
        theme,
        screen_manager,
        background
    ):

        super().__init__(
            master,
            theme,
            background
        )

        self.screen_manager = screen_manager

        self.sidebar = Sidebar(
            self,
            self.on_menu_click
        )

        self.topbar = TopBar(self)

    def on_menu_click(
        self,
        menu
    ):

        from views.dashboard_view import DashboardView
        from views.livros_view import LivrosView
        from views.utilizadores_view import UtilizadoresView
        from views.emprestimos_view import EmprestimosView
        from views.devolucao_view import DevolucaoView
        from views.ativos_view import AtivosView
        from views.historico_view import HistoricoView
        from views.csv_view import CsvView
        from views.estatisticas_view import EstatisticasView

        routes = {
            "Dashboard": DashboardView,
            "Livros": LivrosView,
            "Utilizadores": UtilizadoresView,
            "Empréstimos": EmprestimosView,
            "Devolução": DevolucaoView,
            "Ativos": AtivosView,
            "Histórico": HistoricoView,
            "CSV": CsvView,
            "Estatísticas": EstatisticasView,
        }

        view = routes.get(menu)

        if view is not None:
            self.screen_manager.show(view)