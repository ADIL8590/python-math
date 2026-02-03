# area of trianlgle whose three coordinates are given by user
x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))
x3 = float(input("Enter x-coordinate of third point: "))
y3 = float(input("Enter y-coordinate of third point: "))

def area_of_triangle(x1, y1, x2, y2, x3, y3):
    area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)
    return area
area = area_of_triangle(x1, y1, x2, y2, x3, y3)
print(f"The area of the triangle formed by the points ({x1}, {y1}), ({x2}, {y2}), and ({x3}, {y3}) is: {area} square units.")
# plotting the triangle
import matplotlib.pyplot as plt
plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'b-')
plt.scatter([x1, x2, x3], [y1, y2, y3], color='red')
plt.title("Triangle formed by the given points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
#saving the result to a text file
with open("triangle_area.txt", "w") as file:
    file.write(f"The area of the triangle formed by the points ({x1}, {y1}), ({x2}, {y2}), and ({x3}, {y3}) is: {area} square units.\n")
    file.write("The triangle has been plotted and displayed.\n")
#saving the figure
plt.savefig('triangle_plot.png')