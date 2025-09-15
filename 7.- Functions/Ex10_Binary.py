# Write a function that converts a decimal into binary
# and another that does the contrary

def binary(num):
    result = []
    quotient = 1
    residue = 1
    while quotient != 0:
        quotient = num // 2 
        residue = num % 2
        result.append(residue)
        num //= 2
    result.reverse()
    return result

def decimal(num):
    num = list(num)
    num.reverse()
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i]) * 2 ** i
    return decimal

option = int(input("\nChoice an option\n" + 
                    "\t1. Binary\n" +
                    "\t2. Decimal\n" +
                    "-> "))

if option == 1:
    number = int(input("\nWrite the decimal number: "))
    print(f"\nThe binary number will be: {binary(number)}")

if option == 2:
    number = input("\nWrite the binary number: ")
    print(f"\nThe decimal number will be: {decimal(number)}")