# Plot parabolas of the form y^2 = 4ax by user-defined a
import numpy as np
import matplotlib.pyplot as plt
# Function to plot Parabola
a = float(input("Enter the value of a: "))
def plot_parabola(a, ax):
    x = np.linspace(-10, 10, 400)
    y1 = 2 * np.sqrt(a * x)
    y2 = -2 * np.sqrt(a * x)
    ax.plot(x, y1, 'r', label=f'Parabola: y^2 = 4*{a}*x')
    ax.plot(x, y2, 'r')
# Create figure and axis
fig, ax = plt.subplots()
# Set aspect of the plot to be equal
ax.set_aspect('equal')
# Set limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
# Plot parabola with a from user input
plot_parabola(a, ax)
# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.title(f'Parabola: y^2 = 4*{a}*x')
# Add grid and highlight X and Y axes
ax.grid(True)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
plt.show()
# Save the plot
plt.savefig('parabola_plot.png')