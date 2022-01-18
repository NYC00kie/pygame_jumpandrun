import sys
import pygame
import time
from level import Level
import copy
import numpy as np


class Draw():
    """docstring for Draw."""

    def __init__(self):
        self.drawable_obj = []

    def collision(self, Level):
        """calculates if the player collides with an object """
        Player = Level.Player

        speed = copy.deepcopy(Player.speed)
        copyPlayerrect = copy.deepcopy(Player.rect)

        copyPlayerrect = copyPlayerrect.move(speed)

        for i in range(copyPlayerrect.topleft[1], copyPlayerrect.bottomright[1]):
            # skip itteration if there is no Wall
            if "Wall" not in Level.matrix[i]:
                continue

            for j in range(copyPlayerrect.topleft[0], copyPlayerrect.bottomright[0]):
                if Level.matrix[i][j] == "Wall" and copyPlayerrect.collidepoint(j, i):
                    return [0, 0]

        return [1, 1]

    def checkforfinish(self, Level):
        finish = Level.finish
        Player = Level.Player
        print(finish)
        if Player.rect.collidepoint(finish[0], finish[1]):
            print("finished")
            return True
        else:
            return False

    def drawlevel(self, Level):

        Player = Level.Player
        bg = pygame.image.load(Level.picpath)
        screen = pygame.display.set_mode(Level.size)
        self.drawable_obj.append(Player)
        while True:

            if self.checkforfinish(Level):
                return None

            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
                    sys.exit()

            if pressed_keys[pygame.K_a]:
                Player.speed[0] += -2
            elif pressed_keys[pygame.K_d]:
                Player.speed[0] += 2
            else:
                if Player.speed[0] > 0:
                    Player.speed[0] += -1
                elif Player.speed[0] < 0:
                    Player.speed[0] += 1
            if pressed_keys[pygame.K_SPACE]:
                Player.speed[1] += -5
            else:
                Player.speed[1] += 1

            # speedlimit
            if Player.speed[0] > 10:
                Player.speed[0] = 10
            elif Player.speed[0] < -10:
                Player.speed[0] = -10
            if Player.speed[1] > 10:
                Player.speed[1] = 10
            elif Player.speed[1] < -10:
                Player.speed[1] = -10

            print(Player.speed, "speet")

            Player.speed = list(np.multiply(
                self.collision(Level),
                Player.speed
                ))

            Player.rect = Player.rect.move(Player.speed)
            screen.blit(bg, (0, 0))  # draw background
            screen.blit(Player.sprite, Player.rect)
            pygame.display.flip()
            time.sleep(0.05)


if __name__ == "__main__":
    newlevel = Level(levelmatrixpath="Levels/Level1.tif.json.bz",
                     levelpicpath="Levelpictures/Level1.tif",
                     spritepath="textures/Char.png")

    pygame.init()
    draw = Draw()
    print(newlevel.size)
    draw.drawlevel(newlevel)
