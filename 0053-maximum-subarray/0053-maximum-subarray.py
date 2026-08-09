class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # maxSum = float('-inf')  => 0(n^2)
        # n = len(nums)

        # for i in range(n):
        #     currentSum = 0
        #     for j in range(i,n):
        #         currentSum += nums[j]
        #         maxSum = max(maxSum, currentSum)
        # return maxSum

        currentSum = 0
        maxSum = float('-inf')
        for num in nums:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)
        return maxSum