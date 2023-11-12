

import numpy as np
from scipy.sparse import find



def sparse_matrix_to_csr(matrix):
    # Find non-zero elements and their indices
    row_indices, col_indices, values = find(matrix)

    # Compute row pointers
    row_ptr = np.concatenate(([0], np.cumsum(np.bincount(row_indices))))

    return values, col_indices, row_ptr

def get_original_row(values, col_indices, row_ptr, index):
    # Find the start and end indices in the values and col_indices arrays for the specified row
    start_idx = row_ptr[index]
    end_idx = row_ptr[index + 1]

    # Extract the values and column indices for the specified row
    row_values = values[start_idx:end_idx]
    row_col_indices = col_indices[start_idx:end_idx]

    # Reconstruct the row using the original matrix shape
    original_row = np.zeros(row_ptr[-1] - 1)  # Use the total number of columns in the original matrix

    # Fill in the values at their respective column indices
    original_row[row_col_indices] = row_values

    return original_row

matrix = [
    [1, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 5, 0, 0, 0],
    [0, 0, 6, 0, 0, 7, 0]
]
sparse_matrix = np.array(matrix)

[values, col_indices, row_ptr]=sparse_matrix_to_csr(matrix)

print( get_original_row(values, col_indices, row_ptr, 0) )
print( get_original_row(values, col_indices, row_ptr, 1) )
print( get_original_row(values, col_indices, row_ptr, 2) )





