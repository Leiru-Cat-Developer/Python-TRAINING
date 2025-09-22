# Write a function that takes a sample of numbers and returns outliers,
# that is, values ​​whose standard score is greater than 3 or less than -3. 
# Note: The standard score of a value is obtained by subtracting the 
# mean and dividing by the standard deviation of the sample.

import statistics

def outliers(numbers: list[int]) -> list:
    numbers.sort()

    firstHalf = []
    secondHalf = []

    for i in range(len(numbers)//2):
        firstHalf.append(numbers[i])
    for i in range(len(numbers)//2,len(numbers)):
        secondHalf.append(numbers[i])

    q1 = statistics.median(firstHalf)
    q3 = statistics.median(secondHalf)
    iqr = q3 - q1

    def difference(numbers):
        return (numbers < (q1 - 1.5 * iqr)) or (numbers > (q3 + 1.5 * iqr))

    return list(filter(difference,numbers))

print(f"\nOutliers: {outliers([1,2,3,4,5,6,7,8,9,100])}")
print(f"\nOutliers: {outliers([10,20,30,40,50])}")
print(f"\nOutliers: {outliers([1,2,3,4,5,6,8,79])}")

# EDGE CASES
print(f"\nOutliers: {outliers([10,12,14,15,16,18,20,50])}") # 50
print(f"\nOutliers: {outliers([-20,5,8,9,10,11,12,15])}") # -20
print(f"\nOutliers: {outliers([1,25,28,30,32,35,38,100])}") # 1,100
print(f"\nOutliers: {outliers([10,20,30,40,50,60,70,80])}") # nothing
print(f"\nOutliers: {outliers([6,7,15,36,39,40,41,42,43,47,49,78])}") # 78