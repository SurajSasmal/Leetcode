class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n < 1:
        #     return False
        # if n == 1:
        #     return True
        # if n % 4 != 0:
        #     return False
        # else:
        #     return self.isPowerOfFour(n // 4)

        # or 

        if n < 1:
            return False

        while(n > 1):
            if n % 4 != 0:
                return False
            else:
                n = n // 4
        if n == 1:
            return True