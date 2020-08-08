""" Make a class Die with one attribute called sides , which has 
a default value of 6. Write a method called roll_die() that prints
a random number between 1 and the number of sides the die has. 
Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times. """

from random import randint

class Dice:

    def __init__(self, sides=6):
        self.sides = sides

    def show_dice(self):
        print(f'this is dice of {self.sides} sides:')
    
    def roll_dice(self):
        return randint(1, self.sides)

dice_6 = Dice()
dice_6.show_dice()
results = []
for roll in range(10):
    tiros = dice_6.roll_dice()
    results.append(tiros)
print(results)

dice_10 = Dice(sides=10)
dice_10.show_dice()
results = []
for roll in range(10):
    tiros = dice_10.roll_dice()
    results.append(tiros)
print(results)

dice_20 = Dice(sides=20)
dice_20.show_dice()
results = []
for roll in range(10):
    tiros = dice_20.roll_dice()
    results.append(tiros)
print(results)