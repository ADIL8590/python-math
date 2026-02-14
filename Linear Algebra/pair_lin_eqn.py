#pair of linear equations graphical solution
import matplotlib.pyplot as plt
import numpy as np
# Define the coefficients of the equations
a1, b1, c1 = 2, 1, 8   # 2x + y = 8
a2, b2, c2 = 1, -1, 1  # x - y = 1
# Create a range of x values
x = np.linspace(-10, 10, 400)
#Calculate corresponding y values for each equation
y1 = (c1 - a1 * x) / b1 #putting in y= (c1 - a1x)/b different values of x to get different values of y
y2 = (c2 - a2 * x) / b2 #putting in y= (c2 - a2x)/b different values of x to get different values of y
# Plot the equations
plt.plot(x, y1, label=f'{a1}x + {b1}y = {c1}') #label for first equation
plt.plot(x, y2, label=f'{a2}x + {b2}y = {c2}') #label for second equation
# Find the intersection point
A = np.array([[a1, b1], [a2, b2]])
B = np.array([c1, c2])
solution = np.linalg.solve(A, B)
x_sol, y_sol = solution
# Plot the intersection point
plt.scatter(x_sol, y_sol, color='red', label=f'Intersection ({x_sol:.2f}, {y_sol:.2f})')
plt.xlabel('x') #
plt.ylabel('y')
plt.legend() 
plt.grid(True)
plt.show()
plt.savefig('pair_linear_equations_graph.png')  # save the figure to a file