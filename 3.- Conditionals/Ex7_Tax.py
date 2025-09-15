# lower than 10,0000 = 5%
# between 10,000 and 20,000 = 15%
# between 20,000 and 35,000 = 20%
# between 35,000 and 60,000 = 30%
# higher than 60,000 = 45%
# Ask for annual rent and show the percentage it belongs
rent = float(input("Write the rent you pay: "))

if rent < 10000:
    print("Tax 5%")
if rent >= 10000 and rent <= 20000:
    print("Tax 15%")
if rent > 20000 and rent <= 35000:
    print("Tax 20%")
if rent > 35000 and rent <= 60000:
    print("Tax 30%")
if rent > 60000:
    print("Tax 45%")