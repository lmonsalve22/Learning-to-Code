""" Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant . Make a Restaurant 
instance, and call one of Restaurant ’s methods to show that the
import statement is working properly. """

from restaurant import Restaurant

my_place = Restaurant('Healthy food', 'vegetable food')
my_place.describe_restaurant()