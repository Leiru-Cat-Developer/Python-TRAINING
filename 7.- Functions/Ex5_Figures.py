# Write a function calculates a circle area and another which
# calculates the cylinder volume using the first function

def circleArea(radius):
    """CALCULATES CIRCLE AREA"""
    return 3.1416 * (radius ** 2)

def cylinderVolume(radius, height):
    """CALCULATES CYLINDER VOLUME"""
    return height * circleArea(radius)

radius = float(input("\nWrite the circle radius: "))
height = float(input("Write the cylinder height: "))

print("\nThe volume cylinder result is: " + str(cylinderVolume(radius,height)))