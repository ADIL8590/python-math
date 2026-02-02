# plot a cicle for circles_plot.py
import matplotlib.pyplot as plt
# function to draw a circle
center = tuple(map(float, input("Enter the center coordinates as x,y: ").split(',')))
radius = float(input("Enter the radius of the circle: "))
def draw_circle(ax, center, radius, color):
    circle = plt.Circle(center, radius, color=color, fill=False, linewidth=1)
    ax.add_artist(circle)

# create figure and axis
fig, ax = plt.subplots()
# set aspect of the plot to be equal
ax.set_aspect('equal')
# set limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
# draw circle with user input
draw_circle(ax, center, radius, 'blue')
# add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.plot(center[0], center[1], 'ro')  # mark center
# add grid and highlight X and Y axes
ax.axhline(0, color='yellow',linewidth=0.5, ls='--')
ax.axvline(0, color='yellow',linewidth=0.5, ls='--')
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
#add title
plt.title(f'Circle with radius {radius} centered at {center}')
plt.show()
# save the plot
plt.savefig('circle_plot.png')



