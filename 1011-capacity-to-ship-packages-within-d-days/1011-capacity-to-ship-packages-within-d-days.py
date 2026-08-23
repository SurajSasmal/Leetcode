class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)
        ans = 0
        
        while left <= right:
            totalDays = 1
            mid = (left + right) // 2
            total = 0
            for weight in weights:
                if total + weight <= mid:
                    total += weight
                else:
                    total = weight 
                    totalDays += 1

            if totalDays <= days:
                ans = mid 
                right = mid - 1
            else:
                left = mid + 1
        return ans
