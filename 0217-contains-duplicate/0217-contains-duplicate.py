class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # j = 0
        # n = len(nums)
        # nums.sort()

        # for i in range(1,n):
        #     if nums[j] == nums[i]:
        #         return True
        #     else:
        #         j += 1
        # return False

        return len(nums) != len(set(nums))