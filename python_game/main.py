import argparse

from classes import Game
from pygame import quit

parser = argparse.ArgumentParser()

parser.add_argument(
    "--train", action=argparse.BooleanOptionalAction, default=False, help="Train AI"
)

args = parser.parse_args()

if args.train:
    epoch = 1
    game = Game(args.train)
    ancestors = game.run_training()

    while epoch < 100:
        game = Game(args.train, ancestors)
        ancestors = game.run_training()
        epoch += 1
else:
    score = 0

    while score < 1:
        game = Game(args.train)
        score, distance = game.run_game()

quit()
