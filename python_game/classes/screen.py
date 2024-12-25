import pygame

class Screen:
    """Screen"""
    def __init__(self, requested_width: int, requested_height: int):
        self.surface = pygame.display.set_mode((requested_width, requested_height))
        self.surface.fill("white")
        self.width, self.height = self.surface.get_size()
        # self.topleft = pygame.Vector2(0, 0)

        # self.image = pygame.image.load(background_image_path).convert()
        # self.max_width, self.max_height = pygame.Vector2(self.image.get_size())
        # self.screen = pygame.display.set_mode((1280, 720))
