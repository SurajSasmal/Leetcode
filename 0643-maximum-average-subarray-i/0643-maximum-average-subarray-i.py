class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        windowSum = sum(nums[:k])

        answer = windowSum 

        n = len(nums)

        for r in range(k,n):

            windowSum += nums[r]

            windowSum -= nums[r-k]

            answer = max(answer,windowSum)

        return answer / k

