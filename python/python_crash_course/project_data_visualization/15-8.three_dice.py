import pygal
from dice import Dice

dice_1 = Dice()
dice_2 = Dice()
dice_3 = Dice()

results = []
for i in range(100):
    result = dice_1.roll() + dice_2.roll() +dice_3.roll()
    results.append(result)

max_results = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides 
frequency = [results.count(i) for i in range(3, max_results+1)]

#Pygal structure
hist = pygal.Bar()

hist.title = '3 dices a 100 times'

hist.x_labels = [str(i) for i in range(3, max_results+1)]

hist.add('D6 + D6 + D6', frequency)

hist.render_to_file('15-8.svg')