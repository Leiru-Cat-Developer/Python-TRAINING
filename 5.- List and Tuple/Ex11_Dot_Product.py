# Save the next values: (1,2,3) and (-1,0,2)
# Display the dot product A*B = (A1 * B1) + (A2 * B2) + (AN * AN)

print("")
array1 = [1,2,3]
array2 = [-1,0,2]

sum = 0

for i in range(3):
    sum += array1[i] * array2[i]

print(f"\nDot product: {sum}\n")