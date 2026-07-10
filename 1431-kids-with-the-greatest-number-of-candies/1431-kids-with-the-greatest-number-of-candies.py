class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)

        maximum = max(candies)
        result = [0] * n

        for i in range(n):
            if candies[i] + extraCandies >= maximum:
                result[i] = True
            else:
                result[i] = False
        return result