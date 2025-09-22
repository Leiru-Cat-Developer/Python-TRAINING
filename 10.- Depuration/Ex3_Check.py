# Check the next code and fix it

u = [1, 2, 3]
v = [4, 5, 6]

def scalar(u, v):
    for i in range(len(u)):
        u[i] *= v[i]
    return sum(u)

print(scalar(u, v))