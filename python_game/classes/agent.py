import json
import typing

import numpy as np

from .character import Character


class Agent(Character):
    """Non-Player Character"""

    INPUT_SIZE = 5
    HIDDEN_SIZE = 8
    OUTPUT_SIZE = 1

    FILE_PATH = "agent.json"

    def __init__(
        self,
        params: np.ndarray[typing.Any, np.dtype[np.float64]] | None = None,
        score: int = 0,
    ) -> None:
        super().__init__()

        # Neural network architecture: input -> hidden -> output
        # weights_ih: input to hidden (5x8), bias_h: hidden bias (8,)
        # weights_ho: hidden to output (8x1), bias_o: output bias (1,)
        total_params = (self.INPUT_SIZE * self.HIDDEN_SIZE + self.HIDDEN_SIZE +
                       self.HIDDEN_SIZE * self.OUTPUT_SIZE + self.OUTPUT_SIZE)

        if params is not None:
            self.params = params
        else:
            # Initialize with Xavier/Glorot initialization
            self.params = np.random.normal(0, 0.5, size=(total_params,))

        self.score = score

    def predict(self, input_params: np.ndarray) -> float:
        # Ensure input is flattened and normalized
        inputs = input_params.flatten()

        # Extract weights and biases
        idx = 0
        weights_ih = self.params[idx:idx + self.INPUT_SIZE * self.HIDDEN_SIZE].reshape(self.INPUT_SIZE, self.HIDDEN_SIZE)
        idx += self.INPUT_SIZE * self.HIDDEN_SIZE

        bias_h = self.params[idx:idx + self.HIDDEN_SIZE]
        idx += self.HIDDEN_SIZE

        weights_ho = self.params[idx:idx + self.HIDDEN_SIZE * self.OUTPUT_SIZE].reshape(self.HIDDEN_SIZE, self.OUTPUT_SIZE)
        idx += self.HIDDEN_SIZE * self.OUTPUT_SIZE

        bias_o = self.params[idx:idx + self.OUTPUT_SIZE]

        # Forward pass: input -> hidden
        hidden = np.tanh(np.dot(inputs, weights_ih) + bias_h)

        # Forward pass: hidden -> output
        output = 1 / (1 + np.exp(-(np.dot(hidden, weights_ho) + bias_o)))

        return output[0]

    def save(self) -> None:
        f = open(self.FILE_PATH, "w")
        data = {"score": self.score, "params": self.params.tolist()}
        f.write(json.dumps(data))
        f.close()
