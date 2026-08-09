class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = float('inf')

        maximum = 0

        n = len(prices)

        for i in range(n):
            if prices[i] < minimum:
                minimum = prices[i]
            if prices[i] - minimum > maximum:
                maximum = prices[i] - minimum
        return maximum

        