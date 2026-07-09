from pathlib import Path

from theme.config import CURRENT_THEME


class ThemeManager:

    def __init__(self):

        self.theme_path = (
            Path(__file__).parent /
            CURRENT_THEME
        )

    def get_background(self, nome_arquivo):

        return self.theme_path / nome_arquivo