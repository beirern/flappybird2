from pygame import Rect


class Pipe:
    """Pipes"""

    NUM_PIPES: int = 8
    PIPE_WIDTH: int = 100
    # Distance between pipes
    MIN_PIPE_DISTANCE: int = 180
    MAX_PIPE_DISTANCE: int = 220
    # Size of gap in pipes
    MIN_GAP: int = 150
    MAX_GAP: int = 200
    # Height difference between gaps in pipes
    MIN_HEIGHT_DIFF: int = 50
    MAX_HEIGHT_DIFF: int = 300

    def __init__(self, x: int, topheight: int, bottomy: int, bottomheight: int, id: int):
        self.topRect = Rect(x, 0, self.PIPE_WIDTH, topheight)
        self.bottomRect = Rect(x, bottomy, self.PIPE_WIDTH, bottomheight)

        self.dx: int = -200
        self.dy: int = 0
        self.gravity: int = 0
        self.id = id
