# Show the following phone number without prefix and extension
# Input: +52-5566556655-52
# PREFIX = 2 numbers
# EXTENSION = 2 numbers
# REST = 10 numbers
# Output: 5566556655

natural_phone_number = input("Enter the phone number: ")
phone_number = natural_phone_number[4:-3]
print("The phone number is:", phone_number)