class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        average_sum = sum(nums[:k]) 

        answer = average_sum

        n = len(nums)

        l = 0

        for r in range(k,n):

            average_sum += nums[r]
            average_sum -= nums[r-k]

            answer = max(answer,average_sum)

        return float(answer) / k



