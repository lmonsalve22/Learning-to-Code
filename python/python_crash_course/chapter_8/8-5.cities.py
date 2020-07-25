""" Write a function called describe_city() that accepts 
the name of a city and its country. The function should 
print a simple sentence, such as Reykjavik is in Iceland . 
Give the parameter for the country a default value. """

def describe_city(city, country='peru'):
    """ Name for a city and his location """
    return f'{city.title()} is in {country.title()}\n{"-"*50}'

print(describe_city('lima'))
print(describe_city('arequipa'))
print(describe_city('miami', country='usa'))