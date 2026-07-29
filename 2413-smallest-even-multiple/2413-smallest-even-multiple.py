class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        if n % 2 == 0:
            rem = n // 2

            return rem * 2
            
        return n * 2