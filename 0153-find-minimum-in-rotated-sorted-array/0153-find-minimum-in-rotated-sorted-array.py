class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # minElement = float('inf')

        # for num in nums:
        #     minElement = min(minElement, num)
        
        # return minElement 

        l = 0

        r = len(nums) - 1

        while l < r:

            mid = (l + r) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
        return nums[l]