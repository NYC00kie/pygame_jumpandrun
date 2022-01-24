from draw import Draw
from level import Level
import pygame
import sys
sys.path.append(".")
if __name__ == "__main__":
    pygame.init()
    level1 = Level(levelmatrixpath="Levels/Level1.json.bz",
                   levelpicpath="Levelpictures/Level1.png",
                   spritepath="textures/Char.png")

    level2 = Level(levelmatrixpath="Levels/Level2.json.bz",
                   levelpicpath="Levelpictures/Level2.png",
                   spritepath="textures/Char.png")

    level3 = Level(levelmatrixpath="Levels/Level_test.json.bz",
                   levelpicpath="Levelpictures/Level_test.tif",
                   spritepath="textures/Char.png")

    draw = Draw("backgroundmusic/Homescreen.mp3")

    draw.drawmenu([level1, level2, level3], pygame)
