class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        n = len(candies)

        greatestCandey = max(candies)

        answer = []

        for candey in candies:
            if candey + extraCandies >= greatestCandey:
                answer.append(True)
            else:
                answer.append(False)
        return answer