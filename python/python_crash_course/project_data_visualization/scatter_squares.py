import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [i**2 for i in x_values]

# c= define the color and we can use RGB
# plt.scatter(x_values, y_values, c='red', edgecolors='none',s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.prism,
            edgecolors='none', s=40)

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# which does the same thing that axis
plt.tick_params(axis='both', which='major', labelsize=14)

# set the range for each axis
plt.axis([0, 1100, 0, 1100000])

# save the file:
# plt.savefig('squares_plot.png')
plt.show()
