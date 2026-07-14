class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        iscount = 0

        n = len(nums)

        for i in range(n):
            number = nums[i]

            count = 0

            while(number != 0):
                rem = number % 10
                count += 1
                number = number // 10
            if count % 2 == 0:
                iscount += 1
        return iscount 