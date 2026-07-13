from views.base_view import BaseView

from components.sidebar import Sidebar
from components.topbar import TopBar
from components.card import Card
from components.quick_action_button import QuickActionButton
from components.activity_panel import ActivityPanel

from controllers.dashboard_controller import DashboardController

from views.livros_view import LivrosView
from views.utilizadores_view import UtilizadoresView
from views.emprestimos_view import EmprestimosView
from views.devolucao_view import DevolucaoView
from views.ativos_view import AtivosView
from views.historico_view import HistoricoView
from views.csv_view import CsvView
from views.estatisticas_view import EstatisticasView


class DashboardView(BaseView):

    ROUTES = {
        "Livros": LivrosView,
        "Utilizadores": UtilizadoresView,
        "Empréstimos": EmprestimosView,
        "Devolução": DevolucaoView,
        "Ativos": AtivosView,
        "Histórico": HistoricoView,
        "CSV": CsvView,
        "Estatísticas": EstatisticasView,
    }

    def __init__(self, master, theme, screen_manager):
        super().__init__(master, theme, "dashboard")

        self.screen_manager = screen_manager
        self.controller = DashboardController()

        self.sidebar = Sidebar(self, self.on_menu_click)
        self.topbar = TopBar(self, self.on_theme_change)

        # Cards principais
        self.card_livros = Card(
            self, x=280, y=172, width=220, height=120,
            command=lambda: self.screen_manager.show(LivrosView)
        )
        self.card_utilizadores = Card(
            self, x=510, y=172, width=220, height=120,
            command=lambda: self.screen_manager.show(UtilizadoresView)
        )
        self.card_emprestimos = Card(
            self, x=740, y=172, width=220, height=120,
            command=lambda: self.screen_manager.show(EmprestimosView)
        )
        self.card_historico = Card(
            self, x=970, y=172, width=220, height=120,
            command=lambda: self.screen_manager.show(HistoricoView)
        )

        # Botões de ação rápida (Quick Action)
        self.quick_add_book = QuickActionButton(
            self, x=280, y=345, width=105, height=100,
            command=lambda: self.screen_manager.show(LivrosView)
        )
        self.quick_search_book = QuickActionButton(
            self, x=410, y=345, width=105, height=100,
            command=lambda: self.screen_manager.show(LivrosView)
        )
        self.quick_loan = QuickActionButton(
            self, x=535, y=345, width=110, height=100,
            command=lambda: self.screen_manager.show(EmprestimosView)
        )
        self.quick_return = QuickActionButton(
            self, x=670, y=345, width=100, height=100,
            command=lambda: self.screen_manager.show(DevolucaoView)
        )
        self.quick_users = QuickActionButton(
            self, x=795, y=345, width=95, height=100,
            command=lambda: self.screen_manager.show(UtilizadoresView)
        )
        self.quick_active = QuickActionButton(
            self, x=915, y=345, width=95, height=100,
            command=lambda: self.screen_manager.show(AtivosView)
        )
        self.quick_history = QuickActionButton(
            self, x=1030, y=345, width=95, height=100,
            command=lambda: self.screen_manager.show(HistoricoView)
        )
        self.quick_statistics = QuickActionButton(
            self, x=1150, y=345, width=95, height=100,
            command=lambda: self.screen_manager.show(EstatisticasView)
        )

    def on_theme_change(self, tema):
        temas = {
            "Porto": "porto",
            "Natal": "natal",
            "São João": "sao_joao",
        }

        self.theme.set_theme(temas[tema])
        self.screen_manager.show(DashboardView)

    def on_menu_click(self, menu):
        if menu == "Dashboard":
            return

        view = self.ROUTES.get(menu)
        if view is not None:
            self.screen_manager.show(view)
