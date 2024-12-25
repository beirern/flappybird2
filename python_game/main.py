from pygame import quit
from classes import Game

game = Game()
score, distance = game.run()

print(f"Score: {score}, Distance: {str(round(distance, 2))}")

quit()