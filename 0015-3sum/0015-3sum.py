class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()

        s = set()

        result = []

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r] 

                if sum == 0:
                    s.add((nums[i] ,nums[l] ,nums[r]))
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1

        result = list(s)
        
        return result


