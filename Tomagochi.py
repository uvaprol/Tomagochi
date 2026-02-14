from random import randint, choice, shuffle
import pygame
class Tomagochi():
      __golod = 100
      __hp = 100
      __vibe = 100
      __energy = 100
      __poo = False
      __face = {
            'happy': 'cat/happy.png',
            'sad': 'cat/sad.png',
            'hungry': 'cat/hungry.png',
            'sick': 'cat/sick.png',
            'sleepy': 'cat/sleepy.png',
            'dirty': 'cat/dirty.png',
      }
      def __init__(self):
            self.__action()

      def get_face(self):
            face = 'happy'
            if self.__vibe >= 80:
                  face = 'happy'
            else:
                  face = 'sad'
            if self.__golod <= 50:
                  face = 'hungry'
            if self.__poo:
                  face = 'dirty'
            if self.__energy <= 30:
                  face = 'sleepy'
            return pygame.image.load(self.__face[face])

      def dat_poest(self):
            self.__golod += 10
            self.__action()
      def polechit(self):
            self.__hp += 10
            self.__action()
      def pogladit(self):
            self.__vibe += 10
            self.__action()
      def polozit_spat(self):
            self.__energy = 100
            self.__action()
      def pochistit(self):
            self.__poo = False
            self.__action()
      def __action(self):
            action = randint(0, 5)
            if action == 0:
                  self.__golod -= 20
            elif action == 1:
                  self.__hp -= 20
            elif action == 2:
                  self.__vibe -= 20
            elif action == 3:
                  self.__energy -= 20
            elif action == 4:
                  self.__poo = True
      def get_stat(self):
            print(f'Голод     : {self.__golod}')
            print(f'Здоровье  : {self.__hp}')
            print(f'Настроение: {self.__vibe}')
            print(f'Силы      : {self.__energy}')
            print(f'Чистота   : {"грязный" if self.__poo else "чистый"}')

if __name__ == '__main__':
      toma = Tomagochi()
      ACTION_LIST = {
            'покормить': toma.dat_poest,
            'полечить': toma.polechit,
            'погладить': toma.pogladit,
            'уложитьспать': toma.polozit_spat,
            'почистить': toma.pochistit
      }
      while True:
            toma.get_stat()
            print('----------------------------\n\n\n')
            action = input('Что вы хотите сделать:\nПокормить?\nПолечить?\nПогладить?\nУложить спать?\nПочистить?\n:\t')
            action = action.lower()
            action = action.strip()
            action = action.replace(' ', '')
            action = action.replace('_', '')
            if ACTION_LIST.get(action):
                  ACTION_LIST[action]()
            else:
                  print(f'{action}: такой команды не существует')
            print('----------------------------\n\n\n')
