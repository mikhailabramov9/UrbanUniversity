print("Слишком Древний Шифр")
import random
num1 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a = random.choice(num1)
print("Напишите неповторяющиеся пары чисел друг за другом,")
print("так чтобы Число: ", a, "было кратно сумме их значений.")
code = []
for i in range(1, a):
    for j in range(2, a):
        if a % (i + j) == 0 and i != j and i < a // 2 + 1:
            code.extend([i, j])
        j += 1
    i += 1

print("Шифр: ", ' '.join(map(str, code))) # пробел для лучшего считывания пары чисел
