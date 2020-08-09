from dice import Dice
import pygal

dice = Dice()

results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

# Analyze the results:
frequencies = [results.count(value) for value in range(1, dice.num_sides+1)]

# Visualize the results:
hist = pygal.Bar()

hist._title = 'Results of rolling one D6 1000 times'
hist.x_labels = [str(i) for i in range(1, dice.num_sides+1)]
hist.x_title = 'Results'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('dice_visual_1.svg')
