class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # n = len(nums)

        # result = []

        # for i in range(n):
        #     total = 0
        #     for j in range(i+1):
        #         total = total + nums[j]
        #     result.append(total)
        # return result

        for i in range(1,len(nums)):
            nums[i] += nums[i - 1]
        return nums
        
