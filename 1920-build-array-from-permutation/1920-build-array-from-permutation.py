class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # ans = [0] * n
        ans = []
        for i in range(n):
            # ans[i] = nums[nums[i]]
            ans.append(nums[nums[i]])
        return ans