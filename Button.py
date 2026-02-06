import pygame
class Button(pygame.Rect):
     def __init__(self, x, y, width, height,
                  color=(255, 255, 255),
                  func=lambda: print('call'),
                  text='',
                  text_color=(0, 0, 0)):
          super().__init__(x, y, width, height)
          self.color = color
          self.func = func
          self.x = x
          self.y = y
          self.width = width
          self.height = height
          self.text = text
          self.text_color = text_color
          self.default_color = color
          self.default_text_color = text_color
          self.__font = pygame.font.SysFont("None", 32)

     def draw(self, surface):
          pygame.draw.rect(surface, self.color, self)
          surface.blit(self.__font.render(self.text, True, self.text_color),
                       [self.x + 5, self.y + 5])

     def colision(self, x, y, mode=0):
          # mode 0 passive
          # mode 1 hover
          # mode 2 active
          if self.x <= x <= self.x + self.width \
               and self.y <= y <= self.y + self.height:
               if mode == 1:
                    self.color = (max(0, self.default_color[0] - 50), max(0, self.default_color[1] - 50), max(0, self.default_color[2] - 50))
                    print(self.color)
               elif mode == 2:
                    self.func()
                    self.text_color, self.color = self.color, self.text_color
               return True
          else:
               self.color = self.default_color
               self.text_color = self.default_text_color
               return False


