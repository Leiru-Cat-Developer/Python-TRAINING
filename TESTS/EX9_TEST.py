# BINARY SEARCH

def binarySearch(array: list[int], number: int):
    array.sort()
    print("\n" + str(array))
    leftPos = 0
    rightPos = len(array)-1
    while leftPos <= rightPos:
        half = (leftPos + rightPos)//2
        if array[half] == number:
            return f"\nThe number exists in position: {str(half)}"
        elif array[half] > number:
            rightPos = half - 1
        elif array[half] < number:
            leftPos = half + 1
    return "\nThe number doesn't exists"

array = [5,7,4,10,54,3,69,11,52,30]
number = 99
print(binarySearch(array,number))