from views.base_view import BaseView


class LivrosView(BaseView):

    def __init__(self, master, theme):

        super().__init__(
            master,
            theme,
            "livros"
        )