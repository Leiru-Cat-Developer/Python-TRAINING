# Ask for 'n' lottery numbers and display them order asc [minor to major]

print("")
n = int(input("How many lottery numbers do you want?: "))
print("")

lotteryNumbers = []

for i in range(n):
    number = int(input(f"Write the lottery number {i+1}: "))
    lotteryNumbers.append(number)
print("")

print("Numbers are as follows: \n")
lotteryNumbers.sort()
print(lotteryNumbers)