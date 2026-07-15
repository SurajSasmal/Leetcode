class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        # if n == 1:
        #     return 1
        # evenSum = 0

        # oddSum = 1

        # for i in range(n+1):
        #     evenSum = evenSum + i * 2

        #     oddSum = oddSum + 2 * i - 1
        
        # if evenSum > oddSum:
        #     divident = evenSum 
        #     divisor = oddSum
        # else:
        #     divident = oddSum
        #     divisor = evenSum

        # rem = divident % divisor 

        # return rem

        evenSum = 0
        oddSum = 0 

        for i in range(1,n + 1):
            evenSum += 2 * i
            oddSum += 2 * i - 1
        
        while oddSum != 0:
            rem = evenSum  % oddSum
            evenSum = oddSum 
            oddSum = rem 

        return evenSum