class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        
        nums1 = nums.copy()

        nums1.sort()

        if nums == nums1 or nums == nums1[::-1]:
            return True
        return False