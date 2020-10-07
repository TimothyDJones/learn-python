# matrix_determinant.py
# https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python

def determinant_2_by_2(matrix):
    if len(matrix) != 2:
        return 0
    
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return determinant

def determinant_recursive(matrix, determinant=0):
    rank = len(matrix)      # Matrix rank (number of rows/columns)
    
    if rank == 1:
        return matrix[0][0]
    elif rank == 2:
        return determinant_2_by_2(matrix)
    
    # Find sub-matrix and call method recursively until the 2x2 case.
    for col in range(rank):
        sub_matrix = matrix[:]      # Make a copy of the matrix to avoid mutation.
        sub_matrix = sub_matrix[1:]     # Remove first row, because sub-matrix doesn't include it.
        for row in range(len(sub_matrix)):
            # For each *remaining* row remove the elements from "col"
            sub_matrix[row] = sub_matrix[row][0:col] + sub_matrix[row][col+1:]

        sub_matrix_det = determinant_recursive(sub_matrix)
        
        determinant += ((-1) ** (col % 2)) * matrix[0][col] * sub_matrix_det
        print(sub_matrix, sub_matrix_det, determinant, ((-1) ** (row % 2)) * matrix[0][col] * sub_matrix_det)        
    return determinant

def determinant(matrix):
    return determinant_recursive(matrix)
    

if __name__ == "__main__":
    print(determinant([ [1] ]))
    print(determinant([ [1, 3], [2,5] ]))
    print(determinant([ [2,5,3], [1,-2,-1], [1, 3, 4] ]))
