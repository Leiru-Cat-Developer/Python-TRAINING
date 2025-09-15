# Write a function which receives a number and returns it's factorial

def calculation(number):
    """FACTORIAL"""
    total = number
    if number == 1 or number == 0:
        print("FACTORIAL OF " + str(number) + " IS 1")
    else:
        if number > 0:
            for i in range(number,1,-1):
                total *= i-1  
        if number < 0:
            number *= -1
            total = number
            for i in range(number,1,-1):
                total *= i-1  
            total *= -1
        print("\nFACTORIAL OF " + str(number) + " IS " + str(total))
    return

number = int(input("\nWRITE A NUMBER \n -> "))

calculation(number)