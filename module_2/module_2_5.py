def get_matrix(n,m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

res1 = get_matrix(4,6,9)
print(res1)
res2 = get_matrix(3,5,7)
print(res2)
res3 = get_matrix(2,3,8)
print(res3)