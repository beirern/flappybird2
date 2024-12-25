from pygame import Rect


class Pipe:
    """Pipes"""

    NUM_PIPES: int = 8
    PIPE_WIDTH: int = 100
    MIN_PIPE_DISTANCE: int = 180
    MAX_PIPE_DISTANCE: int = 220
    MIN_GAP: int = 150
    MAX_GAP: int = 200

    def __init__(self, x: int, topheight: int, bottomy: int, bottomheight: int):
        self.topRect = Rect(x, 0, self.PIPE_WIDTH, topheight)
        self.bottomRect = Rect(x, bottomy, self.PIPE_WIDTH, bottomheight)

        self.dx: int = -200
        self.dy: int = 0
        self.gravity: int = 0
        self.passed: bool = False
