from player import Player
import compress_json


class Level():
    """docstring for Level."""

    def __init__(self, levelmatrixpath, levelpicpath, spritepath="textures/Char.png"):
        self.matrix = compress_json.load(levelmatrixpath)
        self.picpath = levelpicpath
        self.size = (len(self.matrix[0]), len(self.matrix))
        self.Player = Player(spritepath)
