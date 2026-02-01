# plot animated line
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
#create empty data list
x = []
y = []
# function that draws each frame of the animation
def animate(i):
    x.append(i)
    pt = randint(1, 9) #generate random temperature between 30 and 70
    y.append(pt)  

    ax.clear()
    ax.plot(x, y, marker='o', linestyle='-', color='b')
    ax.set_xlabel('Day Number')
    ax.set_ylabel('Temperature (°F) at Sonnar')
    ax.set_title('Temperature Over Days')
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 10)
# create figure and axis objects
fig, ax = plt.subplots()
# create animation object
ani = FuncAnimation(fig, animate, frames=range(11), interval=500)
#plot
plt.show()
#save animation
plt.savefig('temperature_plot.png')