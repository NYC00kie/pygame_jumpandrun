import sys
import pygame
import time
from level import Level
import copy


class Draw():
    """docstring for Draw."""

    def __init__(self):
        self.drawable_obj = []

    def collision(self, Level, res=10):
        Player = Level.Player

        speed = copy.deepcopy(Player.speed)

        bl = Player.rect.bottomleft

        speed[0] = speed[0] / res
        speed[1] = speed[1] / res

        print(speed)
        P1 = copy.deepcopy(Player.rect)
        Player.rect = Player.rect.move(speed)
        #time.sleep(1)
        if Player.rect.bottomleft == P1.bottomleft:
            print(
                f"{Player.rect.bottomleft} == {P1.bottomleft} is {Player.rect.bottomleft == P1.bottomleft}")
            print("oyy")
        #for i in range(res):
        #    pass
        #
        #print(bl[1], bl[0])
        #if Level.matrix[bl[1]][bl[0]] == "Wall":
        #    print("""

        #    looooooooooooooooooooooooooooooooooooooooooooooo
        #    oooooooooooooooooooooooooooooooooooooooooooooooo
        #    oooooooooooooooooooooooooooooooooooooooooooooooo
        #    l

        #    """)

    def draw(self, Level):

        Player = Level.Player
        bg = pygame.image.load(Level.picpath)
        screen = pygame.display.set_mode(Level.size)
        self.drawable_obj.append(Player)
        while True:

            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
                    sys.exit()

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
                Player.speed[1] += -5
            else:
                Player.speed[1] += 1

            self.collision(Level)

            print(Player.rect.bottomleft)
            Player.rect = Player.rect.move(Player.speed)
            screen.blit(bg, (0, 0))  # draw background
            screen.blit(Player.sprite, Player.rect)
            pygame.display.flip()
            time.sleep(0.05)


if __name__ == "__main__":
    newlevel = Level(levelmatrixpath="Levels/Level1.png.json.bz",
                     levelpicpath="Levelpictures/Level1.png",
                     spritepath="textures/Char.png")
    pygame.init()
    draw = Draw()
    print(newlevel.size)
    draw.draw(newlevel)
