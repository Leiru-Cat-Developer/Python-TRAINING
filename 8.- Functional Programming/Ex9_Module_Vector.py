# Write a function to calculate the module vector

import math

def vector(x: int, y: int) -> float:
    return math.sqrt(math.pow(x,2) + math.pow(y,2))

x = int(input("\nWrite the value of x: "))
y = int(input("Write the value of y: "))

print(f"\nThe module vector is {vector(x,y):.2f}")