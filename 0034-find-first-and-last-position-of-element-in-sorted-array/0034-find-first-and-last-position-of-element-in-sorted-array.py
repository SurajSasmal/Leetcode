class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # this problem will divide into two parts 
        # first half 
        # last half 

        l = 0
        r = len(nums) - 1
        first = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                r = mid - 1
                first = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        l = 0
        r = len(nums) - 1
        last = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                l = mid + 1
                last = mid 
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [first,last]
