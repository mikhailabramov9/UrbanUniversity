name1 = int(input('введите первое число: '))
name2 = int(input('введите второе число: '))
name3 = int(input('введите третье число: '))
if name1==name2==name3:
    print(3)
elif name1==name2 or name1==name3 or name2==name3:
    print(2)
else:
    print(0)
print('завершено')