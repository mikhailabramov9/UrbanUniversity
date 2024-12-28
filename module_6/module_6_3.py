import random


class Animal:
    #Класс обладает следующими атрибутами:
    live = True
    sound = None # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0  # степень опасности существа

    def __init__(self, speed):
        self._cords = [0, 0, 0] # координаты в пространстве.
        self.speed = speed # скорость передвижения существа (определяется при создании объекта)

    def move(self, dx, dy, dz):
        self._cords[0] = int(dx) * int(self.speed)
        self._cords[1] = int(dy) * int(self.speed)
        if dz < 0:
            print("It's too deep, i can't dive :(" )
        else:
            self._cords[2]= int(dz) * int(self.speed)

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if  self._DEGREE_OF_DANGER < 5:
            print( "Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(f"{self.sound}")


class Bird(Animal):
    beak = True
    eggs_list = [1,2,3,4]
    egg = random.choice(eggs_list)

    def lay_eggs(self):
        print(f"Here are(is) {self.egg} eggs for you")

class AquaticAnimal(Animal): # класс описывающий плавающего животного
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = int(dz) - int(self.speed)/2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal ):
    sound = "Click-click-click"

#print(Duckbill.mro())

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()