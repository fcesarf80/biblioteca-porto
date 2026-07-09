from views.base_view import BaseView


class DashboardView(BaseView):

    def __init__(self, master, theme):

        super().__init__(
        master,
        theme,
        "dashboard"
    )