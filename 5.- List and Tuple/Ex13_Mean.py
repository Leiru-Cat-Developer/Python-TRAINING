# Write a program that asks for a sample of numbers, separated by commas, saves them in a list, # and displays their mean and standard deviation on the screen.

print("")
sample = input("Write numbers separated by commas: ")
sample = sample.split(",")

for i in range(len(sample)):
    sample[i] = int(sample[i])

sum = 0.0
des = 0.0

for i in range(len(sample)):
    sum += sample[i]
    des += sample[i] ** 2

total_sum = sum/len(sample)
total_dev = (des/len(sample) - total_sum ** 2) ** (1/2)

print(f"Sum: {total_sum} and Des: {total_dev}")