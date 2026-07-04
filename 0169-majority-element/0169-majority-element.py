class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)

        # return nums[n//2]
        majority = nums[0]
        vote = 0
        n = len(nums)
        for i in range(n):
            if vote == 0:
                vote = vote + 1
                majority = nums[i]
            elif majority == nums[i]:
                vote = vote + 1
            else:
                vote = vote - 1
        return majority 