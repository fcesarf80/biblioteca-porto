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

        self.sidebar = Sidebar(self)

        self.topbar = TopBar(self)