class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        totalCount = []

        for num in nums:
            count = 0
            for j in range(n):
                if num > nums[j] and nums[j] != num:
                    count += 1
            totalCount.append(count)
        return totalCount 
        