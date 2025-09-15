# During hallowing night a witch is preparing a potion. She has a list
# of potions, each one with an associated power, she wants to combine
# 2 of them to get a specific total power

# Given a list of integer numbers where each number represents the power
# of a potion and an integer number represents the objective power, you
# should find the index in the first two potions which sum exactly
# the objective power

# For example
#   const potions = [4,5,6,2]
#   const goal = 8
#   createMagicPotion(potions,goal) -> [2,3]

# If there's no possible combination, returns undefined
#   const potions [1,2,3,4]
#   const goal = 8
#   createMagicPotion(potions,goal) -> undefined

def createMagicPotion(potions: list, goal: int):
    for i in range(len(potions)):
        for j in range(len(potions)):
            if i == j:
                continue
            if potions[i] + potions[j] == goal:
                return [i,j]
    return "undefined"

print("\n->" + str(createMagicPotion([4,5,6,2],8)))
print("\n->" + str(createMagicPotion([1,2,3,4],9)))
print("\n->" + str(createMagicPotion([4,4,4,5,10],14)))
print("\n->" + str(createMagicPotion([3,3,0],3)))