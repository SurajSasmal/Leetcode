class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        k = 1

        while(i < n):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k