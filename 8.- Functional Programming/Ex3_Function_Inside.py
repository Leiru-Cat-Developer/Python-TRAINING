# Write a function that receives another function and a list, and returns
# another list with the result to apply the function given for each of
# the elements of the list


def result(fun,lis):
    """
        Return a lis of numbers with a function
        applied
            -> fun (function)
            -> lis (list)
    """
    answer = []
    for i in lis:
        answer.append(fun(i))

    return answer

def square(number):
    return number ** 2

print(f"\nThe square result is: {result(square,[1,2,3,4,5])}")