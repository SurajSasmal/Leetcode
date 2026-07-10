class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        lis = []

        for i in range(1,n+1):
            if n % i == 0:
                lis.append(i)
        
        m = len(lis)

        # for j in range(m):
        #     if j == k -1:
        #         return lis[k-1]

        if m >= k:
            return lis[k - 1]

        return -1