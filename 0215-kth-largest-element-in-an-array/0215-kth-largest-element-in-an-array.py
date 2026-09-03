class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        n = len(nums)

        m = n - k

        return nums[m]
        