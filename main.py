import pygame
from level import Level
from draw import Draw
import sys
import os
import requests

sys.path.append(".")


def resource_path(relative_path: str):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def isnotcurrvernewest(currversion: str):
    """get the newest version number and compare it to the current one"""
    response = requests.get(
        "https://api.github.com/repos/NYC00kie/pygame_jumpandrun/releases/latest")
    version = response.json()["name"].replace("v", "")
    splitversion = version.split(".")
    currsplitversion = currversion.split(".")
    if version == currversion:
        # no new release
        return False

    elif splitversion[0] >= currsplitversion[0] or splitversion[1] >= currsplitversion[1] or splitversion[2] > currsplitversion[2]:
        # new release
        return True


def downloadnewestversion():
    pass


if __name__ == "__main__":
    currentversion = "1.2.0"
    if isnotcurrvernewest(currentversion):
        downloadnewestversion()

    pygame.init()
    pygame.font.init()
    pygame.display.set_mode((1920, 1080))
    level1 = Level(levelmatrixpath=resource_path("Levels/Level1.json.bz"),
                   levelpicpath=resource_path("Levelpictures/Level1.png"),
                   spritepath=resource_path("textures/Player_1.png"),
                   coinspritepath=resource_path("textures/Coin_1.png"),
                   winpicpath=resource_path("textures/win_1.png"),
                   levelmusicpath=resource_path("backgroundmusic/Level.mp3"),
                   pygame=pygame)

    level2 = Level(levelmatrixpath=resource_path("Levels/Level2.json.bz"),
                   levelpicpath=resource_path("Levelpictures/Level2.png"),
                   spritepath=resource_path("textures/Player_2.png"),
                   coinspritepath=resource_path("textures/Coin_2.png"),
                   winpicpath=resource_path("textures/win_2.png"),
                   levelmusicpath=resource_path("backgroundmusic/Level2.mp3"),
                   pygame=pygame)

    level3 = Level(levelmatrixpath=resource_path("Levels/Level3.json.bz"),
                   levelpicpath=resource_path("Levelpictures/Level3.png"),
                   spritepath=resource_path("textures/Player_3.png"),
                   coinspritepath=resource_path("textures/Coin_3.png"),
                   winpicpath=resource_path("textures/win_3.png"),
                   levelmusicpath=resource_path("backgroundmusic/Level.mp3"),
                   pygame=pygame)

    draw = Draw(resource_path("backgroundmusic/Homescreen.mp3"))

    draw.drawmenu([level1, level2, level3], pygame)
