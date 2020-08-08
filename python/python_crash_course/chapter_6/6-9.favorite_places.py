""" Think of three names to use as keys in the dictionary,
and store one to three favorite places for each person. """

favorite_places = {
    'james' : ['brazil', 'cuzco', 'campinas'],
    'cynthya' : ['argentina', 'san marcos'],
    'carolina' : ['peru', 'san francisco']
}

for name, places in favorite_places.items():
    print(f'{name.title().upper()}')
    for place in places:
        print(f'- {place.title()}')
