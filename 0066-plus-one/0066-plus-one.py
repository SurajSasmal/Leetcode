class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 0
        sum = 0
        add = 1
        n = len(digits)
        for i in range(n):
            sum = sum * 10 + digits[i]
        
        sum = sum + 1
        arr = []

        while(sum > 0):
            arr.append(sum % 10)
            sum = sum // 10
        return arr[::-1]