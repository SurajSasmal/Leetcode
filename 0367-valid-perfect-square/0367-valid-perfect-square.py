class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left = 1

        right = num 

        while left <= right:
            mid = (left + right) // 2

            Square = mid * mid

            if Square == num:
                return True
            elif Square > num:
                right = mid - 1
            elif Square < num:
                left = mid + 1
        return False