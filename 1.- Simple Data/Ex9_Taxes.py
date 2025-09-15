# Ask for for an amount to invest, the annual interest and the number of years, and displays on the screen the capital obtained from the investment
amount = float(input(("Enter the amount to invest: ")))
annual_interest = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the number of years: "))

capital = amount * (1 + annual_interest / 100) ** years

print(f"The capital obtained from the investment is: ${capital:.2f}")