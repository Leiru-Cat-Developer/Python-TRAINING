# Create a function that receives a number and calculate
# how many characters does the number has using simple
# operations

def length(number: int):
    count = 0
    
    while number > 0:
        number //= 10
        count += 1

    return count

number = int(input("\nWrite a number: "))
print(f"\nLength number: {length(number)} digit(s)")