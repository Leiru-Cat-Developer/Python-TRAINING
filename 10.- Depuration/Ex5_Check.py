# Check the next code and fix it

a = ((1, 2, 3),
     (3, 2, 1))
b = ((1, 2),
     (3, 4),
     (5, 6))

def multiplication(a, b):
    product = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(a[0])):
                sum += a[i][k] * b[k][j]
            row.append(sum)
        product.append(tuple(row))
    return tuple(product)

print(multiplication(a, b))