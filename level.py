from player import Player
import compress_json


class Level():
    """docstring for Level."""

    def __init__(self, levelmatrixpath, levelpicpath, spritepath="textures/Char.png"):
        self.matrix = compress_json.load(levelmatrixpath)
        self.picpath = levelpicpath
        self.spritepath = spritepath
        self.size = (len(self.matrix[0]), len(self.matrix))
        self.Player = Player(self.spritepath)
        self.start = self.loadPlayerposstart()
        self.finish = self.loadfinish()
        self.Player.rect = self.Player.rect.move(self.start)

    def loadPlayerposstart(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "PSpawn":

                    return [j, i]

        return [0, 0]

    def loadfinish(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "PFinish":
                    return [j, i]

        return [0, 0]

    def reset(self):
        self.Player = Player(self.spritepath)
        self.Player.rect = self.Player.rect.move(self.start)
