import numpy as np

# Example 2D NumPy array
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# Slice the first two rows and the first two columns
sub_matrix = matrix[:2, :2]
print("First two rows and columns:")
print(sub_matrix)

# Slice the second and third rows, and the third and fourth columns
sub_matrix_2 = matrix[1:3, 2:4]
print("\nSecond and third rows, third and fourth columns:")
print(sub_matrix_2)

# Select all elements in the second row
row_slice = matrix[1, :]
print("\nSecond row:")
print(row_slice)

# Select all elements in the third column
column_slice = matrix[:, 2]
print("\nThird column:")
print(column_slice)
