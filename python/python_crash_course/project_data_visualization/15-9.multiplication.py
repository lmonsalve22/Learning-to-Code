from dice import Dice
import pygal

d1 = Dice()
d2 = Dice()
results=[]
for roll_dice in range(1000):
    result = d1.roll() * d2.roll()
    results.append(result)
# print(results)


max_results = d1.num_sides + d2.num_sides
frequencies = [results.count(i) for i in range(2, max_results+1)]

hist = pygal.Bar()

hist.title = 'The result of rolling two dices 1000 times'
hist.x_labels = [str(i) for i in range(2, max_results+1)]
hist.x_title = 'Result' 
hist.y_title = 'Frequency of Results'

hist.add('D8 + D8', frequencies)
hist.render_to_file('15-9.svg')
