""" Write a function called city_country() that takes in the 
name of a city and its country. The function should return a
string formatted like this: "Santiago, Chile" """

def city_country(city, country):
    return f'{"-"*50}\n"{city.title()}, {country.title()}"'

print(city_country('lima', 'perú'))
print(city_country('miami', 'usa'))
print(city_country('sao paulo', 'brazil'))
