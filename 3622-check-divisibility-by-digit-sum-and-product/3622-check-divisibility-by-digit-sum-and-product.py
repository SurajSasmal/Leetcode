class Solution:
    def checkDivisibility(self, n: int) -> bool:

        total = 0
        product = 1
        m = n
        while n != 0:
            rem = n % 10 
            total = total + rem 
            product = product * rem 
            n = n // 10
        if m % (total + product) == 0:
            return True
        else:
            return False
            