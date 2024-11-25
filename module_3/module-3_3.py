def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(2, "функция", False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, "строка", True]
values_dict = {"a" : 999, "b" : 47 , "c" : [1,2,3,4,5]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["help", 23]
print_params(values_list_2)
print_params(*values_list_2, 42)