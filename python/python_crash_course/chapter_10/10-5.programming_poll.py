""" Write a while loop that asks people why they like programming.
Each time someone enters a reason, add their reason to a file
that stores all the responses. """

while True:
    print('For quit enter "q"')
    answer = input('Why you like programming?: ')
    if answer == 'q':
        break
    else:
        with open('programmin_pool.txt', 'a') as f:
            f.write(f'{answer}\n')
