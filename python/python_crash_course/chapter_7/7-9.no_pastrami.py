""" Add pastrami to exercise 7-8 and print a message that you run
out of pastrami, and use a while loop to remove it and make
sure that this doesn't appear in the final result """

sandwich_orders = ['pastrami', 'pastrami', 'pastrami', 'hawaina', 'peruana', 'criolla', 'hotdog', 'chicken junior']
finished_sandwiches = []

print('We run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f'I made your {sandwich.title()} sandwich')

while sandwich_orders:
    out = sandwich_orders.pop()
    finished_sandwiches.append(out)

print('WE MADE:')
for f_sandwich in finished_sandwiches:
    print(f'- {f_sandwich}')