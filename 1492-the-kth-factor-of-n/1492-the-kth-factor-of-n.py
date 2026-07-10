class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []

        for i in range(1,n+1):
            if n % i == 0:
                factors.append(i)
        
        m = len(factors)

        # for j in range(m):
        #     if j == k -1:
        #         return lis[k-1]

        if m >= k:
            return factors[k - 1]

        return -1