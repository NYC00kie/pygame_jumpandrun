import pygame


class Player():
    """docstring for Player."""

    def __init__(self, spritepath: str):
        self.startx = 0
        self.starty = 0
        self.speed = [0, 0]
        self.spritepath = spritepath
        self.sprite = pygame.image.load(spritepath)
        self.rect = self.sprite.get_rect()
