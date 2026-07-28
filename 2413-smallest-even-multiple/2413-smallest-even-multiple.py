class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        if n % 2 == 0:
            div = n // 2

            return div * 2
        
        return n * 2
        