class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        ans = 0
        while l <= r:
            totalHours = 0
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                hours = (pile + mid - 1) // mid
                totalHours += hours 
            

            if totalHours <= h:
                ans = mid 
                r = mid - 1
            elif totalHours >= h:
                l = mid + 1
            else:
                r = mid - 1
        return ans 
