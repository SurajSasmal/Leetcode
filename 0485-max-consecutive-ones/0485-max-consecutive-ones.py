class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        totalCount = []
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            totalCount.append(count)
        return max(totalCount) 