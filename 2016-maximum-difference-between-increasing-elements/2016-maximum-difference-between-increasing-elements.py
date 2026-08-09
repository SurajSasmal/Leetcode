class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        minNum = nums[0]
        maxAns = -1

        for i in range(1, len(nums)):
            
            if nums[i] > minNum:
                maxAns = max(maxAns, nums[i] - minNum)
            else:
                minNum = nums[i]

        return maxAns