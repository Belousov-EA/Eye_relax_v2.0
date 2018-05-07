#!/usr/bin/env python
# -*- coding: utf-8 -*-

import game
from game import*
import pygame
from menu import Menu
from pygame import *
import text_blok_object
from texts import *
from colors import*
import message
import time




class LazyGame(game.Game):
    def __init__(self, screen, bg, list_mooving):
        Game.__init__(self, list_mooving, screen)
        self.bg = bg
        self.text_finish = text_blok_object.TextBlockObject(200, 200, Texts.LAZY_GAME_FINISH,\
                                                     MainColors.White, "font.ttf", 70, 50)
        self.text_success_finish = text_blok_object.TextBlockObject(200, 200,Texts.LAZY_GAME_SUCCESS_FINISH,
                                                                    MainColors.White, "font.ttf", 70, 50)
        self.text_greeting = text_blok_object.TextBlockObject(100, 200, Texts.LAZY_GAME_GREETING,
                                                              MainColors.White, "font.ttf", 70, 50)


    def game(self):
        mes = message.Message(MainColors.Blue, self.text_finish, self.bg, self.screen)
        puncts = [(self.WIN_WIDTH / 3, 200, u'Продолжить', MainColors.White, MainColors.Black, 0),
                  (self.WIN_WIDTH / 3, 450, u'Начать заново', MainColors.White, MainColors.Black, 1),
                  (self.WIN_WIDTH / 3, 700, u'Выйти в главное меню', MainColors.White, MainColors.Black, 2)]
        menu = Menu(self.screen, self.bg, 100, "font.ttf", puncts, MainColors.Blue)
        clock = pygame.time.Clock()
        self.start_game()
        self.last_time = time.time()
        while self.game_loop:
            self.bg.fill(MainColors.Green)  # Заливаем поверхность сплошным цветом
            self.screen.blit(self.bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
            self.move(cond=self.condition, succesful_finish=self.success_finish)
            pygame.display.update()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    raise SystemExit, "QUIT"
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        menu.menu()
                        self.last_time = time.time()
            if(menu.state == 2):
                self.game_loop = False
                mes.message()
            if(menu.state == 1):
                self.start_game()
                self.last_time = time.time()
                menu.state = 0
            clock.tick(60)
        #по окончанию игры


    def message(self, color, mes):
        is_finish = True
        while is_finish:
            self.bg.fill(color)
            self.screen.blit(self.bg, (0, 0))
            mes.draw(self.screen)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    raise SystemExit, "QUIT"
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        is_finish = False
                    if e.key == pygame.K_ESCAPE:
                        is_finish = False
            pygame.display.update()


    def success_finish(self):
        mes = message.Message(MainColors.Blue, self.text_success_finish, self.bg, self.screen)
        mes.message()



    def start_game(self):
        self.is_finish = True
        self.x = 10
        self.y = 10
        self.state_moving = 0
        self.state_part = 0
        mes = message.Message(MainColors.Blue, self.text_greeting, self.bg, self.screen)
        mes.message()

    def condition(self):
        return True

