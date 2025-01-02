import json
import typing

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
    ]
    NUM_PARAMETERS: int = len(PARAMETERS)
    FILE_PATH = "agent.json"

    def __init__(
        self,
        params: np.ndarray[typing.Any, np.dtype[np.float64]] | None = None,
        score: int = 0,
    ) -> None:
        super().__init__()
        if params:
            self.params = params
        else:
            self.params = np.random.normal(size=(self.NUM_PARAMETERS,))
        self.score = score

    def predict(self, input_params: np.ndarray) -> float:
        return 1 / (1 + np.exp(-np.dot(input_params, self.params)))

    def save(self) -> None:
        f = open(self.FILE_PATH, "w")
        data = {"score": self.score, "params": self.params.tolist()}
        f.write(json.dumps(data))
        f.close()
