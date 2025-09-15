# Show division steps like "<n> divided by <m> give us a quotient <c> and rest is <r>"
n = int(input("Enter the dividend (n): "))
m = int(input("Enter the divisor (m): "))
c = n / m
r = n % m
print(f"{n} divided by {m} gives us a quotient {c} and the rest is {r}")