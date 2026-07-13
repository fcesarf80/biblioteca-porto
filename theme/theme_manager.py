from pathlib import Path


class ThemeManager:

    def __init__(self, theme_name):

        self.set_theme(theme_name)

    def set_theme(self, theme_name):

        self.theme_name = theme_name

        self.theme_path = (
            Path(__file__).parent / theme_name
        )

    def get_background(
        self,
        screen
    ):

        return self.theme_path / f"{screen}.png"