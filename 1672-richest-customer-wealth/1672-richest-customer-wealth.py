class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)

        maj = float('-inf')

        for i in range(n):
            cust = accounts[i]
            sum = 0
            m = len(cust)

            for j in range(m):
                sum = sum + cust[j]
            if maj < sum:
                maj = sum
        return maj