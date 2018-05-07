import text_blok_object
import pygame


class Message:
    def __init__(self, color, mes, bg, screen):
        self.color = color
        self.mes = mes
        self.bg = bg
        self.screen = screen

    def message(self):
        is_finish = True
        while is_finish:
            self.bg.fill(self.color)
            self.screen.blit(self.bg, (0, 0))
            self.mes.draw(self.screen)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    raise SystemExit, "QUIT"
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        is_finish = False
                    if e.key == pygame.K_ESCAPE:
                        is_finish = False
            pygame.display.update()