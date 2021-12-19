class Draw(object):
    """docstring for Draw."""

    def __init__(self, arg):
        super(Draw, self).__init__()
        self.arg = arg
        self.drawable_obj = []

    def draw(levelpicpath, Level, Player):
        import sys
        import pygame
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[pygame.K_a]:
                Player.speed[0] += -1
            elif pressed_keys[pygame.K_d]:
                Player.speed[0] += 1
            else:
                if Player.speed[0] > 0:
                    Player.speed[0] += -0.5
                elif Player.speed[0] < 0:
                    Player.speed[0] += 0.5
            if pressed_keys[pygame.K_SPACE]:
                pass
