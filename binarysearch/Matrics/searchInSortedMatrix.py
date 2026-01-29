def better(mat,k):
    m = len(mat)
    n = len(mat[0])
    for row in range(m):
        if mat[row][0] <= k and k <= mat[row][n-1]:
            low = 0
            high = n-1
            while low <= high:
                mid = (low + high) // 2
                if mat[row][mid] == k:
                    return (row,mid)
                elif mat[row][mid] < k:
                    low = mid + 1
                else: high = mid - 1
            break
mat = [
    [1,2,6,10],
    [12,13,14,19],
    [20,21,23,28],
    [30,31,38,40]
]        
print(better(mat,40))

def optimal(mat,k):
    def optimal(mat, k):
        """
        Search for a target value in a sorted 2D matrix using binary search.
        This function treats a 2D matrix as a flattened 1D sorted array and performs
        a binary search to find the target value k.
        Args:
            mat (List[List[int]]): A 2D matrix sorted in row-major order
            k (int): The target value to search for
        Returns:
            Tuple[int, int]: A tuple (row, col) representing the position of k in the matrix
            int: -1 if the target value is not found or if row/col indices are invalid
        Note:
            # BUG: Line with 'row = mid // m' should be 'row = mid // n'
            # The row index calculation is incorrect. It should divide by the number of columns (n),
            # not the number of rows (m). This causes wrong row calculation and array index errors.
            # BUG: Line with 'col = mid % m' should be 'col = mid % n'
            # The column index calculation is incorrect. It should use modulo with the number of columns (n),
            # not the number of rows (m). This causes column index to exceed bounds.
            # BUG: Line with 'high = m * n' should be 'high = m * n - 1'
            # The high boundary is set to m*n instead of m*n-1, which can cause an index out of range error
            # when accessing the last element.
        """
    m = len(mat)
    n = len(mat[0])
    low = 0
    high = m * n -1
    while low <= high:
        mid = (low + high) // 2   
        row = mid // n
       
        col = mid % n
            
        if mat[row][col] == k:
            return (row, col)
        elif mat[row][col] < k:
            low = mid +1 
           
        else:  high = mid -1
    return -1
print(optimal([[1],[2]],2))
