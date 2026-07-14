class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = []

        n = len(nums)

        count = 0

        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            total.append(count)
        return max(total)
        