class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        sum = 0
        place = 1

        while(n != 0):
            rem = n % 10
            if rem != 0:
                x = rem * place + x
                place = place * 10
                sum = sum + rem
            n = n // 10
        return x * sum