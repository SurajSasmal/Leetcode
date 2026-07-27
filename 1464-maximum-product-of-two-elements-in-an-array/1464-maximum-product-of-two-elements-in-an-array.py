class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max1 = -1

        max2 = -1

        n = len(nums)

        for i in range(n):
            if max1 <= nums[i]:
                max2 = max1
                max1 = nums[i]
            elif max2 <=nums[i]:
                max2 = nums[i]
        total  = (max1 - 1) * (max2 - 1)

        return total
         