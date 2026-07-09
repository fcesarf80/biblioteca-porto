class ScreenManager:

    def __init__(self, master, theme):

        self.master = master
        self.theme = theme
        self.current_view = None

    def show(self, view_class):

        if self.current_view is not None:
            self.current_view.destroy()

        self.current_view = view_class(
            self.master,
            self.theme
        )