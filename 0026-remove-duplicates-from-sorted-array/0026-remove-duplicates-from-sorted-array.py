class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i = 1
        k = 1
        n = len(nums)
        for i in range(n):
            if nums[k-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k
