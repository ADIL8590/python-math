# plot a cicle for circles_plot.py
import matplotlib.pyplot as plt
import numpy as np
# function to draw a circle
def draw_circle(ax, center, radius, color):
    circle = plt.Circle(center, radius, color=color, fill=False, linewidth=1)
    ax.add_artist(circle)

# create figure and axis
fig, ax = plt.subplots()
# set aspect of the plot to be equal
ax.set_aspect('equal')
# set limits
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
# draw circles
draw_circle(ax, (0, 0), 4, 'blue')
# add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.plot(0, 0, 'ro')  # mark center
# add grid and highlight X and Y axes
ax.axhline(0, color='yellow',linewidth=0.5, ls='--')
ax.axvline(0, color='yellow',linewidth=0.5, ls='--')
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
#add title
plt.title('Circle with radius 4 centered at (0,0)')
plt.show()
# save the plot
plt.savefig('circle_plot.png')



