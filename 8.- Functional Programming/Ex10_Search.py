# A real state from a city manages a list o properties like this:
# [{'year': 2000, 'meters': 100, 'rooms': 3, 'garage': True, 'zone': 'A'},
# {'year': 2012, 'meters': 60, 'rooms': 2, 'garage': True, 'zone': 'B'},
# {'year': 1980, 'meters': 120, 'rooms': 4, 'garage': False, 'zone': 'A'},
# {'year': 2005, 'meters': 75, 'rooms': 3, 'garage': True, 'zone': 'B'},
# {'year': 2015, 'meters': 90, 'rooms': 2, 'garage': False, 'zone': 'A'}]
# Build a function that allows to do a real state search based on budget
# The function will receive a list of real state and a price, and will
# return another list with the real state price which are lower or equals
# from the base budget. The real state list that returns needs a new pair
# each dictionary with the real state price, where the price calculates with
# the next formula based on zone:
# zone A: price =(meters*1000+rooms*5000+garage*15000) * (1-old/100)
# zone B: price =(meters*1000+rooms*5000+garage*15000) * (1-old/100) * 1.5

def priceCalculator(realStates):
    price = (realStates['meters']*1000
             +realStates['rooms']*5000
             +int(realStates['garage']*15000)) * (1-(2025 - realStates['year'])/100)
    if realStates['zone'] == 'B':
        price *= 1.5
    realStates['price'] = price
    return realStates

def betterPrice(realStates, price):
    """
        Function that calculates the better prices for a real state
            - realState: list of dictionaries
            - price: whatever price you want
    """
    def lowest(realState):
        return realState['price'] <= price
    
    return list(filter(lowest,map(priceCalculator,realStates)))

properties = [
    {'year': 2000, 'meters': 100, 'rooms': 3, 'garage': True, 'zone': 'A'},
    {'year': 2012, 'meters': 60, 'rooms': 2, 'garage': True, 'zone': 'B'},
    {'year': 1980, 'meters': 120, 'rooms': 4, 'garage': False, 'zone': 'A'},
    {'year': 2005, 'meters': 75, 'rooms': 3, 'garage': True, 'zone': 'B'},
    {'year': 2015, 'meters': 90, 'rooms': 2, 'garage': False, 'zone': 'A'}
]
price = float(input("\nWhat is the price you're looking for?: $"))

print(f"\nThe best option is: \n\n\t{betterPrice(properties,price)}")