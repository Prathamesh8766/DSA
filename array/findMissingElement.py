def brut(arr):
    for i in range(1,len(arr)+1):
        flag=0
        for j in range(len(arr)):
            if i == arr[j]:
                flag=1
                break
        if flag == 0:        
            return i
print(brut([6,4,3,2,1]))        

def better(arr):
    hash=[0]*(len(arr)+2)
    for i in range(len(arr)):
        hash[i]=0
    
    for i in arr:
        hash[i]=1

    for i in range(1,len(hash)):
        if hash[i]==0:
            return    i
print(better([6,4,3,2,1]))             


def find_missing_number(arr):

    xor1 ,xor2 = 0,0

    for i in range(len(arr)):
        xor1 = xor1 ^ i       
        xor2 = xor2 ^ arr[i] 

    print(f"xor1={xor1}")
    print(f"xor2={xor2}")
    xor1 = xor1 ^ (len(arr))

   
    return xor1 ^ xor2

correct_example = [0,1,3]

print(f"The missing number is: {find_missing_number(correct_example)}")