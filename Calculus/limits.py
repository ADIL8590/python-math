#finding  limits of a function using user defined function
import numpy as np
import matplotlib.pyplot as plt
def find_limit(func, x, approach):
    if approach == 'left':
        return func(x - 0.0001)  # Approaching from the left
    elif approach == 'right':
        return func(x + 0.0001)  # Approaching from the right
    else:
        raise ValueError("Approach must be 'left' or 'right'.")


# Example usage:
if __name__ == "__main__":
    # Define a sample function
    def function(x):
        return (x**3 - 1) / (x - 1)

    x_value = 1
    left_limit = find_limit(function, x_value, 'left')
    right_limit = find_limit(function, x_value, 'right')

    


    print(f"Left-hand limit as x approaches {x_value}: {left_limit}")
    print(f"Right-hand limit as x approaches {x_value}: {right_limit}")
    if abs(left_limit - right_limit) < 0.1:
        print(f"The limit as x approaches {x_value} is equal to: {int(right_limit)}")
    else:
        print(f"The limit does not exist as the left-hand limit ({left_limit}) and right-hand limit ({right_limit}) are not equal.Hence limit does not exist.")


#plot function to visualize limits  

x_vals = np.linspace(0.5, 1.5, 100)
y_vals = [function(x) for x in x_vals]
plt.plot(x_vals, y_vals, label='f(x)')
plt.axvline(x=x_value, color='red', linestyle='--', label=f'x = {x_value}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function Visualization')
plt.legend()
plt.grid(True)
plt.show()
