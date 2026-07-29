class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        answer = float('inf')

        sum = 0

        i = 0

        n = len(nums)

        for j in range(n):

            sum = sum + nums[j]

            while sum >= target:

                answer = min(answer,j - i + 1)

                sum = sum - nums[i]

                i += 1
        if answer == float('inf'):
            return 0
        else:
            return answer
        

