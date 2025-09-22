# Write a function that takes a sample of numbers and returns outliers,
# that is, values ​​whose standard score is greater than 3 or less than -3. 
# Note: The standard score of a value is obtained by subtracting the 
# mean and dividing by the standard deviation of the sample.

import statistics

def calculation(numbers: list[int]):
    mean = statistics.mean(numbers)
    deviation = statistics.stdev(numbers)
    def inside(arrayValue):
        value = (arrayValue - mean) / deviation
        print(value,arrayValue)
        return (value < -3) or (value > 3)
    return inside

def outliers(numbers: list[int]) -> list:
    return list(filter(calculation(numbers),numbers))

print(f"\nOutliers: {outliers([1,2,3,4,5,6,7,8,9,10,1000])}")