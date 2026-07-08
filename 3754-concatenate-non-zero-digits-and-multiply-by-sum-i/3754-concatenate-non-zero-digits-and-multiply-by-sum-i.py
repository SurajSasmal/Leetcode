class Solution:
    def sumAndMultiply(self, n: int) -> int:

        x = 0
        p = 1
        total = 0

        while(n != 0):
            rem = n % 10 
            if rem != 0:
                x = x + rem * p
                total = total + rem
                p = p * 10
            n = n // 10
        result = x * total

        return result 


