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