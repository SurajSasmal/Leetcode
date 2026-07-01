class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = 0
        sum = 0
        n = len(num)

        arr = []

        for i in range(n):
            sum = sum * 10 + num[i]
        sum = sum + k

        while(sum > 0):
            arr.append(sum % 10)
            sum = sum // 10
        
        return arr[::-1]