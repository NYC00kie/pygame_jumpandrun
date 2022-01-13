from player import Player
import compress_json


class Level():
    """docstring for Level."""

    def __init__(self, levelmatrixpath, levelpicpath, spritepath="textures/Char.png"):
        self.matrix = compress_json.load(levelmatrixpath)
        self.picpath = levelpicpath
        self.size = (len(self.matrix[0]), len(self.matrix))
        self.Player = Player(spritepath)
        self.start = self.loadPlayerposstart()
        print(self.start)
        self.Player.rect = self.Player.rect.move(self.start)

    def loadPlayerposstart(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "PSpawn":
                    print("lol")
                    return [j, i]

        return [0, 0]
