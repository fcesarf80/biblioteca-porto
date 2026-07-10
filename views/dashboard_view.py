from views.base_view import BaseView

from components.sidebar import Sidebar
from components.topbar import TopBar
from components.card import Card
from components.quick_action_button import QuickActionButton
from components.activity_panel import ActivityPanel
from controllers.dashboard_controller import DashboardController


class DashboardView(BaseView):

    def __init__(
        self,
        master,
        theme,
        screen_manager
    ):

        super().__init__(
            master,
            theme,
            "dashboard"
        )

        self.screen_manager = screen_manager

        self.controller = DashboardController()

        self.sidebar = Sidebar(self)

        self.topbar = TopBar(self)

        self.card_livros = Card(
            self,
            x=280,
            y=172,
            width=220,
            height=120
        )
       
        self.card_utilizadores = Card(
            self,
            x=510,
            y=172,
            width=220,
            height=120
        )

        self.card_emprestimos = Card(
            self,
            x=740,
            y=172,
            width=220,
            height=120
        )

        self.card_historico = Card(
            self,
            x=970,
            y=172,
            width=220,
            height=120
        )

        self.quick_add_book = QuickActionButton(
            self,
            x=280,
            y=345,
            width=105,
            height=100
        )

        self.quick_search_book = QuickActionButton(
            self,
            x=410,
            y=345,
            width=105,
            height=100
        )

        self.quick_loan = QuickActionButton(
            self,
            x=535,
            y=345,
            width=110,
            height=100
        )

        self.quick_return = QuickActionButton(
            self,
            x=670,
            y=345,
            width=100,
            height=100
        )

        self.quick_users = QuickActionButton(
            self,
            x=795,
            y=345,
            width=95,
            height=100
        )

        self.quick_active = QuickActionButton(
            self,
            x=915,
            y=345,
            width=95,
            height=100
        )

        self.quick_history = QuickActionButton(
            self,
            x=1030,
            y=345,
            width=95,
            height=100
        )

        self.quick_statistics = QuickActionButton(
            self,
            x=1150,
            y=345,
            width=95,
            height=100
        )