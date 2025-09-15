# Write a function that receives another bool function and a list
# and returns another list with the elements of the list which
# returns true after apply the bool function

def boolean(fun,lis):
    """
        Returns the contrary value
            -> fun (function)
            -> lis (list)
    """
    result = []
    for i in lis:
        if fun(i):
            result.append(i)
    return result

def change(value):
    return value % 2 == 0

print(f"\nThe results are: {boolean(change,[1,2,3,4,5,6,7,8,9,10])}")