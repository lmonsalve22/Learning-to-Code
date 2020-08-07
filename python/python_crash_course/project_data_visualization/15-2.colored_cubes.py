""" Apply a colormap to your cubes plot """

import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [i**3 for i in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

plt.title('The cube of a number')
plt.xlabel('numbers', fontsize=14)
plt.ylabel('the cube', fontsize=14)

plt.show()