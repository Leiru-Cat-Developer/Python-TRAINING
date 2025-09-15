# Write a function that receives a grades list and returns
# a list of FINAL GRADES for each of those grades

def average(grades):
    """
        Receives a grades list and returns a list of grades
            -> grades (list)
    """
    results = []

    for i in range(len(grades)):
        if grades[i] < 6:
            results.append("not passed")
        if grades[i] >= 6:
            results.append("passed")
    
    return results

grades = [10,5,10,5,10,3,10]

print(f"\nThe final average is: {average(grades)}")