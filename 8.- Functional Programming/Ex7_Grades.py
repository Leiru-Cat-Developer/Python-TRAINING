# Write a function that receives a dictionary with subjects and grades
# from a student and returns another dictionary with the subjects
# on uppercase and if pass or not pass the subject

def qualifications(dictionary: dict) -> dict:
    result = {}
    for i, k in dictionary.items():
        subject = i.upper()
        if k > 6:
            result[subject] = "PASSED"
        else:
            result[subject] = "REPROVED"
    return result

print("")
test = {"Maths":5.6,"Spanish":4.9,"English":7.7,"Tech":10.0}
print(f"Results: {qualifications(test)}")