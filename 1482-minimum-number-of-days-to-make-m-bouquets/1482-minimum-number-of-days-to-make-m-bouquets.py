class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:


        if len(bloomDay) < m * k:
            return -1 

        left = min(bloomDay)
        right = max(bloomDay)
        
        while left <= right:
            mid = (left + right) // 2 
            bouquet = 0
            flower = 0
            for bloom in bloomDay:
                if bloom <= mid:
                    flower += 1
                    if flower == k:
                        bouquet += 1
                        flower = 0
                else:
                    flower = 0
            if bouquet >= m:
                right = mid - 1
            else:
                left = mid + 1
        return left 