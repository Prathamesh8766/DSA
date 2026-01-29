def florandceil(arr,target):
    def ceil(arr,target):
        high = len(arr) - 1
        low = 0
        ceil = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= target: 
                ceil = mid
                high = mid - 1
            else:
                low = mid + 1
        return arr[ceil] if ceil != -1 else -1

    def flor(arr,target):
        high = len(arr) - 1
        low = 0
        flor = -1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= target:
                flor = mid
                low = mid + 1
            else:
                high = mid - 1
        return arr[flor] if flor != -1 else -1

    return [f'Ceil: {ceil(arr,target)}' , f'Flor: {flor(arr,target)}'] 

print(florandceil([10,11,20,28,30,40,50],20))                   