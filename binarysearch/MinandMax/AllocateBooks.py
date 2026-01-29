def brut(arr,s):
        if len(arr) < s:
            return -1
        ans = float("inf")
        for pages in range(max(arr),sum(arr)+1):
            pagesStudent =0
            student = 1
            for j in range(len(arr)):
                
                if  pagesStudent + arr[j] <= pages:
                    pagesStudent += arr[j]
                else:
                    student +=1
                    pagesStudent = arr[j]
            if student <= s:
                return pages        
                       

                   

print(brut([25,46,28,49,24],4))        
print(brut( [12, 34, 67, 90],2))
print(brut([15, 17, 20],5))
print(brut([10, 20, 30, 40],2))
print(brut([15, 10, 19, 10, 5, 18, 1],5))
