from random import randint as rd

class Tomagochi():
    __hp = 100
    __potion = 0
    __hapy = 100
    __poo = False
    __hungry = 0

    def __init__(self, name, type='cat'):
        self.__name = name
        self.__type = type

    def give_food(self):
        self.__hungry += 10

    def healing(self):
        self.__hp = 100 if self.__hp + 10 >= 100 else self.__hp + 10

    def cleaning(self):
        self.__poo = False

    def give_treatment(self):
        self.__potion = 0 if self.__potion - 10 <= 0 else self.__potion - 10

    def play(self):
        self.__hapy = 100 if self.__hapy + 10 >= 100 else self.__hapy + 10

    def get_event(self):
        event = rd(0, 5)
        match event:
            case 1:
                self.__hp -= rd(5, 20)
            case 2:
                self.__potion -= rd(5, 20)
            case 3:
                self.__hapy -= rd(5, 20)
            case 4:
                self.__poo = True
            case 5:
                self.__hungry -= rd(5, 20)
            case _:
                print('pass event')

    def get_status(self):
        return self.__hp, \
               self.__potion, \
               self.__hapy, \
               self.__poo, \
               self.__hungry

class Cat(Tomagochi):
    __face: str
