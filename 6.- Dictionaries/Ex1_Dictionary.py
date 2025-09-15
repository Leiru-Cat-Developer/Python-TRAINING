# Save this dictionary and ask for the badge and show the symbol
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

print("")
dictionary = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
money = input("Write the badge you want? ")
print("")

print(dictionary.get(money.title(),"Badge doesn't exists"))
print("")