from pygame import Rect
from .screen import Screen

class Character:
    """Player Character"""

    def __init__(self) -> None:
        self.dx: int = 0
        self.dy: int = 200
        self.gravity: int = 300
        self.rect = Rect(100.0, 150.0, 20.0, 20.0)
        self.alive = True # Whether to render or not
        self.score = 0
        self.distance = 0.0
        self.last_pipe_passed = 0

    def jump(self) -> None:
        self.dy = -225
    
    def move(self, dt: float, screen: Screen) -> None:
        proposed_y = int(
            self.rect.y
            + self.dy * dt
            + 0.5 * (dt**2) * self.gravity
        )

        if proposed_y < 0:
            self.rect.y = 0
        elif proposed_y + self.rect.height > screen.height:
            self.rect.y = screen.height - self.rect.height
        else:
            self.rect.y = proposed_y

        self.dy += int(400 * dt)