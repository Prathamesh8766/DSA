
arr=[9,87,47,3,2,45,64,7]


def quick_sort(arr, start, end):
    if start >= end:
        return
    def partition(arr, start, end):
        index = start - 1
        for j in range(start, end):
            if arr[j] < arr[end]:
                index += 1
                arr[index], arr[j] = arr[j], arr[index]

        arr[index + 1], arr[end] = arr[end], arr[index + 1]
        return index + 1
    pivot = partition(arr, start, end)
    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)





# """
# 📊 Cases:
# | Case | Time Complexity | Explanation | 
# | Best | O(n log n) | Pivot divides array into two equal halves. Each level does O(n) work, and there are log n levels. | 
# | Average | O(n log n) | On average, pivot divides array reasonably well. | 
# | Worst | O(n²) | Pivot is always the smallest or largest element, leading to unbalanced partitions. | whent the arry is allredy sorted



# -
# 📊 Cases:
# | Case | Space Complexity | Explanation | 
# | Best/Average | O(log n) | Balanced recursion tree. | 
# | Worst | O(n) | Skewed recursion tree due to poor pivot choices. | 



# """




def merge_sort(arr, start, end):
    if start >= end:
        return

    mid = start + (end - start) // 2

    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)

    temp = []
    left = start
    right = mid + 1

    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= end:
        temp.append(arr[right])
        right += 1


    for i in range(len(temp)):
        arr[start + i] = temp[i]

arr = [6, 3, 9, 5, 2, 8]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
