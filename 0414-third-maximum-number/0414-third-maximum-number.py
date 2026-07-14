class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums.sort()

        n = len(nums)

        i = n - 1

        count = 1
        while(i != 0):
            if nums[i - 1] < nums [i]:
                count += 1

                if count == 3:
                    return nums[i - 1]
            i -= 1

        return nums[n - 1]
        