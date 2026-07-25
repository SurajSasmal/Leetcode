class Solution:
    def maxProduct(self, n: int) -> int:
        
        max1 = -1
        max2 = -1 

        # ans= []

        while(n != 0):
            rem = n % 10
            if max1 <= rem:
                max2 = max1
                max1 = rem
            elif max2 < rem:
                max2 = rem

            n = n // 10
        
        return max1 * max2





        
