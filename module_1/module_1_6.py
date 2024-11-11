# словарь
my_dict = {"Mikhail" : 1983 , "Olga" : 1983 , "Svetlana" : 1960}
print(my_dict)
print(my_dict["Olga"])
print(my_dict.get("Dima"))
my_dict["Konstantin"] = 1960
my_dict["Evgeniy"] = 1930
print(my_dict)
print(my_dict["Mikhail"])
my_dict.pop("Mikhail")
print(my_dict)

# множества
my_set = {1,2,3,4,5,6,7,"mama", "papa" , 7, 3,2,5, "papa"}
print(my_set)
my_set.add("sister")
my_set.add("brother")
print(my_set)
my_set.remove(7)
print((my_set))