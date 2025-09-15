# Ask for salary and worked hours, then calculate the salary for the worked hours
hours = float(input("Enter the number of hours worked: "))
salary_per_hour = float(input("Enter the salary per hour: "))
total_salary = hours * salary_per_hour
print(f"The total salary for {hours} hours at {salary_per_hour} per hour is: ${total_salary}")