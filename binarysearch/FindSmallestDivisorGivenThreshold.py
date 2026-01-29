def smallestDivisor( nums,threshold) :
        high = max(nums)
        low = 1

        def division(divisor):

            sum = 0
            for num in nums:
                sum += -(- num // divisor )

            if sum<= threshold:
                return True
            False
        while low <= high:
            mid = (low + high) // 2             
            if division(mid):
                high = mid - 1
            else: low = mid + 1

        return low      