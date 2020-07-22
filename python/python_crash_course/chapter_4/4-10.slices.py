""" Using a list:
1. slice The first three items
2. slice The three items from the middle 
3. slice The last three items """

cubes = [cube**2 for cube in range(1,11)]

print(cubes)

print(f'The first three items in the list are: {cubes[:3]}') #1
print(f'The three items from the middle of the list are: {cubes[3:6]}') #2
print(f'The last three items in the list are: {cubes[-3:]}') #3