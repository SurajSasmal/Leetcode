class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # arr = [] - > 0(n logn)

        # for num in nums:

        #     number = num * num

        #     arr.append(number)

        # arr.sort()

        # return arr

        l = 0
        r = len(nums) - 1
        k = r
        squareNums = [0] * len(nums)

        while l <= r:

            lastSquare = nums[l] * nums[l]

            rightSquare = nums[r] * nums[r]

            if lastSquare < rightSquare:
                squareNums[k] = rightSquare
                r -= 1
            else:
                squareNums[k] = lastSquare
                l += 1
            k -= 1
        return squareNums 
