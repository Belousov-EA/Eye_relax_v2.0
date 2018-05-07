#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame


class TextBlockObject:
    def __init__(self,
                 x,
                 y,
                 text_list,
                 color,
                 font_name,
                 font_size,
                 line_spacing):
        self.pos = (x, y)
        self.text_list = text_list
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.line_spacing = line_spacing
        #self.bounds = self.get_surface(text_func())

    def draw(self, surface, centralized=False):
        delta = 0
        for text in self.text_list:
            text_surface, self.bounds = self.get_surface(text)
            if centralized:
                pos = (self.pos[0] - self.bounds.width // 2,
                       self.pos[1] + delta)
            else:
                pos = (self.pos[0],
                       self.pos[1] + delta)
            surface.blit(text_surface, pos)
            delta += self.line_spacing


    def get_surface(self, text):
        text_surface = self.font.render(text,
                                        False,
                                        self.color)
        return text_surface, text_surface.get_rect()
