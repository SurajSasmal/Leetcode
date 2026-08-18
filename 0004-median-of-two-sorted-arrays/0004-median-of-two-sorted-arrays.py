class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1 = nums1 + nums2

        nums1.sort()

        n = len(nums1)

        ans = 0

        if n % 2 == 0:
            m = n // 2 
            ans = (nums1[m-1] + nums1[m]) / 2
        else:
            m = n // 2

            ans = nums1[m] / 1

        return ans 