class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        total = sum(nums[:k])

        answer = total

        n = len(nums)

        for right in range(k,n):

            total = total + nums[right]
            total = total - nums[right - k]

            answer = max(answer,total)
        
        return answer/k
