# Keras missing mypy stubs :(
import keras  # type: ignore

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
        self.model = keras.Sequential(
            [
                keras.Input(shape=(self.NUM_PARAMETERS,)),
                # keras.layers.Dense(16),
                keras.layers.Dense(8),
                # keras.layers.Dense(2),
                keras.layers.Dense(1, activation="sigmoid"),
            ]
        )
