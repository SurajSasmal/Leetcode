class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        # nums2 = []

        # for num in nums:
        #     if not nums2 or nums2[-1] != num:
        #         nums2.append(num)

        # ans = 0
        # n = len(nums2)

        # for i in range(1,n-1):
        #     if nums2[i - 1] < nums2[i] > nums2[i + 1]:
        #         ans += 1
        #     if nums2[i - 1] > nums2[i] < nums2[i + 1]:
        #         ans += 1
        # return ans

        ans = 0

        prev = nums[0]

        n = len(nums)

        for i in range(1,n - 1):
            if nums[i] == nums[i + 1]:
                continue
            if prev < nums[i] > nums[i + 1]:
                ans += 1
            elif prev > nums[i] < nums[i + 1]:
                ans += 1
            prev = nums[i]
        return ans 
        