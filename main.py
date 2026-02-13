import pygame
from Button import Button
from Tomagochi import *
pygame.init()
display = pygame.display.set_mode((560, 400))

toma = Cat('Bars')

# создание кнопок
hp_btn =     Button(10,  340, 100, 50, text='Лечить',  func=lambda: print('Лечить'))
potion_btn = Button(120, 340, 100, 50, text='Спать',   func=lambda: print('Спать'))
happy_btn =  Button(230, 340, 100, 50, text='Играть',  func=lambda: print('Играть'))
poo_btn =    Button(340, 340, 100, 50, text='Помыть',  func=lambda: print('Помыть'))
hungry_btn = Button(450, 340, 100, 50, text='Кормить', func=lambda: print('Кормить'))

# рисуем кнопки
def render():
     display.fill((100, 100, 100))
     display.blit(toma.get_face(), (0, 0))
     hp_btn.draw(display)
     potion_btn.draw(display)
     happy_btn.draw(display)
     poo_btn.draw(display)
     hungry_btn.draw(display)
     pygame.display.flip()

while True:
     render()
     for e in pygame.event.get():
          if e.type == pygame.QUIT:
               pygame.quit()
               quit()
          if e.type == pygame.MOUSEBUTTONDOWN:
               hp_btn.colision(*pygame.mouse.get_pos(), on_press=True)
               potion_btn.colision(*pygame.mouse.get_pos(), on_press=True)
               happy_btn.colision(*pygame.mouse.get_pos(), on_press=True)
               poo_btn.colision(*pygame.mouse.get_pos(), on_press=True)
               hungry_btn.colision(*pygame.mouse.get_pos(), on_press=True)
          elif e.type == pygame.MOUSEBUTTONUP:
               hp_btn.colision(*pygame.mouse.get_pos(), realise=True)
               potion_btn.colision(*pygame.mouse.get_pos(), realise=True)
               happy_btn.colision(*pygame.mouse.get_pos(), realise=True)
               poo_btn.colision(*pygame.mouse.get_pos(), realise=True)
               hungry_btn.colision(*pygame.mouse.get_pos(), realise=True)
          else:
               hp_btn.colision(*pygame.mouse.get_pos())
               potion_btn.colision(*pygame.mouse.get_pos())
               happy_btn.colision(*pygame.mouse.get_pos())
               poo_btn.colision(*pygame.mouse.get_pos())
               hungry_btn.colision(*pygame.mouse.get_pos())

