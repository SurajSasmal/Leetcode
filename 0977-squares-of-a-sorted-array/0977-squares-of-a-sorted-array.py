class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        arr = []

        for num in nums:

            number = num * num

            arr.append(number)

        arr.sort()

        return arr
        

