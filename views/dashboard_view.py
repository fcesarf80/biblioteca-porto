from views.base_view import BaseView
from components.sidebar import Sidebar

class DashboardView(BaseView):

    def __init__(self, master, theme):

        super().__init__(
        master,
        theme,
        "dashboard"
    )
        
        self.sidebar = Sidebar(self)