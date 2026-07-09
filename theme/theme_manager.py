from pathlib import Path


class ThemeManager:

    def __init__(self, theme_name: str):
        self.theme_path = Path(__file__).parent / theme_name

    def get_background(self, screen: str):
        return self.theme_path / f"{screen}.png"