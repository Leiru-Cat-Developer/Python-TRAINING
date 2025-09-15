# Write a function that receives a numbers sample and display
# the average

def average(numbers):
    """CALCULATES AVERAGE OF A LIST ON NUMBERS"""
    count = 0
    total = 0
    for i in numbers:
        count += 1
        total += i
    return total / count

numbers = [2.3, 5.7, 6.8, 9.7, 12.1, 15.6]

print("\nThe average is: " + str(average(numbers)))