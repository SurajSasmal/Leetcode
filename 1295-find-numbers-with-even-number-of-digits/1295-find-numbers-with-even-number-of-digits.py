class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        totalCount = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                totalCount += 1
        return totalCount
