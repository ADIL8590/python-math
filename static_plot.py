#static_plot.py
import matplotlib.pyplot as plt
#data
data_list = [60,58, 48, 52, 44, 56, 45, 37, 58, 49, 50]
#create figure and axis objects
fig, ax = plt.subplots()
#plot data
ax.plot(data_list, marker='o', linestyle='-', color='b')
#add title and labels
ax.set_xlabel('Day Number')
ax.set_ylabel('Temperature (°F)')
ax.set_title('Temperature Over 11 Days')
#save and show plot
plt.savefig('temperature_plot.png')
plt.show() 