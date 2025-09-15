# Ask for whole positive number and calculate the sum of all numbers from 1 to the number
number = int(input("Please enter a whole positive number: "))
sum_of_numbers = number * (number + 1) / 2
print(f"The sum of all numbers from 1 to {number} is: {sum_of_numbers}")