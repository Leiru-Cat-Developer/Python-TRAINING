# Write a function receives a sample of numbers and returns
# another with square numbers

def square(numbers):
    """RETURNS A LIST OF SQUARE NUMBERS"""
    square = []
    for i in numbers:
        square.append(i ** 2)
    return square


sample = [1,2,3,4,5,6,7,8,9,10]

print("\nList of square numbers: " + str(square(sample)))