#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hero
import pygame
import time
import math



MOVE_SPEED = 500
INDENTION = 5

class Game:
    def __init__(self, list_moving, screen):
        self.x = 10
        self.y = 10
        self.figure = hero.Hero(self.x, self.y)
        self.list_moving = list_moving
        self.state_moving = 0
        self.state_part = 0
        self.xvel = 0
        self.yvel = 0
        self.last_time = time.time()
        self.dt = 0
        self.screen = screen
        self.game_loop = True
        self.pred_v = 0
        self.WIN_WIDTH = screen.get_width()
        self.WIN_HEIGHT = screen.get_height()


    def move(self, cond, succesful_finish):
        if cond():
            if not (self.state_moving < len(self.list_moving)):
                self.game_loop = False
                succesful_finish()
                return
            elif self.list_moving[self.state_moving] == "square":
                self.__square__()
            elif self.list_moving[self.state_moving] == "eight":
                self.__eight__()
            elif self.list_moving[self.state_moving] == "down-up":
                self.__down_up__()
            elif self.list_moving[self.state_moving] == "x-moving":
                self.__x_moving__()
            elif self.list_moving[self.state_moving] == "left-right":
                self.__left_right__()
            elif self.list_moving[self.state_moving] == "zigzag":
                self.__zigzag__()
            elif self.list_moving[self.state_moving] == "circle":
                self.__circle__()
            elif self.list_moving[self.state_moving] == "second eight":
                self.__eight_second_type_()
            self.dt = time.time() - self.last_time
            v_x = self.xvel * self.dt
            v_y = self.yvel * self.dt
            self.x += v_x
            self.y += v_y
            self.pred_v = math.sqrt(v_y**2 + v_x**2)

        else:
            self.xvel = 0
            self.yvel = 0
        self.last_time = time.time()
        self.figure.draw(self.screen, self.x, self.y)


    def __go_to_point__(self, x, y):
        dx = x - self.x
        dy = y - self.y
        hypotenuse = math.sqrt((dx ** 2) + (dy ** 2))
        self.xvel = dx * MOVE_SPEED / hypotenuse
        self.yvel = dy * MOVE_SPEED / hypotenuse
        if hypotenuse < self.pred_v:
            return True
        else:
            return False



    def __square__(self):
        if self.state_part == 0:
            if self.__go_to_point__(INDENTION,
                                    INDENTION):
                self.state_part = 1
                self.xvel = 0
                self.yvel = 0

        #движение вправо
        if self.state_part == 1:
            if self.__go_to_point__(self.WIN_WIDTH - INDENTION - hero.WIDTH, INDENTION):
                self.state_part = 2
                self.yvel = 0
                self.xvel = 0


        #Движение вниз
        if self.state_part == 2:
            if self.__go_to_point__(self.WIN_WIDTH - INDENTION - hero.WIDTH,
                                    self.WIN_HEIGHT - INDENTION - hero.HEIGHT):
                self.state_part = 3
                self.xvel = 0
                self.yvel = 0

        #Движение влево
        if self.state_part == 3:
            if self.__go_to_point__(INDENTION,
                                    self.WIN_HEIGHT - INDENTION - hero.HEIGHT):
                self.state_part = 4
                self.xvel = 0
                self.yvel = 0

        #движение вверх
        if self.state_part == 4:
            if self.__go_to_point__(INDENTION, INDENTION):
                self.state_part = 0
                self.xvel = 0
                self.yvel = 0
                self.state_moving +=1



    def __eight__(self):
        if self.state_part == 0:
            if self.__go_to_point__(INDENTION,
                                    INDENTION):
                self.state_part = 1
                self.xvel = 0
                self.yvel = 0

        #движение влево-вниз
        if self.state_part == 1:
            if self.__go_to_point__(self.WIN_WIDTH - INDENTION - hero.WIDTH,
                                    self.WIN_HEIGHT - INDENTION - hero.HEIGHT):
                self.state_part = 2
                self.xvel = 0
                self.yvel = 0

        #движение вверх, прям как фильм ;)
        if self.state_part == 2:
            if self.__go_to_point__(self.WIN_WIDTH - INDENTION - hero.WIDTH,
                                    INDENTION):
                self.state_part = 3
                self.xvel = 0
                self.yvel = 0

        #движение влево вниз
        if self.state_part == 3:
            if self.__go_to_point__(INDENTION,
                                    self.WIN_HEIGHT - INDENTION - hero.HEIGHT):
                self.state_part = 4
                self.xvel = 0
                self.yvel = 0

        #движение вверх
        if self.state_part == 4:
            if self.__go_to_point__(INDENTION,
                                    INDENTION):
                self.state_part = 0
                self.xvel = 0
                self.yvel = 0
                self.state_moving += 1

    def __down_up__(self):
        if self.state_part == 0:
            if self.__go_to_point__(INDENTION,
                                    INDENTION):
                self.state_part = 1
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 1:
            if self.__go_to_point__(INDENTION, self.WIN_HEIGHT - INDENTION - hero.HEIGHT):
                self.state_part = 2
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 2:
            if self.__go_to_point__(INDENTION, INDENTION):
                self.xvel = 0
                self.yvel = 0
                self.state_part = 0
                self.state_moving += 1

    def __x_moving__(self):
        if self.state_part == 0:
            if self.__go_to_point__(INDENTION,
                                    INDENTION):
                self.state_part = 1
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 1:
            if self.__go_to_point__((self.WIN_WIDTH-hero.WIDTH)/2,
                                    (self.WIN_HEIGHT - hero.HEIGHT)/2):
                self.state_part = 2
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 2:
            if self.__go_to_point__(INDENTION,
                                    self.WIN_HEIGHT - INDENTION - hero.HEIGHT):
                self.state_part = 3
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 3:
            if self.__go_to_point__((self.WIN_WIDTH-hero.WIDTH)/2,
                                    (self.WIN_HEIGHT - hero.HEIGHT)/2):
                self.state_part = 4
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 4:
            if self.__go_to_point__(self.WIN_WIDTH-hero.WIDTH - INDENTION,
                                    self.WIN_HEIGHT - hero.HEIGHT - INDENTION):
                self.state_part = 5
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 5:
            if self.__go_to_point__((self.WIN_WIDTH-hero.WIDTH)/2,
                                    (self.WIN_HEIGHT - hero.HEIGHT)/2):
                self.state_part = 6
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 6:
            if self.__go_to_point__(self.WIN_WIDTH-hero.WIDTH - INDENTION,
                                    INDENTION):
                self.state_part = 8
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 8:
            if self.__go_to_point__((self.WIN_WIDTH-hero.WIDTH)/2,
                                    (self.WIN_HEIGHT - hero.HEIGHT)/2):
                self.state_part = 9
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 9:
            if self.__go_to_point__(INDENTION,
                                    INDENTION):
                self.state_part = 0
                self.xvel = 0
                self.yvel = 0
                self.state_moving += 1


    def __left_right__(self):
        if self.state_part == 0:
            if self.__go_to_point__(INDENTION,
                                    INDENTION):
                self.state_part = 1
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 1:
            if self.__go_to_point__(self.WIN_WIDTH - hero.WIDTH - INDENTION,
                                    INDENTION):
                self.state_part = 2
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 2:
            if self.__go_to_point__(INDENTION,
                                    INDENTION):
                self.state_part = 0
                self.xvel = 0
                self.yvel = 0
                self.state_moving += 1

    def __eight_second_type_(self):
        if self.state_part == 0:
            if self.__go_to_point__(INDENTION,
                                    INDENTION):
                self.state_part = 1
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 1:
            if self.__go_to_point__(self.WIN_WIDTH - INDENTION - hero.WIDTH,
                                    INDENTION):
                self.state_part = 2
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 2:
            if self.__go_to_point__(INDENTION,
                                    self.WIN_HEIGHT - INDENTION - hero.HEIGHT):
                self.state_part = 3
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 3:
            if self.__go_to_point__(self.WIN_WIDTH - INDENTION - hero.WIDTH,
                                    self.WIN_HEIGHT - INDENTION - hero.HEIGHT):
                self.state_part = 4
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 4:
            if self.__go_to_point__(INDENTION,
                                    INDENTION):
                self.state_part = 0
                self.xvel = 0
                self.yvel = 0
                self.state_moving += 1


    def __zigzag__(self):
        if self.state_part == 0:
            if self.__go_to_point__(INDENTION,
                                    self.WIN_HEIGHT/3):
                self.state_part = 1
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 1:
            if self.__go_to_point__(self.WIN_WIDTH/4,
                                    2*self.WIN_HEIGHT/3):
                self.state_part = 2
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 2:
            if self.__go_to_point__(2*self.WIN_WIDTH/4,
                                    self.WIN_HEIGHT/3):
                self.state_part = 3
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 3:
            if self.__go_to_point__(3*self.WIN_WIDTH/4,
                                    2*self.WIN_HEIGHT/3):
                self.state_part = 4
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 4:
            if self.__go_to_point__(self.WIN_WIDTH - hero.WIDTH - INDENTION,
                                    self.WIN_HEIGHT/3):
                self.state_part = 5
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 5:
            if self.__go_to_point__(3*self.WIN_WIDTH/4,
                                    2*self.WIN_HEIGHT/3):
                self.state_part = 6
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 6:
            if self.__go_to_point__(2*self.WIN_WIDTH/4,
                                    self.WIN_HEIGHT/3):
                self.state_part = 7
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 7:
            if self.__go_to_point__(self.WIN_WIDTH/4,
                                    2*self.WIN_HEIGHT/3):
                self.state_part = 8
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 8:
            if self.__go_to_point__(INDENTION,
                                    self.WIN_HEIGHT/3):
                self.state_part = 0
                self.xvel = 0
                self.yvel = 0
                self.state_moving += 1


    def __circle__(self):
        #x:=R * cos(pi * i / 4)
        #y:=R * sin(pi * i / 4)
        #i = 1..8
        R = (self.WIN_HEIGHT - hero.HEIGHT - INDENTION)/2
        dy = R
        dx = (self.WIN_WIDTH - hero.WIDTH)/2

        if self.state_part == 0:
            if self.__go_to_point__(R * math.cos(math.pi * (self.state_part + 6) / 4) + dx,
                                    R * math.sin(math.pi * (self.state_part + 6) / 4) + dy):
                self.state_part = 1
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 1:
            if self.__go_to_point__(R * math.cos(math.pi * (self.state_part + 6) / 4) + dx,
                                    R * math.sin(math.pi * (self.state_part + 6) / 4) + dy):
                self.state_part = 2
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 2:
            if self.__go_to_point__(R * math.cos(math.pi * (self.state_part + 6) / 4) + dx,
                                    R * math.sin(math.pi * (self.state_part + 6) / 4) + dy):
                self.state_part = 3
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 3:
            if self.__go_to_point__(R * math.cos(math.pi * (self.state_part + 6) / 4) + dx,
                                    R * math.sin(math.pi * (self.state_part + 6) / 4) + dy):
                self.state_part = 4
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 4:
            if self.__go_to_point__(R * math.cos(math.pi * (self.state_part + 6) / 4) + dx,
                                    R * math.sin(math.pi * (self.state_part + 6) / 4) + dy):
                self.state_part = 5
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 5:
            if self.__go_to_point__(R * math.cos(math.pi * (self.state_part + 6) / 4) + dx,
                                    R * math.sin(math.pi * (self.state_part + 6) / 4) + dy):
                self.state_part = 6
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 6:
            if self.__go_to_point__(R * math.cos(math.pi * (self.state_part + 6) / 4) + dx,
                                    R * math.sin(math.pi * (self.state_part + 6) / 4) + dy):
                self.state_part = 7
                self.xvel = 0
                self.yvel = 0

        if self.state_part == 7:
            if self.__go_to_point__(R * math.cos(math.pi * (self.state_part + 6) / 4) + dx,
                                    R * math.sin(math.pi * (self.state_part + 6) / 4) + dy):
                self.state_part = 0
                self.xvel = 0
                self.yvel = 0
                self.state_moving += 1




