import numpy as np
import matplotlib.pyplot as plt
def cal_roots_poly(a,b,c):
    a= int(a)
    b= int(b)
    c= int(c)
    dis= (b**2-4*a*c)
    if dis>0:
        root1= (-b + dis**0.5)/(2*a)
        root2= (-b - dis**0.5)/(2*a)
        print("Roots are real and distinct:", root1, root2)
    elif dis==0:
        root= -b/(2*a)
        print("Roots are real and equal:", root)
    else:
        real_part= -b/(2*a)
        imag_part= (-dis**0.5)/(2*a)
        print("Roots are complex:", complex(real_part, imag_part), complex(real_part, -imag_part))
# Example usage
cal_roots_poly(1,-3,2)
# plot graph of quadratic equation  y=ax**2+bx+c on y_axis against x values on x-axis

def plot_quadratic(a, b, c, x_range):
    """
    Plot the quadratic function y = ax^2 + bx + c over the specified x range.

    Parameters:
    a, b, c : coefficients of the quadratic function
    x_range : tuple (x_min, x_max) specifying the range of x values
    """
    x_min, x_max = x_range
    x = np.linspace(x_min, x_max, 400)
    y = a * x**2 + b * x + c

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
    plt.title('Quadratic Function Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()
# Example usage
plot_quadratic(1, -3, 2, (-10, 10))
