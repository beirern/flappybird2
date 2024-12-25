import pygame


class Screen:
    """Screen"""

    def __init__(self, requested_width: int, requested_height: int):
        self.surface = pygame.display.set_mode((requested_width, requested_height))
        self.surface.fill("white")
        self.width, self.height = self.surface.get_size()
