# Do the same as exercise 7 but just display the approved notes

def qualifications(dictionary: dict) -> dict:
    result = {}
    for i, k in dictionary.items():
        subject = i.upper()
        if k > 6:
            result[subject] = "PASSED"
    return result

print("")
test = {"Maths":5.6,"Spanish":4.9,"English":7.7,"Tech":10.0}
print(f"Results: {qualifications(test)}")