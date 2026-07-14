class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)

        nums = 0

        for i in range(n):
            nums = nums * 10 + digits[i]
        total = nums + 1

        last = []

        while(total != 0):
            rem = total % 10
            last.append(rem)
            total = total // 10

        return last[::-1]