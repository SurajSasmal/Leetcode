class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        total = 0

        n = len(nums)

        for i in range(n):
            total = total ^ nums[i]
        
        return total 
        