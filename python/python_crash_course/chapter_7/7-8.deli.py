""" Make a list with orders and then move it to finished orders,
print them all! """

sandwich_orders = ['hawaina', 'peruana', 'criolla', 'hotdog', 'chicken junior']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f'I made your {sandwich.title()} sandwich')

while sandwich_orders:
    out = sandwich_orders.pop()
    finished_sandwiches.append(out)

print('WE MADE:')
for f_sandwich in finished_sandwiches:
    print(f'- {f_sandwich}')