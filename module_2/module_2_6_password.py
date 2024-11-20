print("Слишком Древний Шифр")
import random
num1 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a = random.choice(num1)
print("Напишите неповторяющиеся пары чисел друг за другом, ")
print("так чтобы Число: ", a, "было кратно сумме их значений.")
code = []
for i in range(1, a):
    for j in range(1, a):
        if a % (i + j) == 0 and i != j and i < j:
            code.extend([i, j])
        j += 1
    i += 1
code_int = int(''.join(map(str, code))) # преобразовал в число для сверки с ответами
print("Шифр: ", code_int)

# Ответы:
n3 = 12
n4 = 13
n5 = 1423
n6 = 121524
n7 = 162534
n8 = 13172635
n9 = 1218273645
n10 = 141923283746
n11 = 11029384756
n12 = 12131511124210394857
n13 = 112211310495867
n14 = 1611325212343114105968
n15 = 1214114232133124115106978
n16 = 1317115262143531341251161079
n17 = 11621531441351261171089
n18 = 12151811724272163631545414513612711810
n19 = 118217316415514613712811910
n20 = 13141911923282183731746416515614713812911

# Проверка:
correct = False
if n3 == code_int or n4 == code_int or n4 == code_int or n5 == code_int or n6 == code_int or n7 == code_int or \
        n8 == code_int or n9 == code_int or n9 == code_int or n10 == code_int or n11 == code_int or n12 == code_int or \
        n13 == code_int or n14 == code_int or n15 == code_int or n16 == code_int or n17 == code_int or \
        n18 == code_int or n19 == code_int or n20 == code_int:
    correct = True
print(correct)