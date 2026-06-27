class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        n = num
        while(num != 0):
            rem = num % 10
            if n % rem == 0:
                count += 1
            num = num // 10
        return count