# Into an epic fight between humans and monsters both bands has a list
# of fighters with specific powers
# Battle develops in rounds, each round faces each fighter of the band
# The band with higher attack power wins the round, and it's power should
# be the sum of the next fighter in his team
# In draw case, both fighters fall and doesn't affect the next round
# Given 2 strings of text "zombies", "humans" where each digit 1-9
# represents the power of the fighter, determinate who stays at the end
# and the power left
# IMPORTANT: 2 strings always has the same length
# OUTPUT: String that represents the final result

def battleHorde(zombies: str, humans: str):
    if (len(list(zombies)) != len(list(humans))): return print("\nNot possible")
    
    z = 0
    h = 0
    
    zombiesValues = [int(x) for x in list(zombies)]
    humansValues = [int(x) for x in list(humans)]

    for i in range(len(zombiesValues)):
        z += zombiesValues[i]
        h += humansValues[i]

    if h == z: return print("\nx")
    return print(f"\n{abs(h-z)}{"h" if h > z else "z"}")

zombies = input("\nWrite some values for zombies: ")
humans = input("\nWrite some values for humans: ")

battleHorde(zombies,humans)