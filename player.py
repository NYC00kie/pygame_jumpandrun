class Player(object):
    """docstring for Player."""

    def __init__(self, arg):
        super(self).__init__()
        self.arg = arg
        self.posx = 0
        self.posy = 0
        self.speed = [0, 0]
        self.spritepath = None
