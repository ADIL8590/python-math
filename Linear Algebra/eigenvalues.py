# eigen values and eigen vectors of a matrix
import numpy as np
def calculate_eigenvalues_eigenvectors(matrix):
    """
    Calculate the eigenvalues and eigenvectors of a given square matrix.

    Parameters:
    matrix : 2D list or numpy array representing the square matrix

    Returns:
    eigenvalues : array of eigenvalues
    eigenvectors : 2D array where each column is an eigenvector
    """
    A = np.array(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors
# Example usage
matrix = [[4, -2], [1, 1]]
eigenvalues, eigenvectors = calculate_eigenvalues_eigenvectors(matrix)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)