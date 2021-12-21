import pygame


class Player():
    """docstring for Player."""

    def __init__(self, spritepath):
        self.posx = 0
        self.posy = 0
        self.speed = [0, 0]
        self.spritepath = spritepath
        self.sprite = pygame.image.load(spritepath)
        self.rect = self.sprite.get_rect()
