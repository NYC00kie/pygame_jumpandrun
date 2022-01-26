import pygame
from level import Level
from draw import Draw
import sys
sys.path.append(".")


if __name__ == "__main__":
    pygame.init()
    level1 = Level(levelmatrixpath="Levels/Level1.json.bz",
                   levelpicpath="Levelpictures/Level1.png",
                   spritepath="textures/Player_1.png",
                   winpicpath="textures/win_1.png",
                   levelmusicpath="backgroundmusic/Level.mp3")

    level2 = Level(levelmatrixpath="Levels/Level2.json.bz",
                   levelpicpath="Levelpictures/Level2.png",
                   spritepath="textures/Player_2.png",
                   winpicpath="textures/win_2.png",
                   levelmusicpath="backgroundmusic/Level.mp3")

    level3 = Level(levelmatrixpath="Levels/Level3.json.bz",
                   levelpicpath="Levelpictures/Level3.png",
                   spritepath="textures/Player_3.png",
                   winpicpath="textures/win_3.png",
                   levelmusicpath="backgroundmusic/Level.mp3")

    draw = Draw("backgroundmusic/Homescreen.mp3")

    draw.drawmenu([level1, level2, level3], pygame)
