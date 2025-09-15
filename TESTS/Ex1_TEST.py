# Create a function that finds out all the combinations of numbers from a list that sums
# the objective value
# - The function will receive a list of int positive numbers and a value
# - To get combinations you just can use an element once (but can exists repeated elements on it)
# Example: Array = [1,5,3,2], Objective = 6
# Solutions: [1,5] and [1,3,2] (both combinations sums 6)
# If there's no combinations, return an empty list

def find_sums(numbers: list, target: int) -> list:
    """
        Finds out all the combinations from a list of numbers
            -> list (array)
            -> target (int)
    """
    # We check for positive numbers in both cases
    for i in range(len(numbers)):
        if numbers[i] < 0:
            return "\n\nNegative numbers in list are not allowed . . ."
    if target <= 0:
        return "\n\nTarget should be positive and higher than 0, try again . . ."
    
    # EXS
    def find(start: int, target: int, combinations: list):
        # Find the solution
        if target == 0:
            solution.append(combinations[:]) # Copy all the numbers on the new array
            return

        # There's no solution
        if target < 0 or start == len(numbers):
            # If the target is overflowed or start is already ended
            return solution

        # Backtracking
        for i in range(start,len(numbers)):
            # If number already exists, is ignored
            if i > start and numbers[i] == numbers[i-1]:
                continue
            combinations.append(numbers[i])
            find(i + 1, target - numbers[i], combinations)
            combinations.pop()

    solution = []
    numbers.sort() # Ordering the target [2,3,4,1] = [1,2,3,4]
    find(0,target,[]) # Backtracking function
    return solution

print(f"\nSOLUTION: {find_sums([10],6)}")