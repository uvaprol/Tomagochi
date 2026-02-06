import pygame
from Button import Button
pygame.init()
display = pygame.display.set_mode((560, 400))


# создание кнопок
hp_btn =     Button(10,  340, 100, 50, text='Лечить',  func=lambda: print('Лечить'))
potion_btn = Button(120, 340, 100, 50, text='Спать',   func=lambda: print('Спать'))
happy_btn =  Button(230, 340, 100, 50, text='Играть',  func=lambda: print('Играть'))
poo_btn =    Button(340, 340, 100, 50, text='Помыть',  func=lambda: print('Помыть'))
hungry_btn = Button(450, 340, 100, 50, text='Кормить', func=lambda: print('Кормить'))

# рисуем кнопки
def render():
     display.fill((100, 100, 100))
     hp_btn.draw(display)
     potion_btn.draw(display)
     happy_btn.draw(display)
     poo_btn.draw(display)
     hungry_btn.draw(display)
     pygame.display.flip()

while True:
     render()
     for e in pygame.event.get():
          hp_btn.colision(*pygame.mouse.get_pos(), mode=1)
          potion_btn.colision(*pygame.mouse.get_pos(), mode=1)
          happy_btn.colision(*pygame.mouse.get_pos(), mode=1)
          poo_btn.colision(*pygame.mouse.get_pos(), mode=1)
          hungry_btn.colision(*pygame.mouse.get_pos(), mode=1)
          if e.type == pygame.MOUSEBUTTONDOWN:
               # проверяем нажатие кнопки
               hp_btn.colision(*pygame.mouse.get_pos(), mode=2)
               potion_btn.colision(*pygame.mouse.get_pos(), mode=2)
               happy_btn.colision(*pygame.mouse.get_pos(), mode=2)
               poo_btn.colision(*pygame.mouse.get_pos(), mode=2)
               hungry_btn.colision(*pygame.mouse.get_pos(), mode=2)
