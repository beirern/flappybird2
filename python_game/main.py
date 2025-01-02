import argparse
import copy
import json

from classes import Agent, Game
from pygame import quit

parser = argparse.ArgumentParser()

parser.add_argument(
    "--train", action=argparse.BooleanOptionalAction, default=False, help="Train AI"
)

args = parser.parse_args()

if args.train:
    best_previous_agent: Agent | None
    try:
        with open(Agent.FILE_PATH, "r") as f:
            agent_info = json.load(f)
        best_previous_agent = Agent(agent_info["params"], agent_info["score"])
    except Exception:
        best_previous_agent = None

    epoch = 1
    game = Game(args.train, best_agent=best_previous_agent)
    father, mother = game.run_training()
    # Masogynistic
    best_agent = father

    while epoch < 200:
        game = Game(args.train, father, mother, best_agent)
        father, mother = game.run_training()
        if best_agent.score < father.score:
            best_agent = copy.deepcopy(father)
        epoch += 1

        print(f"Epoch: {epoch}")
        print(f"Game Score: {father.score}, Best Score: {best_agent.score}")

    if best_previous_agent is None or (
        best_previous_agent is not None and best_previous_agent.score < best_agent.score
    ):
        best_agent.save()
else:
    score = 0

    while score < 1:
        game = Game(args.train)
        score, distance = game.run_game()

    print(f"Score: {score}")
quit()
