# Ask for subject grades and display the grade for each value in console

print("")
subjects = ["History","Spanish","Programming","English"]
grades = []

for i in range(0,len(subjects),1):
    grade = float(input(f"Write note for {subjects[i]} subject: "))
    grades.append(grade)
print("")

for i in range(len(subjects)):
    print(f"Grade for {subjects[i]} subject: {grades[i]}")
print("")