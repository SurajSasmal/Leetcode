class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)

        r = sum(weights)
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            total = 0
            daysCount = 1

            for weight in weights:
                if total + weight <= mid:
                    total += weight
                else:
                    daysCount += 1
                    total = weight

            if daysCount <= days:
                ans = mid 
                r = mid - 1
            elif daysCount > days:
                l = mid + 1
            else:
                r = mid - 1
        return ans 