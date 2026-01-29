def optimal(mat):
    
    m = len(mat)
    n = len(mat[0])
    if n == 1 and m == 1:
        return [0,0]

    low = 0
    high = n - 1

    def findmax(mat,m,mid):
        max = 0
        row = 0
        print(mid)
        for i in range(m):
            if mat[i][mid] >max:
                max= mat[i][mid]
                row = i
        return row              
    while low <= high:
        mid = (low + high)// 2
        row = findmax(mat,m,mid)
  
        if mid != 0 and mid != n-1:
            if mat[row][mid] > mat[row][mid -1] and mat[row][mid] > mat[row][mid+1]:
                return [row, mid]
            elif mat[row][mid] < mat[row][mid-1]: high = mid -1
            else: low = mid + 1
        elif mid == 0:
            if mat[row][mid] > mat[row][mid+1]: return [row,mid]
            else: low = mid + 1
        else:
            if mat[row][mid] > mat[row][mid-1]: return [row,mid]
            else: high = mid - 1

mat = [
    [1,4,2,1,4,5],
    [2,6,3,2,3,2],
    [1,5,6,7,1,3],
    [3,6,2,3,7,2]
]
mat2 = [[10,20,15],
        [21,30,14],
        [7,16,32]]
mat3 = [[1,4],
       [3,2]]
mat4 =[[1]]
print(optimal(mat))
print(optimal(mat2))
print(optimal(mat3))
print(optimal(mat4))


        