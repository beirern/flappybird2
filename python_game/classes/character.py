from pygame import Rect


class Character:
    """Player Character"""

    def __init__(self):
        self.dx = 0
        self.dy = 200
        self.gravity = 200
        self.rect = Rect(100, 150, 20, 20)
