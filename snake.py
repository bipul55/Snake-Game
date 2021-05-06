import pygame
import math
scl = 10


class Snake:
    def __init__(self, win):
        self.x = 100
        self.w, self.h = pygame.display.get_surface().get_size()
        self.y = 50
        self.xSpeed = 10
        self.ySpeed = 0
        self.win = win
        self.body = [[0, 50], [10, 50], [20, 50],[30, 50], [40, 50], [50, 50], [60, 50], [70, 50], [80, 50], [90, 50]]
        self.body.append([self.x, self.y])
        self.length = len(self.body)
        self.ai = False

    def distance(self, x1, y1, x2, y2):
        # print (abs((x2-x1)^2)+((y2-y1)^2))
        number = ((x2-x1)**2)+((y2-y1)**2)

        return number

    def possible_to_move(self, x, y):
        if x >= self.w-scl or x < 0 or y >= self.h-scl or y < 0:
            return False
        for i in range(self.length - 1):
            if self.body[i] == self.body[-1]:
                return False
        return True

    def movement(self,x,y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.ai = not self.ai
        if not self.ai:
            if keys[pygame.K_LEFT] and not self.xSpeed > 0:
                self.xSpeed = -scl
                self.ySpeed = 0
            if keys[pygame.K_RIGHT] and not self.xSpeed < 0:
                self.xSpeed = scl
                self.ySpeed = 0
            if keys[pygame.K_UP] and not self.ySpeed > 0:
                self.xSpeed = 0
                self.ySpeed = -scl
            if keys[pygame.K_DOWN] and not self.ySpeed < 0:
                self.xSpeed = 0
                self.ySpeed = scl

        else:
            print(x,y, self.x,self.y)
            L = self.distance(self.x-scl, self.y, x, y)
            R = self.distance(self.x + scl, self.y, x, y)
            U = self.distance(self.x, self.y-scl, x, y)
            D = self.distance(self.x, self.y+scl, x, y)
            arr = [L, R, U, D]
            min_value = min(arr)
            min_index = arr.index(min_value)


            # if min_index == 0 :
            #     if self.xSpeed > 0:
            #         self.xSpeed = -0
            #         self.ySpeed = -scl
            #     else:
            #         self.xSpeed = -scl
            #         self.ySpeed = 0
            # elif min_index == 1:
            #     if self.xSpeed < 0 :
            #         self.xSpeed = -0
            #         self.ySpeed = scl
            #     else:
            #         self.xSpeed = scl
            #         self.ySpeed = 0
            # elif min_index == 2:
            #     if self.ySpeed > 0:
            #         self.xSpeed = scl
            #         self.ySpeed = 0
            #     else:
            #         self.xSpeed = 0
            #         self.ySpeed = -scl
            # elif min_index == 3 :
            #     # print(arr)
            #     if self.ySpeed < 0:
            #         self.xSpeed = -scl
            #         self.ySpeed = 0
            #     else:
            #         self.xSpeed = 0
            #         self.ySpeed = scl
            if min_index == 0 :
                if self.xSpeed > 0 or not self.possible_to_move(self.x-scl, self.y):
                    if self.possible_to_move(self.x, self.y- scl):
                        self.xSpeed = 0
                        self.ySpeed = -scl
                    elif self.possible_to_move(self.x, self.y+scl):
                        self.xSpeed = 0
                        self.ySpeed = scl
                else:
                    self.xSpeed = -scl
                    self.ySpeed = 0
            elif min_index == 1:
                if self.xSpeed < 0 or not self.possible_to_move(self.x+scl, self.y):
                    if self.possible_to_move(self.x, self.y- scl):
                        self.xSpeed = 0
                        self.ySpeed = -scl
                    elif self.possible_to_move(self.x, self.y+scl):
                        self.xSpeed = 0
                        self.ySpeed = scl
                else:
                    self.xSpeed = scl
                    self.ySpeed = 0
            elif min_index == 2:
                if self.ySpeed > 0 or not self.possible_to_move(self.x, self.y-scl):
                    if self.possible_to_move(self.x+scl, self.y):
                        self.xSpeed = scl
                        self.ySpeed = 0
                    elif self.possible_to_move(self.x-scl, self.y):
                        self.xSpeed = -scl
                        self.ySpeed = 0

                else:
                    self.xSpeed = 0
                    self.ySpeed = -scl
            elif min_index == 3:
                # print(arr)

                if self.ySpeed < 0 or not self.possible_to_move(self.x, self.y+scl):
                    if self.possible_to_move(self.x+scl, self.y ):
                        self.xSpeed = scl
                        self.ySpeed = 0
                    elif self.possible_to_move(self.x-scl, self.y ):
                        self.xSpeed = -scl
                        self.ySpeed = 0

                else:
                    self.xSpeed = 0
                    self.ySpeed = scl



    def update(self,x,y):
        self.movement(x,y)
        self.x += self.xSpeed
        self.y += self.ySpeed
        for i in range(self.length -1):
            self.body[i] = self.body[i+1]
        self.body[self.length-1] = [self.x, self.y]

    def eat(self):
        self.length += 1
        self.body.append([self.x, self.y])

    def draw(self):
        for i in range(self.length):
            pygame.draw.rect(self.win, (0, 0, 255), (self.body[i][0], self.body[i][1], scl, scl))

    def endGame(self):
        if self.x >= self.w-scl or self.x < 0 or self.y >= self.h-scl or self.y < 0:
            return True
        for i in range(self.length - 1):
            if self.body[i] == self.body[-1]:
                return True
        return False
