# Calculate the savings account balance after 1, 2 and 3 years, 4% interest rate
money = float(input("Enter the amount of money in the savings account: $"))

interest_rate = 0.04

year_1 = money * (1 + interest_rate)
year_2 = year_1 * (1 + interest_rate)
year_3 = year_2 * (1 + interest_rate)

print("The balance after 1 year is: $", round(year_1, 2))
print("The balance after 2 years is: $", round(year_2, 2))
print("The balance after 3 years is: $", round(year_3, 2))