# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        
        n = mountainArr.length()
        l = 0
        r = n - 1
        # finding the peak element 
        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid 

        peak = l

        # left side search 
        l = 0
        r = peak

        while l <= r:
            mid = (l + r) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                l = mid + 1
            else:
                r = mid - 1
        
        # right side search 
        l = peak 
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1