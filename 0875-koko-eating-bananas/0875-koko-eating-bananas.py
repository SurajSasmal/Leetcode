class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1

        right = max(piles)

        while left <= right:

            mid = (left + right) // 2

            totalHours = 0

            for pile in piles:

                hours = (pile + mid - 1) // mid 

                totalHours += hours

            if totalHours <= h:
                answer = mid 
                right = mid - 1
            else:
                left = mid + 1

        return answer

