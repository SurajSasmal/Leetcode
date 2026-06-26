class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i):
                if target == nums[i] + nums[j]:
                    return i, j
                else:
                    j = nums[j+1]
        