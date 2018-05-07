#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import*
import standart_game
import lazy_game
from menu import Menu
from colors import MainColors
import sys
import face_detection_game



WIN_WIDTH_D = 800
WIN_HEIGHT_D = 600
DISPLAY = (WIN_WIDTH_D, WIN_HEIGHT_D)


LIST_MOOVING = [ "square", "eight", "down-up", "x-moving",
                 "left-right", "zigzag", "circle", "second eight" ]




def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    #set icon:
    icon_screen = pygame.image.load("icon/eye.ico")
    pygame.display.set_icon(icon_screen)


    #screen = pygame.display.set_mode((1000, 500))
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)  # Создаем окошко
    WIN_WIDTH = screen.get_width()
    WIN_HEIGHT = screen.get_height()
    pygame.display.set_caption("Eye_relax_v2.0")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    s_game = standart_game.StandartGame(screen, bg, LIST_MOOVING)
    l_game = lazy_game.LazyGame(screen, bg, LIST_MOOVING)
    fd_game = face_detection_game.FaceDetectionGame(screen,bg, LIST_MOOVING)

    puncts = [
        (WIN_WIDTH / 3, 200, u'Обычная игра', MainColors.White, MainColors.Black, 0),
        (WIN_WIDTH / 3, 350, u'Простая игра', MainColors.White, MainColors.Black, 1),
        (WIN_WIDTH / 3, 500, u'Face режим', MainColors.White, MainColors.Black, 2),
        (WIN_WIDTH / 3, 650, u'Выйти из игры', MainColors.White, MainColors.Black, 3)

    ]
    menu = Menu(screen, bg, 100, "font.ttf", puncts, MainColors.Blue)
    game_loop = True

    while game_loop:
        menu.menu()
        if(menu.state == 0):
            s_game.game()
        if(menu.state == 1):
            l_game.game()
        if(menu.state == 2):
            fd_game.game()
        if(menu.state == 3):
            game_loop = False

    sys.exit()








if __name__ == '__main__':
    main()