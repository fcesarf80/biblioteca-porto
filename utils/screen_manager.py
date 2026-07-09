class ScreenManager:

    def __init__(self):

        self.current_view = None

    def show(self, view_class, master):

        if self.current_view is not None:
            self.current_view.destroy()

        self.current_view = view_class(master)