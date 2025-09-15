# Write a function that receives a sample of numbers and returns
# a dictionary with median, variance and deviance

import statistics

def dictionary(numbers):
    """
        RETURNS:
         -> AVG
         -> VAR
         -> DEV
    """
    mean = statistics.mean(numbers)
    variance = statistics.pvariance(numbers,mean)
    deviance = statistics.pstdev(numbers)
    results = {"Median":mean, "Variance":variance, "Deviance":deviance}
    return results

numbers = [2.3, 5.7, 6.8, 9.7, 12.1, 15.6]

print("\nThe dictionary is as follows: " + str(dictionary(numbers)))