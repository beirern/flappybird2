import numpy as np

from .character import Character


class Agent(Character):
    """Non-Player Character"""

    PARAMETERS = [
        "dy",
        "top_rect_y",
        "bottom_rect_y",
        "left_rect",
        "right_rect",
        "top_screen",
        "bottom_screen",
    ]
    NUM_PARAMETERS: int = len(PARAMETERS)

    def __init__(self) -> None:
        super().__init__()
        self.params = np.random.normal(size=(self.NUM_PARAMETERS,))

    def predict(self, input_params: np.ndarray) -> float:
        return 1 / (1 + np.exp(-np.dot(input_params, self.params)))
