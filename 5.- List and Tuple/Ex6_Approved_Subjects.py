# Ask for grades for 'n' subjects, and display just the ones which the user
# needs to repeat, delete those ones which are passed from the list

print("")
n = 0
while n <= 0:
    n = int(input("Write the subjects quantity: "))
print("")

subjects = []
grades = []

for i in range(n):
    subject = input(f"Write the #{i+1} subject: ")
    grade = float(input(f"Write the {subject} grade: "))
    print("")
    if grade < 6:
        subjects.append(subject)
        grades.append(grade)
print("")

print("SUBJECTS YOU NEED TO REPEAT: \n")
for i in range(0,len(subjects)):
    print(f"{i+1}: {subjects[i]} with {grades[i]} grade . . .")
print("")