# Button
import pygame
class Button(pygame.Rect):
    def __init__(self,
                 x: int,
                 y: int,
                 w: int,
                 h: int,
                 color: tuple = (255, 255, 255),
                 func=lambda: print('call'),
                 text: str = '',
                 text_color: tuple = (0, 0, 0)):
        super().__init__(x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.func = func
        self.text = text
        self.text_color = text_color
        self.active_status = False
        self.default_color = color
        self.default_text_color = text_color
        self.font = pygame.font.SysFont('None', 32)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self)
        surface.blit(self.font.render(self.text, True, self.text_color), [self.x, self.y])

    def get_collision(self, x, y, pressed=False, realised=False):
        if self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h:
            if pressed:
                self.active_status = True
            if realised:
                self.active_status = False
            if self.active_status:
                self.func()
                self.text_color, self.color = self.default_color, self.default_text_color
            else:
                self.color = (max(0, self.default_color[0] - 50),
                              max(0, self.default_color[1] - 50),
                              max(0, self.default_color[2] - 50))
            return True
        else:
            self.active_status = False
            self.color = self.default_color
            self.text_color = self.default_text_color
            return False
