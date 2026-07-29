class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        answer = float('inf')
        
        left = 0

        right = 0

        n = len(nums)

        total = 0

        while right < n:

            total = total + nums[right]

            while total >= target:

                total = total - nums[left]

                ind = (right - left + 1)

                answer = min(answer,ind)

                left += 1

            right += 1
        
        if answer == float('inf'):
            return 0
        else:
            return answer
        

                