class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        run = [0] * n
        for i in range(n):
            sum = 0
            for j in range(i+1):
                sum = sum + nums[j]
            run[i] = sum
        return run
