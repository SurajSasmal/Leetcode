class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        iscount = []

        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            iscount.append(count)
        return max(iscount)
