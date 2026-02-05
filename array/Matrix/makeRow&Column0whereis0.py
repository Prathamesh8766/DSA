def makeRowAndColoumZeroWhereIsZero(mat):
    zero_row = []
    zero_col = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                zero_row.append(i)
                zero_col.append(j)
    for i in zero_row:
        for j in range(len(mat[0])):
            mat[i][j] = 0
    for j in zero_col:
        for i in range(len(mat)):   
            mat[i][j] = 0
    return mat
mat1= [[1,2,3,0,4],
        [1,2,3,4,5],
        [1,2,3,4,5]]
#[
# [0, 0, 0, 0, 0], 
# [1, 2, 3, 0, 5],
# [1, 2, 3, 0, 5]
# ]        

mat2 =[[0,1,2,3,4],
        [1,2,3,0,5],
        [1,2,3,4,5]]
mat3 =[[1,1,2,3,4],
        [1,2,3,1,5],
        [1,2,3,4,5]]
print(makeRowAndColoumZeroWhereIsZero(mat1))      
print(makeRowAndColoumZeroWhereIsZero(mat2))   

class Circle:
        def __init__(self,radius):
                self.__radius = radius
        @property
        def radius(self):
                return self.__radius
        @radius.setter
        def radius(self,new_radius):
                self__radius = new_radius
        @radius.deleter
        def radius(self):
                del self.__radius 
        def area(self):
                return 3.14*(self.__radius**2)
c= Circle(5)
c.area()
c.radius=6
del c.radius