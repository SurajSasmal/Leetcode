class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        isIncresing = True
        isDecresing = True

        n = len(nums)

        for i in range(1,n):
            if nums[i-1] <= nums[i]:
                isIncresing = True
            else:
                isIncresing = False
                break

        for i in range(1,n):
            if nums[i - 1] >= nums[i]:
                isDecresing = True
            else:
                isDecresing = False
                break
        
        return isIncresing or isDecresing 