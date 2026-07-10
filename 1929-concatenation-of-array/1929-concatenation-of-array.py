class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        concat = [0] * (2 * n)

        for i in range(n):
            concat[i] = nums[i]
            concat[i + n] = nums[i]
        
        return concat 