import argparse
import os

from classes import Game
from pygame import quit

parser = argparse.ArgumentParser()

parser.add_argument(
    "--train", action=argparse.BooleanOptionalAction, default=False, help="Train AI"
)

os.environ["KERAS_BACKEND"] = "tensorflow"

args = parser.parse_args()

score = 0
while score < 1:
    game = Game(args.train)
    score, distance = game.run()

    text = f"Score: {score}, Distance: {str(round(distance, 2))}"
    if args.train:
        text += f", AI Score: {distance ** (score + 1)}"
    print(text)

quit()
