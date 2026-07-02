class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        for i in range(n):
            minId = i

            for j in range(i+1,n):
                if nums[j] < nums[minId]:
                    minId = j
            nums[i], nums[minId] = nums[minId], nums[i]
        return nums
