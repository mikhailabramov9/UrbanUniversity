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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 30)
h1.go_to(5)
h2.go_to(10)
h3.go_to(9)