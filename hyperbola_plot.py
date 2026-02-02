# Plot hyperbolas of the form (x^2/a^2) - (y^2/b^2) = 1
import numpy as np
import matplotlib.pyplot as plt
# Function to plot hyperbola
def plot_hyperbola(a, b, ax):
    x = np.linspace(-10, 10, 400)
    y1 = b * np.sqrt((x**2 / a**2) - 1)
    y2 = -b * np.sqrt((x**2 / a**2) - 1)
    ax.plot(x, y1, 'r', label=f'Hyperbola: (x^2/{a}^2) - (y^2/{b}^2) = 1')
    ax.plot(x, y2, 'r')
# Create figure and axis
fig, ax = plt.subplots()
# Set aspect of the plot to be equal
ax.set_aspect('equal')
# Set limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
# Plot hyperbola with a=5, b=3
plot_hyperbola(5, 3, ax)
# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.title('Hyperbola Plot')
# Add grid and highlight X and Y axes
ax.grid(True)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
plt.show()
# Save the plot
plt.savefig('hyperbola_plot.png')
