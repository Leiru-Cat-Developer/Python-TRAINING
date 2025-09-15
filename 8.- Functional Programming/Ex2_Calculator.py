# Write a function that simulates a scientific calculator that allows calculate
# sen, cos, tan, exp and log nep. The function will ask to the user the value
# and the function to apply, and will display a table with int's from 1 to
# the introduced value and the value of the function for each of those int's

import cmath

def calculator(value,function):
    """
        Simulates a scientific calculator
            -> value (int)
            -> function (str)
    """
    if number <= 0:
        return
    if function == "sen":
        for i in range(1,value+1,1):
            print(f"{i}: {cmath.sin(i):.4f}")
        return
    if function == "cos":
        for i in range(1,value+1,1):
            print(f"{i}: {cmath.cos(i):.4f}")
        return
    if function == "tan":
        for i in range(1,value+1,1):
            print(f"{i}: {cmath.tan(i):.4f}")
        return
    if function == "exp":
        for i in range(1,value+1,1):
            print(f"{i}: {cmath.exp(i):.4f}")
        return
    if function == "log":
        for i in range(1,value+1,1):
            print(f"{i}: {cmath.log(i):.4f}")
        return
    
number = int(input("\nWrite a number \n -> "))
function = input("\nWrite the function you want to apply \n -> ")

print(f"\nThe values for the {function} function are: \n")
calculator(number,function)