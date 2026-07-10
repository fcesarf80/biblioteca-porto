class Navigator:

    def __init__(self, screen_manager):

        self.screen_manager = screen_manager

        self.routes = {}

    def register(
        self,
        name,
        view
    ):

        self.routes[name] = view

    def open(self, name):

        view = self.routes.get(name)

        if view is not None:

            self.screen_manager.show(view)
            