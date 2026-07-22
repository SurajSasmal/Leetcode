class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0

        right = len(nums) - 1

        # smallest = float('inf')

        while left < right:
            
            mid = (left + right) // 2

            if nums[left] == nums[mid] == nums[right]:
                left = left + 1
                right = right - 1

            elif nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid 

        return nums[left]