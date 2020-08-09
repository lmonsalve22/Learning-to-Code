from dice import Dice
import matplotlib.pyplot as plt

dice = Dice()

results = []
for i in range(1000):
    result = dice.roll()
    results.append(result)

frequency = [results.count(i) for i in range(1, dice.num_sides+1)]

x_value = [str(i) for i in range(1, dice.num_sides+1)]

plt.plot(x_value, frequency)
plt.title('''How much times can appear a number in a single dice 
if we roll 1000 times''')
plt.xlabel('numbers')
plt.ylabel('times appearing')

plt.show()