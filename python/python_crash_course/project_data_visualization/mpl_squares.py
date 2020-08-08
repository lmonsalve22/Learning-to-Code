import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

# Drawing a line
plt.plot(squares, linewidth=5)
# The title
plt.title('Square Numbers', fontsize=24)
# Configuration for x side
plt.xlabel('Value', fontsize=14)
# Configuration fot y side
plt.ylabel('Square of Value', fontsize=14)
# Configuration for values, where:
# axis = what side of the table we want to apply 
# labelsize = just the size of the font
plt.tick_params(axis='both', labelsize=14)

plt.show()