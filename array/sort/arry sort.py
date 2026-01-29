
arr=[13,46,24,52,20,9]
def selectionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            if arr[j]<arr[i] : arr[i] ,arr[j]=arr[j],arr[i]

    return arr
print(selectionSort(arr))        

def bubleSort(arr):
    count=0
    for i in range(len(arr)-1, 0, -1):

        for j in range(i):
            if arr[j]>arr[j+1] : 
                arr[j], arr[j+1]=arr[j+1],arr[j] 
 
                count+=1
        if count==0:
            return  arr, count   
    return arr  , count

arrr=[13,46,24,52,20,9]  
print(bubleSort(arrr))
a=[13,46,24,52,20,9] 

def insertionSort(arr):
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j] :
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
            print(arr)
    return arr    

print(insertionSort(a))