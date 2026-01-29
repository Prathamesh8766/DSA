def minHeapInsertion(nums,k):
    nums.append(k)
    l = len(nums)
    i = l - 1
    while i > 0:
        parent = (i - 1) // 2
        print(i)
        if nums[parent] > nums[i] :
            nums[parent], nums[i] = nums[i], nums[parent] 
            i = parent
        else:
            break    
    return nums        




print(minHeapInsertion([5,10,15,20,30,40],12))    
print()

def removeElmentInMinHeap(heap,idx):
    l = len(heap)
    heap[idx] = heap[l - 1] 
    heap = heap[:-1]    
    if idx < len(heap):
        parent = (idx - 1) // 2
        if idx > 0 and heap[idx] < heap[parent]:
            while idx > 0:
                parent = (idx - 1) // 2
                print(idx)
                if heap[parent] > heap[idx] :
                    heap[parent], heap[idx] = heap[idx], heap[parent] 
                    idx = parent
                else:
                    break    
        else:
            while True:
                smallest = idx
                left = 2*idx + 1
                right = 2*idx + 2

                if left < len(heap) and heap[left] < heap[smallest]:
                    smallest = left
                if right < len(heap) and heap[right] < heap[smallest]:
                    smallest = right

            
                if smallest == idx:
                    break

                heap[idx], heap[smallest] = heap[smallest], heap[idx]
                idx = smallest

    return heap

print(removeElmentInMinHeap([5,10,15,20,30,40],1))        

