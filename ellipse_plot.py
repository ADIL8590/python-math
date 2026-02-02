# plot an ellipse for ellipse_plot.py
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
# function to draw an ellipse
def draw_ellipse(ax, center, width, height, angle, color): #draw ellipse function given center,width,height,angle and color
    ellipse = Ellipse(center, width, height, angle=angle, color=color, fill=False, linewidth=1)
    ax.add_artist(ellipse)
# create figure and axis
fig, ax = plt.subplots()
# set aspect of the plot to be equal
ax.set_aspect('equal')
# set limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
# draw ellipse
draw_ellipse(ax, (0, 0), 12, 6, 0, 'green')
# add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.title('Ellipse with width 12, height 6, and angle 30 degrees')
ax.plot(0, 0, 'ro')  # mark center
# add grid and highlight X and Y axes
ax.axhline(0, color='yellow',linewidth=0.5, ls='--')
ax.axvline(0, color='yellow',linewidth=0.5, ls='--')
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()
# save the plot
plt.savefig('ellipse_plot.png')