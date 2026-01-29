

# linear algebra using numpy
import numpy as np
def solve_linear_equations(a1, b1, c1, a2, b2, c2):
    """
    Solve the system of linear equations:
    a1*x + b1*y = c1
    a2*x + b2*y = c2

    Parameters:
    a1, b1, c1 : coefficients of the first equation
    a2, b2, c2 : coefficients of the second equation

    Returns:
    (x, y) : solution of the equations
    """
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    solution = np.linalg.solve(A, B)
    return solution[0], solution[1]
# Example usage
a1, b1, c1 = 2, 3, 8   # 2x + 3y = 8
a2, b2, c2 = 1, -4, -2  # x - 4y = -2
x, y = solve_linear_equations(a1, b1, c1, a2, b2, c2)
print(f"The solution is x = {x}, y = {y}")


def matrix_operations(matrix_a, matrix_b):
    """
    Perform basic matrix operations: addition, subtraction, and multiplication.

    Parameters:
    matrix_a : first matrix (2D list or numpy array)
    matrix_b : second matrix (2D list or numpy array)

    Returns:
    addition : result of matrix addition
    subtraction : result of matrix subtraction
    multiplication : result of matrix multiplication
    """
    A = np.array(matrix_a)
    B = np.array(matrix_b)
    addition = A + B
    subtraction = A - B
    multiplication = A@B
    return addition, subtraction, multiplication
# Example usage
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[7, 8, 9], [10, 11, 12], [13, 14, 15]]
addition, subtraction, multiplication  = matrix_operations(matrix_a, matrix_b)
print("Matrix Addition:\n", addition)
print("Matrix Subtraction:\n", subtraction)
print("Matrix Multiplication:\n", multiplication)
