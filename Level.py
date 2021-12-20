from player import Player
import compress_json


class Level(object):
    """docstring for Level."""

    def __init__(self, levelmatrixpath):
        super(self).__init__()
        self.matrix = compress_json.load(levelmatrixpath)
        self.levelsize = (len(self.levelmatrix), len(self.levelmatrix[0]))
        self.Player = Player()
