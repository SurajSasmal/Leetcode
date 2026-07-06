class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i = 1
        # k = 1
        # n = len(nums)
        # for i in range(n):
        #     if nums[k-1] != nums[i]:
        #         nums[k] = nums[i]
        #         k += 1
        # return k

        if len(nums) == 0:
            return 0
        k = 1
        n = len(nums)

        for i in range(1,n):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k