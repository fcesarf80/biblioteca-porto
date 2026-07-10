from views.base_view import BaseView


class LivrosView(BaseView):

    def __init__(
        self,
        master,
        theme,
        screen_manager
    ):

        super().__init__(
            master,
            theme,
            "livros"
        )

        self.screen_manager = screen_manager