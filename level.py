from player import Player
import compress_json


class Level():
    """docstring for Level."""

    def __init__(self, levelmatrixpath, levelpicpath, levelmusicpath="backgroundmusic/Homescreen.mp3", winpicpath="textures/win_1.png", spritepath="textures/Char.png"):
        self.matrixpath = levelmatrixpath
        self.matrix = compress_json.load(levelmatrixpath)
        self.picpath = levelpicpath
        self.spritepath = spritepath
        self.winpicpath = winpicpath
        self.levelpicpath = levelmusicpath
        self.size = (len(self.matrix[0]), len(self.matrix))
        self.Player = Player(self.spritepath)
        self.start = self.loadPlayerposstart()
        self.finish = self.loadfinish()
        self.obstaclelist = self.loadobstacle()
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

    def loadobstacle(self):
        obstlist = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "Obstacle":
                    obstlist.append([j, i])
        return obstlist

    def reset(self):
        self.__init__(levelmatrixpath=self.matrixpath, levelpicpath=self.picpath,
                      winpicpath=self.winpicpath, spritepath=self.spritepath,
                      levelmusicpath=self.levelmusicpath)
