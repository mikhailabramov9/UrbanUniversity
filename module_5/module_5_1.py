class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        number = int(new_floor)
        if number > self.number_of_floors or number < 1:
            print("Такого этажа не существует")
        else:
            for i in range (1, (number +1)):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        isinstance(other, int)
        return self.number_of_floors == other

#Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=)
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

#__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

#__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
    def __iadd__(self, value):
        self.number_of_floors += value
        return self
    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return self




# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h3 = House('ЖК Эльбрус', 30)
# h1.go_to(5)
# h2.go_to(10)
# h3.go_to(9)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

#__str__
# print(h1)
# print(h2)

# # __len__
# print(len(h1))
# print(len(h2))


print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__