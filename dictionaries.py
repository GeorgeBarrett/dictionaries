# a list of states
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# a list of cities
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

# i can add new cities like so
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)

# I am calling the cities and then NY. The parantheses are important 
print('NY state has: ', cities['NY'])
print('OR state has: ', cities['OR'])

print('-' * 10)
print('Michigan\'s abbreviation is: ', states['Michigan'])
print('Florida\'s abbreviation is: ', states['Florida'])

print('-' * 10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has :', cities[states['Florida']])

print('-' * 10)
# this loops through the items in 'states' and will list them
for state, abbreviation in list(states.items()):
    # this prints the state and its abbreviation
    print(f'{state} is abbreviated {abbreviation}')

print('-' * 10)
# this loops through the items within 'cities' and will list them
for abbreviation, city in list (cities.items()):
    print(f'{abbreviation} has the city {city}')

print('-' * 10)
# this loops through the items in 'states' and will list them
for state, abbreviation in list (states.items()):
    # each state will be printed with its abbreviation  
    print(f'{state} is abbreviated to {abbreviation}')
    # each city will be printed
    print(f'and has a city named {cities[abbreviation]}') # {cities[abbreviation]} ? 

print('-' * 10)
# this variable is searching through 'states' and tring to get Texas
state = states.get('Texas')

# if the state variable proves false then the print message will appear
if not state:
    print('Sorry, Texas doesn\'t qualify')

# this is similar logic to the variable above par the print message uses an f string
city = cities.get('TX', 'does not exist')
print(f"The city for the state 'TX' is: {city}")





