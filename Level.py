from player import Player


class Level(object):
    """docstring for Level."""

    def __init__(self, levelmatrix):
        super(self).__init__()
        self.matrix = levelmatrix
        self.levelsize = (len(levelmatrix), len(levelmatrix[0]))
        self.Player = Player()
