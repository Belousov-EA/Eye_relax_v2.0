#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
from pygame import*
import time
import colors

WIDTH = 150
HEIGHT = 152
COLOR =  "#888888"

ANIMATION_RIGHT = [
    "Дракончик/frame-1.png",
    "Дракончик/frame-2.png",
    "Дракончик/frame-3.png",
    "Дракончик/frame-4.png",
    "Дракончик/frame-5.png",
    "Дракончик/frame-6.png",
    "Дракончик/frame-7.png",
    "Дракончик/frame-8.png"
]

ANIMATION_LEFT = [
    "Дракончик/frame-1l.png",
    "Дракончик/frame-2l.png",
    "Дракончик/frame-3l.png",
    "Дракончик/frame-4l.png",
    "Дракончик/frame-5l.png",
    "Дракончик/frame-6l.png",
    "Дракончик/frame-7l.png",
    "Дракончик/frame-8l.png"
]

ANIMATION_DELAY = 0.1


class Hero(sprite.Sprite):
    def __init__(self, x = 10, y = 10):
        sprite.Sprite.__init__(self)
        self.image = Surface((WIDTH,HEIGHT))
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
        self.rect.x = x
        self.rect.y = y
        self.pred_x = x
        self.pred_y = y
        self.cadr = 0
        self.anim_right = []
        self.anim_left = []
        self.last_time = time.time()
        for cadr in ANIMATION_RIGHT:
            self.anim_right.append(pygame.image.load(cadr))
        for cadr in ANIMATION_LEFT:
            self.anim_left.append(pygame.image.load(cadr))
        self.pred_napr = True


    def draw(self, screen, x, y):  # Выводим себя на экран
        self.rect.x = int(x)
        self.rect.y = int(y)
        if(time.time() - self.last_time > ANIMATION_DELAY):
            self.last_time = time.time()
            self.cadr+=1
        if(self.cadr > len(self.anim_right) - 1):
            self.cadr = 0
        if(self.rect.x > self.pred_x):
            screen.blit(self.anim_right[self.cadr], (self.rect.x, self.rect.y))
            self.pred_napr = True
        elif(self.rect.x < self.pred_x):
            screen.blit(self.anim_left[self.cadr], (self.rect.x, self.rect.y))
            self.pred_napr = False
        elif(self.rect.x == self.pred_x):
            if(self.pred_napr == True):
                screen.blit(self.anim_right[self.cadr], (self.rect.x, self.rect.y))
            else:
                screen.blit(self.anim_left[self.cadr], (self.rect.x, self.rect.y))
        self.pred_x = self.rect.x
        self.pred_y = self.rect.y


