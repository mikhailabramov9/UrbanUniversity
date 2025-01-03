class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            Animal.fed = True
            print(f"{self.name} съел {food.name}")
        if not food.edible:
            Animal.alive = False
            print(f"{self.name} не стал есть {food.name}")

class Plant:
    edible = False #(съедобность)

    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True


#Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
#Вывод на консоль:
#Волк с Уолл-Стрит
#Цветик семицветик
#True
#False
#Волк с Уолл-Стрит не стал есть Цветик семицветик
#Хатико съел Заводной апельсин
#False
#True