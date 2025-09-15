# Ask fot a mont, tax and years and display the capital
# obtained every year the inversion lasts

print("")
mont = float(input("Digit the mont: $"))
tax = float(input("Digit the tax: "))
years = int(input("Digit the years: "))
print("")

# capital = amount * (1 + annual_interest / 100) ** years

for i in range(1,years+1):
    print(f"Year {i} - Inversion = {(mont * (1 + tax / 100) ** i):0.2f}")