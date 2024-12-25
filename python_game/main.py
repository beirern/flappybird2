from classes import Game
from pygame import quit

game = Game()
score, distance = game.run()

print(f"Score: {score}, Distance: {str(round(distance, 2))}")

quit()
