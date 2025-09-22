# Check the next code and fix it

def apply_tax(base: float, tax = 21) -> float:
    base *= tax   
    return base

base = float(input('Write the base: '))
print(apply_tax(base))