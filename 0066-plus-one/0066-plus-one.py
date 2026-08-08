class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        total = 0

        product = 1
        n = len(digits)

        digits = digits[::-1]

        for i in range(n):
            total = total + digits[i] * product
            product = product * 10
        
        total = total + 1

        result = []

        while total != 0:
            rem = total % 10
            result.append(rem)
            total = total // 10
        
        return result[::-1]