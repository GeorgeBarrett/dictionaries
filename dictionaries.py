import states
import cities

print('-' * 10)
print('NY state has: ', cities['NY'])
print('OR state has: ', cities['OR'])

print('-' * 10)
print('Michigan\'s abbreviation is: ', states['Michigan'])
print('Florida\'s abbreviation is: ', states['Florida'])

print('-' * 10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has :', cities[states['Florida']])

print('-' * 10)
for state, abbreviation in list(states.items()):
    print(f'{state} is abbreviated {abbreviation}')

print('-' * 10)
for abbreviation, city in list (cities.items()):
    print(f'{abbreviation} has the city {city}')

print('-' * 10)
for state, abbreviation in list (states.items()):
    print(f'{state} is abbreviated {abbreviation}')
    print(f'and has city {cities[abbreviation]}')

print('-' * 10)
state = states.get('Texas')

if not state:
    print('Sorry, Texas doesn\'t qualify')

cities = city.get('TX', 'does not exist')
print('The city for the state \'TX\' is: {city}')





