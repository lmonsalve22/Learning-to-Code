from dice import Dice
import pygal

d_1 = Dice(8)
d_2 = Dice(8)
results=[]
for roll_dice in range(1000):
    result = d_1.roll() + d_2.roll()
    results.append(result)

max_results = d_1.num_sides + d_2.num_sides
frequencies = [results.count(i) for i in range(2, max_results+1)]

hist = pygal.Bar()

hist.title = 'The result of rolling two dices 1000 times'
hist.x_labels = [str(i) for i in range(2, max_results+1)]
hist.x_title = 'Result' 
hist.y_title = 'Frequency of Results'

hist.add('D8 + D8', frequencies)
hist.render_to_file('15-7.svg')
