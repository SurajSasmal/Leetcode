class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        minElement = float('inf')

        for num in nums:
            minElement = min(minElement, num)
        
        return minElement 
        