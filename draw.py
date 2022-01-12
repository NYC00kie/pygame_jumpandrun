import sys
import pygame
import time


class Draw():
    """docstring for Draw."""

    def __init__(self):
        self.drawable_obj = []

    def collision(self, Level):
        Player = Level.Player

        bl = Player.rect.bottomleft
        print(bl[1], bl[0])
        if Level.matrix[bl[1]][bl[0]] == "Wall":
            print("""

            looooooooooooooooooooooooooooooooooooooooooooooo
            oooooooooooooooooooooooooooooooooooooooooooooooo
            oooooooooooooooooooooooooooooooooooooooooooooooo
            l

            """)

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
    from level import Level
    newlevel = Level(levelmatrixpath="Levels/Level1.png.json.bz",
                     levelpicpath="Levelpictures/Level1.png",
                     spritepath="textures/Char.png")
    pygame.init()
    draw = Draw()
    print(newlevel.size)
    draw.draw(newlevel)
