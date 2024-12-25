from pygame import Rect


class Pipe:
    """Pipes"""

    NUM_PIPES = 8
    PIPE_WIDTH = 100
    MIN_PIPE_DISTANCE = 150
    MAX_PIPE_DISTANCE = 200
    MIN_GAP = 120
    MAX_GAP = 250

    def __init__(self, x, topheight, bottomy, bottomheight):
        self.topRect = Rect(x, 0, self.PIPE_WIDTH, topheight)
        self.bottomRect = Rect(x, bottomy, self.PIPE_WIDTH, bottomheight)

        self.dx = -200
        self.dy = 0
        self.gravity = 0
        self.passed = False
