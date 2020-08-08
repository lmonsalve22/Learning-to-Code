""" Write a function that accepts a list of items a person 
wants on a sandwich. The function should have one parameter
that collects as many items as the function call provides, 
and it should print a summary of the sandwich that is being ordered. """

def sandwiches_order(*sandwich):
    print('ORDER:')
    for order in sandwich:
        print(f'- {order.title()}')

sandwiches_order('peruvian', 'mcburger', 'chicken junior')
sandwiches_order('american classic', 'fish burger', 'chicken')
sandwiches_order('onion', 'simple burger', 'turkey')