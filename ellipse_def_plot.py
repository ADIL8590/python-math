# Plot parbolas of the form (x^2/a^2) + (y^2/b^2) = 1
import numpy as np
import matplotlib.pyplot as plt
# Function to plot Ellipse
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
def plot_ellipse(a, b, ax):
    x = np.linspace(-10, 10, 400)
    y1 = b * np.sqrt(1 - (x**2 / a**2))
    y2 = -b * np.sqrt(1 - (x**2 / a**2))
    ax.plot(x, y1, 'r', label=f'ellipse: (x^2/{a}^2) + (y^2/{b}^2) = 1')
    ax.plot(x, y2, 'r')
# Create figure and axis
fig, ax = plt.subplots()
# Set aspect of the plot to be equal
ax.set_aspect('equal')
# Set limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
# Plot ellipse with a and b from user input
plot_ellipse(a, b, ax)
# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.title('Ellipse Plot')
# Add grid and highlight X and Y axes
ax.grid(True)
ax.axhline(0, color='yellow', linewidth=0.5)
ax.axvline(0, color='yellow', linewidth=0.5)
plt.show()
# Save the plot
plt.savefig('ellipse_def_plot.png')