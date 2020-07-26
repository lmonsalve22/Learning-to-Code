""" Write a function that stores information about a car in 
a dictionary. The function should always receive a manufacturer
and a model name. It should then accept an arbitrary number of 
keyword arguments. """

def make_car(brand, model_name, cost, **aditional):
    """ show a simple car description """
    car_info = {}
    car_info['brand'] = brand
    car_info['model_name'] = model_name
    car_info['cost'] = cost
    for key, value in aditional.items():
        car_info[key] = value
    return car_info

car = make_car('Tesla', 'outback', 1000000,
               color='white', wifi=True)
print(car)
