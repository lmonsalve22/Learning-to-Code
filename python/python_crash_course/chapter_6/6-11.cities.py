""" Make a dictionary and store some data, make sure
to print all the information about it """

cities = {
    'new york': {
        'country': 'usa',
        'population': 1000000,
        'fact': 'time square'
    },
    'lima': {
        'country': 'peru',
        'population': 500000,
        'fact': 'main city'
    },
    'sao paulo': {
        'country': 'brazil',
        'population': 20000000,
        'fact': 'feijoada'
    }
}

for city, info in cities.items():
    name = city.title().upper()
    country = info['country'].title()
    population = info['population']
    fact = info['fact'].title()
    print(f'{name}\n- Country: {country}\n- Population: {population}\n- Fact: {fact}')