import pygame
import random

from classes import Character, Pipe, Screen

class Game:
  """The Game"""
  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.running = True
    self.dt = 0.0
    self.screen = Screen(1280, 720)
    pygame.display.set_caption("flappy bird")
    self.score = 0
    self.distance = 0

    self.character = Character()
    self.pipes = [Pipe(600, 200, 400, 320), Pipe(1000, 50, 500, 220)]

  def run(self):
    while self.running:
      # poll for events
      # pygame.QUIT event means the user clicked X to close your window
      for event in pygame.event.get():
        match event.type:
          case pygame.QUIT:
            self.running = False
          case pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE):
              self.running = False
            elif (event.key == pygame.K_SPACE):
              self.character.dy = -275
      self.update()
      self.render()
      self.dt = self.clock.tick(60) / 1000
    
    return self.score, self.distance

  def update(self):
    proposed_y = self.character.rect.y + self.character.dy * self.dt + 0.5 * (self.dt ** 2) * self.character.gravity

    if proposed_y < 0:
      self.character.rect.y = 0
    elif proposed_y + self.character.rect.height > self.screen.height:
      self.character.rect.y = self.screen.height - self.character.rect.height
    else:
      self.character.rect.y = proposed_y

    self.character.dy += 300 * self.dt
    if self.pipes[0].topRect.x + self.pipes[0].topRect.width < 0:
      self.pipes.pop(0)
    for pipe in self.pipes:
      pipe.topRect.x += pipe.dx * self.dt
      pipe.bottomRect.x += pipe.dx * self.dt

    if self.character.rect.colliderect(self.pipes[0].topRect) or self.character.rect.colliderect(self.pipes[0].bottomRect):
      self.running = False
    
    if len(self.pipes) < Pipe.NUM_PIPES:
      for _ in range(Pipe.NUM_PIPES - len(self.pipes)):
        x = self.pipes[-1].topRect.right + random.randint(Pipe.MIN_PIPE_DISTANCE, Pipe.MAX_PIPE_DISTANCE)
        gap = random.randint(Pipe.MIN_GAP, Pipe.MAX_GAP)
        topheight = random.randint(0, self.screen.height - gap)
        bottomy = topheight + gap
        bottomheight = self.screen.height - bottomy
        self.pipes.append(Pipe(x, topheight, bottomy, bottomheight))
    
    if self.character.rect.left > self.pipes[0].topRect.right and not self.pipes[0].passed:
      self.score += 1
      self.pipes[0].passed = True

    self.distance -= self.pipes[0].dx * self.dt
    pygame.event.pump()

  def render(self):
    self.screen.surface.fill("white")
    self.character.rect = pygame.draw.rect(self.screen.surface, "green", self.character.rect)
    for pipe in self.pipes:
      pygame.draw.rect(self.screen.surface, "red", pipe.topRect)
      pygame.draw.rect(self.screen.surface, "red", pipe.bottomRect)
    score_text = pygame.font.Font('freesansbold.ttf', 50).render(str(self.score), True, "black")
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (20, 35)
    self.screen.surface.blit(score_text, score_text_rect)

    distance_text = pygame.font.Font('freesansbold.ttf', 50).render(str(round(self.distance, 2)), True, "black")
    distance_text_rect = distance_text.get_rect()
    distance_text_rect.center = (100, 80)
    self.screen.surface.blit(distance_text, distance_text_rect)
    pygame.display.update()
    pygame.display.flip()
