from pathlib import Path

from theme.config import CURRENT_THEME


class ThemeManager:

    def __init__(self):

        self.theme_path = (
            Path(__file__).parent /
            CURRENT_THEME
        )

theme.get_background("dashboard")