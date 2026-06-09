import heapq
def minimumEffort(heights):
    rows = len(heights)
    cols = len(heights[0])
    drow = [-1,0,1,0]
    dcol = [0,1,0,-1]
    distance = [[float("inf")] * cols for _ in range(rows)]
    distance[0][0] =1
    pq = []
    heapq.heappush(pq,(0,0,0))
  
    while pq:
        cdiff, i,j =heapq.heappop(pq)
        
        if i == rows -1 and j == cols -1:
            return cdiff
        for k in range(4):
            nrow = drow[k] + i
            ncol = dcol[k] + j
            if 0<= nrow < rows and 0<= ncol < cols :
                
                diff = abs(heights[i][j] -heights[nrow][ncol])
                new_diff=max(cdiff,diff)
                if new_diff < distance[nrow][ncol]:

                    distance[nrow][ncol] = new_diff
                    heapq.heappush(pq,(new_diff, nrow, ncol))
                print(pq)
                print(distance)
    return 0

print(minimumEffort( [[1,2,2],[3,8,2],[5,3,5]]))



