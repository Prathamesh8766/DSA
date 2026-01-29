

# sum of N number from A to B without using loop
def arethematic_sum():
    a = int(input("Enter the first value : "))
    b = int(input("Enter the second value : "))
    first = a * (a + 1) // 2
    second = b * (b - 1) // 2

    total = first - second
    print(f"Total sume of {a} to {b} is : {total}")

# Arry CRUD opreation
from array import *
class CreateArray:
    def __init__(self, size, typecode, values=None):
        self.size = size
        self.typecode = typecode
        self.arr = array(typecode, [])
        if values:
            if len(values) != size:
                raise ValueError(f"Expected {size} values, got {len(values)}")
            self.arr = array(typecode, values)

    def __str__(self):
        return str(list(self.arr))

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, index):
        return self.arr[index]

    def __setitem__(self, index, value):
        self.arr[index] = value

    def update_array(self, a, b):
        for i in range(len(self.arr)):
            if a == self.arr[i]:
                self.arr[i] = b

    def delete_val(self, b):
        new_arr = array(self.typecode, [i for i in self.arr if i != b])
        self.arr = new_arr

    def append(self, value):  # it is the not posiple if we is it as the arry perspective . it can appen in vectr which 
        self.arr.append(value)  # is consept of C++ 
        self.size = len(self.arr)    
        return type(self.arr)
    def fingsmalest(self):
        s= float("inf")
        ind=0
        for i in range(len(self.arr)):
            if self.arr[i]< s:
                s= self.arr[i]
                ind=i
        return s , ind    

    def reverse(self):
        i = 0
        j = len(self.arr) - 1
        def helper(i, j):
            if i >= j:
                return
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            helper(i + 1, j - 1)
        helper(i, j)

    def unique(self):
        fre={}
        for element in self.arr:
            fre[element]= fre.get(element,0)+1
        unique=[element for element in self.arr if fre[element]==1 ] 
        return unique

        
        
arrr = CreateArray(7, "i",[1,2,3,4,78,8,78])
print(arrr)
arrr.update_array(2,8)
arrr[2]=99
arrr.delete_val(8)
arrr.reverse()
print(arrr.unique())
print(arrr)
print(arrr.append(47))

print(arrr.fingsmalest())
  
# def read_aaray_from_index():
#     input_string= input("Enter sapce seprated input: ")
#     array_=list(map(int, input_string.split()))
#     print("[", end=" ")
#     for i in array_:
#         print(f"{arrr[i]},", end=" ")
#     print("]", end=" ")        
# read_aaray_from_index()    

# def array_sum():
#     ar = array.array("i", [1999, 12, 2, 3, 4, 5])
#     total = sum(ar)
#     print(total)


# arr = [1, 2, 6, 8, 5, 9]
# s = sum(arr)
# print(s)
# arr=sorted(arr)
# print(arr)

# def binary_search(arr,target):
#     l,r=0,len(arr)-1
#     while l<=r:
#         m =(l+r)//2
#         if arr[m] == target :
#             return arr.index(target)

#         elif arr[m]<target :
#             l=m+1
#         else:
#             r=m-1         
#     return -1

# print(f"elememt at {binary_search(arr,8)}")

# set = set()
# set.add(0)
# set.add(1)
# set.add(2)
# set.add(4)
# set.add(7)
# set.add(False)
# set.add(True)
# print(set)
def modify_list(lst):
   l = lst.append(4)
   print(l) 
my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

def change(x):
    x = x + 1
    print(x)
a = 5
change(a)
print(a)  # Output: 5