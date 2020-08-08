""" Modify rw_visual.py by replacing plt.scatter() with plt.plot().
To simulate the path of a pollen grain on the surface of a drop of
water """

import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(5000)

rw.fill_walk()

plt.figure(dpi=128, figsize=(10, 6))

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, linewidth=1)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()