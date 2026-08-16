class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        
        # nums1 = nums.copy()

        # nums1.sort()

        # if nums == nums1 or nums == nums1[::-1]:
        #     return True
        # return False

        isIncresing = True
        isDecreasing = True 

        n = len(nums)
        j = 0
        for i in range(1,n):
            if nums[j] <= nums[i]:
                isIncresing = True 
                j += 1
            else:
                isIncresing = False
                break
        
        k = 0
        for i in range(1,n):
            if nums[k] >= nums[i]:
                isDecresing = True
                k += 1
            else:
                isDecresing = False
                break
        
        return isIncresing or isDecresing 
