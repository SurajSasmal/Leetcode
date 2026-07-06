class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n < 1:
        #     return False
        # if n == 1:
        #     return True 
        # if n % 3 != 0:
        #     return False
        # else:
        #     return self.isPowerOfThree(n // 3)
        
        # or 
        if n < 1:
            return False
        while(n > 1):
            if n % 3 != 0:
                return False
            else:
                n = n // 3
        if n == 1:
            return True