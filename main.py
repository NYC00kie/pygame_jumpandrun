import pygame
from level import Level
from draw import Draw
if __name__ == "__main__":
    pygame.init()
    level1 = Level(levelmatrixpath="Levels/Level1.tif.json.bz",
                   levelpicpath="Levelpictures/Level1.tif",
                   spritepath="textures/Char.png")

    level2 = Level(levelmatrixpath="Levels/Level1.tif.json.bz",
                   levelpicpath="Levelpictures/Level1.tif",
                   spritepath="textures/Char.png")

    level3 = Level(levelmatrixpath="Levels/Level1.tif.json.bz",
                   levelpicpath="Levelpictures/Level1.tif",
                   spritepath="textures/Char.png")

    draw = Draw()

    draw.drawmenu([level1, level2, level3], pygame)
