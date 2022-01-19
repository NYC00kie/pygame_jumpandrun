import time
import pygame
import sys
from level import Level
import copy
import numpy as np
from threading import Thread
sys.path.append(".")


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


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
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event, pygame):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")
                    draw = Draw()
                    draw.drawlevel(self.assignedobj, pygame)


class Draw():
    """docstring for Draw."""

    def __init__(self):
        self.drawable_obj = []

    def collision(self, Level, collided):
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

    def checkforfinish(self, Level, finished):
        finish = Level.finish
        Player = Level.Player
        print(finish)
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
        finished = []
        collided = []

        while True:

            starttime = time.time()

            if finished[0]:
                return None

            finished = []
            collided = []

            finishthread = ThreadWithReturnValue(
                target=self.checkforfinish, args=(Level, finished))
            collisionthread = ThreadWithReturnValue(
                target=self.collision, args=(Level, collided))
            pressed_keys = pygame.key.get_pressed()
            collisionthread.start()
            finishthread.start()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
                    sys.exit()

                if pressed_keys[pygame.K_DELETE]:
                    return None

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

            Player.speed = list(np.multiply(
                collided[0],
                Player.speed
                ))

            Player.rect = Player.rect.move(Player.speed)
            screen.blit(bg, (0, 0))  # draw background
            screen.blit(Player.sprite, Player.rect)
            pygame.display.flip()

            diff = time.time() - starttime

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
    newlevel = Level(levelmatrixpath="Levels/Level1.tif.json.bz",
                     levelpicpath="Levelpictures/Level1.tif",
                     spritepath="textures/Char.png")

    pygame.init()
    draw = Draw()
    print(newlevel.size)
    draw.drawmenu([newlevel, newlevel, newlevel], pygame)
