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

# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h3 = House('ЖК Эльбрус', 30)
# h1.go_to(5)
# h2.go_to(10)
# h3.go_to(9)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


#__str__
print(h1)
print(h2)
# print(h3)

# __len__
print(len(h1))
print(len(h2))
# print(len(h3))