class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        run = [0] * n
        for i in range(n):
            total = 0
            for j in range(i+1):
                total = total + nums[j]
            run[i] = total
        return run
