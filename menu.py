#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys




class Menu:
    def __init__(self, window, screen,font_size,font_name, \
                 punkts=[120, 140, u'Game', (250, 250, 30), (250, 30, 250), 0], color = (0, 100, 200)):
        self.punkts = punkts
        self.window = window
        self.screen = screen
        self.font_size = font_size
        self.state = 0
        self.font_name = font_name
        self.color = color

    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1] ))
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1] ))

    def menu(self):
        done = True
        pygame.mouse.set_visible(True)
        pygame.key.set_repeat(0, 0)
        font_menu = pygame.font.Font(self.font_name, self.font_size)
        punkt = 0
        while done:
            self.screen.fill(self.color)

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + self.font_size * len(i[2])\
                        and mp[1] > i[1] and mp[1] < i[1] + self.font_size:
                    punkt = i[5]
            self.render(self.screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                       self.state = punkt
                       done = False
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    self.state = punkt
                    done = False

            self.window.blit(self.screen, (0, 0))
            pygame.display.update()
