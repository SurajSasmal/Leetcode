class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        l = 1
        r = max(nums)
        # ans = 0
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for num in nums:
                divisor = (num + mid - 1) // mid 
                total += divisor 

            if total <= threshold:
                # ans = mid
                r = mid - 1
            elif total > threshold:
                l = mid + 1
            else:
                r = mid - 1
        return r + 1
