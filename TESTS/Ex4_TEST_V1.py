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
    """
        This function simulates a battle
            -> zombies
            -> humans
    """
    if len(list(zombies)) != len(list(humans)): return "\nYou need the same length"
    accumulated = 0
    stringZombie = list(zombies)
    stringHuman = list(humans)
    zombiesValues = [int(x) for x in stringZombie]
    humansValues = [int(x) for x in stringHuman]
    lastPos = len(zombiesValues)

    for i in range(len(zombiesValues)-1):
        if zombiesValues[i] == humansValues[i]:
            continue
        if zombiesValues[i] > humansValues[i]:
            accumulated = zombiesValues[i] - humansValues[i]
            zombiesValues[i+1] += accumulated
        if zombiesValues[i] < humansValues[i]:
            accumulated = humansValues[i] - zombiesValues[i]
            humansValues[i+1] += accumulated

    if humansValues[lastPos-1] == zombiesValues[lastPos-1]:
        return "x" # draw
    if humansValues[lastPos-1] > zombiesValues[lastPos-1]:
        return f"{humansValues[lastPos-1] - zombiesValues[lastPos-1]}h" # humans
    if humansValues[lastPos-1] < zombiesValues[lastPos-1]:
        return f"{zombiesValues[lastPos-1] - humansValues[lastPos-1]}z" # zombies


zombie = input("\nWrite zombie values: ")
human = input("Write human values: ")

print(f"\nResult: {battleHorde(zombie,human)}")