import numpy as np


def getMatrix():
    # Get dimensions from the user
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Get matrix entries from the user in a single line
    print(f"Enter {rows * cols} numbers separated by spaces:")
    entries_str = input()
    entries = list(map(int, entries_str.split()))

    # Reshape the list into a numpy array (matrix)
    matrix = np.array(entries).reshape(rows, cols)

    print("\nYour matrix:")
    print(matrix)
    return matrix


def determinant(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        return "Determinant is only defined for square matrices."
    det = np.linalg.det(matrix)
    return round(det, 6)  # rounding helps remove floating-point noise


matrix = getMatrix()
print(determinant(matrix))
