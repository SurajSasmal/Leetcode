class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)

        small = []
        for i in range(n):
            num = nums[i]
            count = 0
            for j in range(n):
                if num > nums[j]:
                    count += 1
            small.append(count)
        return small