# toma_game
import pygame
from Button import Button
from Tomagochi import Tomagochi
from datetime import datetime

GRAY = (155, 155, 155)
W = 540
H = 400

pygame.init()
DIS = pygame.display.set_mode((W, H))
pygame.display.set_caption('Томагочи')

TOMA = Tomagochi()
VIBE_BTN = Button(10, 310, 90, 45, text='Играть', func=lambda: TOMA.pogladit())
FOOD_BTN = Button(110, 310, 120, 45, text='Покормить', func=lambda: TOMA.dat_poest())
HEAL_BTN = Button(240, 310, 90, 45, text='Лечить', func=lambda: TOMA.polechit())
CLEAN_BTN = Button(340, 310, 90, 45, text='Чистить', func=lambda: TOMA.pochistit())
SLEEP_BTN = Button(440, 310, 90, 45, text='Спать', func=lambda: TOMA.polozit_spat())


def render():
    DIS.fill(GRAY)
    DIS.blit(TOMA.get_face(), (0, 0))
    VIBE_BTN.draw(DIS)
    FOOD_BTN.draw(DIS)
    HEAL_BTN.draw(DIS)
    CLEAN_BTN.draw(DIS)
    SLEEP_BTN.draw(DIS)

    pygame.display.flip()

if __name__ == '__main__':
    time_point = datetime.now()
    while True:
        if (datetime.now() - time_point).total_seconds() >= 10:
            TOMA.action()
            time_point = datetime.now()
        render()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                VIBE_BTN.get_collision(*pygame.mouse.get_pos(), pressed=True)
                FOOD_BTN.get_collision(*pygame.mouse.get_pos(), pressed=True)
                HEAL_BTN.get_collision(*pygame.mouse.get_pos(), pressed=True)
                CLEAN_BTN.get_collision(*pygame.mouse.get_pos(), pressed=True)
                SLEEP_BTN.get_collision(*pygame.mouse.get_pos(), pressed=True)
            elif e.type == pygame.MOUSEBUTTONUP:
                VIBE_BTN.get_collision(*pygame.mouse.get_pos(), realised=True)
                FOOD_BTN.get_collision(*pygame.mouse.get_pos(), realised=True)
                HEAL_BTN.get_collision(*pygame.mouse.get_pos(), realised=True)
                CLEAN_BTN.get_collision(*pygame.mouse.get_pos(), realised=True)
                SLEEP_BTN.get_collision(*pygame.mouse.get_pos(), realised=True)
            else:
                VIBE_BTN.get_collision(*pygame.mouse.get_pos())
                FOOD_BTN.get_collision(*pygame.mouse.get_pos())
                HEAL_BTN.get_collision(*pygame.mouse.get_pos())
                CLEAN_BTN.get_collision(*pygame.mouse.get_pos())
                SLEEP_BTN.get_collision(*pygame.mouse.get_pos())



