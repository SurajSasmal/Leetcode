class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        ans = 0
        while left <= right:
            totalHours = 0
            mid = (left + right) // 2 
            hours = 0

            for pile in piles:
                hours = (pile + mid - 1) // mid 
                totalHours += hours 
            
            if totalHours <= h:
                ans = mid 
                right = mid - 1
            else:
                left = mid + 1
        return ans 
