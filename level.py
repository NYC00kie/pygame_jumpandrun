from player import Player
import compress_json


class Level():
    """docstring for Level."""

    def __init__(self, levelmatrixpath: str, levelpicpath: str, pygame, levelmusicpath="backgroundmusic/Homescreen.mp3", winpicpath="textures/win_1.png", coinspritepath="textures/Coin_1.jpg", spritepath="textures/Char.png"):
        self.pygame = pygame
        self.matrixpath = levelmatrixpath
        self.matrix = compress_json.load(levelmatrixpath)
        self.picpath = levelpicpath
        self.spritepath = spritepath
        self.winpicpath = winpicpath
        self.levelmusicpath = levelmusicpath
        self.coinspritepath = coinspritepath
        self.coinsprite = self.pygame.image.load(
            self.coinspritepath).convert_alpha()
        self.size = (len(self.matrix[0]), len(self.matrix))
        self.Player = Player(self.spritepath)
        self.start = self.loadPlayerposstart()
        self.finish = self.loadfinish()
        self.obstaclelist = self.loadobstacle()
        self.coinlist = self.loadcoins()
        self.coincount = 0
        self.framecount = 0
        self.Player.rect = self.Player.rect.move(self.start)

    def loadPlayerposstart(self):
        """Get the Player x-y Position from the Level Matrix"""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "PSpawn":

                    return [j, i]

        return [0, 0]

    def loadfinish(self):
        """Get the Finish x-y Position from the Level Matrix"""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "PFinish":
                    return [j, i]

        return [0, 0]

    def loadobstacle(self):
        """Get a List of Obstacle x-y Positions from the Level Matrix"""
        obstlist = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "Obstacle":
                    obstlist.append([j, i])
        return obstlist

    def loadcoins(self):
        """Get a List of a Dictionary with a rectangle and coordiante entry"""
        coinlist = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "Coin":

                    rect = self.coinsprite.get_rect()
                    rect = rect.move([j, i])
                    coin = {
                        "cord": [j, i],
                        "rect": rect
                    }
                    coinlist.append(coin)
        print(coinlist)
        return coinlist

    def reset(self):
        """reinitialise the Level Class"""
        self.__init__(pygame=self.pygame, levelmatrixpath=self.matrixpath, levelpicpath=self.picpath,
                      winpicpath=self.winpicpath, coinspritepath=self.coinspritepath, spritepath=self.spritepath,
                      levelmusicpath=self.levelmusicpath)
