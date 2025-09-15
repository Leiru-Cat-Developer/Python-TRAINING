# Write a program that stores the dictionary with the credits for the subjects
# in a course{'Mathematics': 6, 'Physics': 4, 'Chemistry': 5} and then displays
# the credits for each subject on the screen in the format <subject> has <credits> credits
# where <subject> is each of the subjects in the course, and <credits> 
# are its credits. At the end, it should also display the total
# number of credits for the course.

print("")
subjects = {'Math':6, 'Physics':4, 'Chemistry':5}
total_credits = 0

for sub, credits in subjects.items() :
    print(f"{sub} has {credits}")
    total_credits += credits

print(f"\nTotal credits are: {total_credits}")