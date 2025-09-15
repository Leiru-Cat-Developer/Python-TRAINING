# Create two functions to calculate LCM and GCD

def lcm(num1,num2):
    """
        LEAST COMMON MULTIPLE
    """
    result = 1
    init = 2
    while True:
        if num1 % init == 0 or num2 % init == 0:
            result *= init
            if num1 % init == 0:
                num1 /= init
            if num2 % init == 0:
                num2 /= init
            init = 2
        else:
            init += 1
        if num1 == 1 and num2 == 1:
            break
    return result

def gcd(num1,num2):
    """
        GREATEST COMMON MULTIPLE
    """
    rest = 0
    while(num2 > 0):
        rest = num2
        num2 = num1 % num2
        num1 = rest
    return num1

num1 = int(input("\nWrite the first number: "))
num2 = int(input("Write the second number: "))

print(f"\nLCM: {lcm(num1,num2)}, GCM: {gcd(num1,num2)}")