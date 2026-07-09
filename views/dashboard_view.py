from views.base_view import BaseView


class DashboardView(BaseView):

    def __init__(self, master):

        super().__init__(
            master,
            "bg_01_dashboard.png"
        )