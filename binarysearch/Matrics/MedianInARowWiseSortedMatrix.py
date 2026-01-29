def function(mat):
    if not mat or not mat[0]:  
        return None  
    m = len(mat)
    n = len(mat[0])
    
    high = max(mat[row][n-1] for row in range(m))
    low = min(mat[row][0] for row in range(m))
    
    condition = ((m*n) // 2) + 1
    
    def checker(mid):
        count =0
        for row in mat:
            left, right = 0 , len(row) - 1
            result = -1
            while left <= right:
                m = (right + left) // 2
                if row[m] <= mid:
                    result = m
                    left = m+1 
                else: right = m - 1
            count += result + 1
        return count   
             
    while low <= high:
        mid = (low + high) // 2
        if checker(mid) >= condition:
            high = mid - 1
        else:
            low = mid + 1

    return low

mat = [[1,5,6,8,11],
       [2,3,4,5,10],
       [9,10,12,14,16]]

print(function(mat))