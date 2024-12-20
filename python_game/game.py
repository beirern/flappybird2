import pygame

from classes import Character
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("flappy bird")
player = Character()
dt = 0

# fill the screen with a color to wipe away anything from last frame
screen.fill("white")

def run(running, player, screen, dt):
  while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
      match event.type:
        case pygame.QUIT:
          running = False
        case pygame.KEYDOWN:
          if (event.key == pygame.K_ESCAPE):
            running = False
          elif (event.key == pygame.K_SPACE):
            player.dy = -50
    
    update(player, dt)
    render(screen, player)

    dt = clock.tick(60) / 1000

def update(player, dt):
  player.x += player.dx * dt
  player.y += player.dy * dt + 0.5 * (dt ** 2) * player.gravity
  player.dy += 30 * dt
  pygame.event.pump()


def render(screen, player):
  screen.fill("white")
  pygame.draw.circle(screen, "green", pygame.Vector2((player.x, player.y)), player.radius)
  pygame.display.flip()

run(running, player, screen, dt)