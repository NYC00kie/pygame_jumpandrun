import time
import pygame
import sys
from level import Level
import copy
import numpy as np

sys.path.append(".")


class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text,  pos, font, assignedobj, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.assignedobj = assignedobj
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        print(self.size)
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(
            self.x-0.5*self.size[0], self.y, self.size[0], self.size[1])

    def show(self, screen):
        screen.blit(self.surface, (self.x-(0.5*self.size[0]), self.y))

    def click(self, event, pygame):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")
                    draw = Draw()
                    draw.drawlevel(self.assignedobj, pygame)
                    self.assignedobj.reset()


class Draw():
    """docstring for Draw."""

    def __init__(self):
        self.drawable_obj = []

    def collision_wall(self, Level):
        """calculates if the player collides with a wall """
        Player = Level.Player

        speed = copy.deepcopy(Player.speed)
        copyPlayerrect = copy.deepcopy(Player.rect)

        copyPlayerrect = copyPlayerrect.move(speed)
        # only itterate through the height and width of the sprite for optimisation purposes
        for i in range(copyPlayerrect.topleft[1], copyPlayerrect.bottomright[1]):
            # skip itteration if there is no Wall
            if "Wall" not in Level.matrix[i]:
                continue

            for j in range(copyPlayerrect.topleft[0], copyPlayerrect.bottomright[0]):
                if Level.matrix[i][j] == "Wall" and copyPlayerrect.collidepoint(j, i):
                    return [0, 0]

        return [1, 1]

    def collison_obstacle(self, Level):
        """calculates if the Player collides with an obstacle and then resets the level"""
        Player = Level.Player
        for cord in Level.obstaclelist:
            if Player.rect.collidepoint(cord):
                Level.reset()

    def checkforfinish(self, Level):
        finish = Level.finish
        Player = Level.Player
        if Player.rect.collidepoint(finish[0], finish[1]):
            print("finished")
            return True
        else:
            return False

    def drawlevel(self, Level, pygame):

        Player = Level.Player
        bg = pygame.image.load(Level.picpath)
        screen = pygame.display.set_mode(Level.size)
        self.drawable_obj.append(Player)

        while True:

            starttime = time.time()

            if self.checkforfinish(Level):
                return None

            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                # exits the programm if you X out of it or if you press escape
                if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
                    sys.exit()

                # returns to the menu screen if the del key is pressed
                if pressed_keys[pygame.K_DELETE]:
                    return None

            # speed calculation
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

            # multiplies the speed list with a returned list from the
            # collision function which keeps the speed as it is or
            # it multiplies it with zeros. This stops falling through walls
            Player.speed = list(np.multiply(
                self.collision_wall(Level),
                Player.speed
                ))

            Player.rect = Player.rect.move(Player.speed)
            screen.blit(bg, (0, 0))  # draw background
            screen.blit(Player.sprite, Player.rect)
            pygame.display.flip()

            diff = time.time() - starttime

            # keeping the amount of ticks (computation cycles) per second roughly the same
            # which in return results in a constant and playable playspeed
            if diff < 1/30:
                time.sleep(1/30-(diff))

    def drawmenu(self, Levelist, pygame):

        # light shade of the button
        color_light = (100, 100, 100)

        screen = pygame.display.set_mode(Levelist[0].size)
        width = screen.get_width()
        height = screen.get_height()
        texts = []
        for i in range(-1, 2):
            btn = Button(f"Level {i+1}", (width/2, height/2+50*i),
                         font=35, assignedobj=Levelist[i+1], bg=color_light, feedback=f"Finished {i+1}")
            texts.append(btn)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                for btn in texts:
                    btn.click(event, pygame)
            screen.fill((60, 25, 60))

            for i in texts:
                i.show(screen)

            pygame.display.update()


if __name__ == "__main__":
    pass
