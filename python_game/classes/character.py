from pygame import Rect


class Character:
    """Player Character"""

    def __init__(self) -> None:
        self.dx: int = 0
        self.dy: int = 200
        self.gravity: int = 300
        self.rect = Rect(100.0, 150.0, 20.0, 20.0)
