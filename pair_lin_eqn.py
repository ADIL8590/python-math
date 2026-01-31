#pair of linear equations graphical solution
import matplotlib.pyplot as plt
import numpy as np
# Define the coefficients of the equations
a1, b1, c1 = 2, 3, 8   # 2x + 3y = 8
a2, b2, c2 = 1, -4, -2  # x - 4y = -2
# Create a range of x values
x = np.linspace(-10, 10, 400)
#Calculate corresponding y values for each equation
y1 = (c1 - a1 * x) / b1
y2 = (c2 - a2 * x) / b2
# Plot the equations
plt.plot(x, y1, label=f'{a1}x + {b1}y = {c1}')
plt.plot(x, y2, label=f'{a2}x + {b2}y = {c2}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('pair_linear_equations_graph.png')  # save the figure to a file