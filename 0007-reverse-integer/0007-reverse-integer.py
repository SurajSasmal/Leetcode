class Solution:
    def reverse(self, x: int) -> int:
        negetive = -1 if x < 0 else 1
        x = abs(x)
        reverse = 0
        while(x != 0):
            rem = x % 10 
            reverse = reverse * 10 + rem
            x = x // 10
        if -2**31 <= reverse <= 2**31 - 1:
            return negetive * reverse
        else:
            return 0