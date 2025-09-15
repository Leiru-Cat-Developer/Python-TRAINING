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