# Display numbers 1-10 inverted separated by commas

print("")
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.reverse()
for i in range(0,10):
    print(numbers[i],end=", ")
print("")