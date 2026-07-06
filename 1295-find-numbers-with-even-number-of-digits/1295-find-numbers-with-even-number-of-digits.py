class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)

        iscount = 0

        for i in range(n):
            num = nums[i]
            count = 0
            while(num != 0):
                rem = num % 10
                count = count + 1
                num = num // 10
            
            if count % 2 == 0:
                iscount += 1
        return iscount
