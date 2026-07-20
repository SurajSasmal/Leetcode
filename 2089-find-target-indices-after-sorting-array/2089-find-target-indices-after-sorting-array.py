class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        # it is done by brute force 
        # time complexity - 0(n log n)
        # nums.sort()

        # arr = []

        # n = len(nums)

        # for i in range(n):
        #     if nums[i] == target:
        #         arr.append(i)
        # return arr

# by binary search 

        nums.sort()

        # first occurrance

        left = 0
        right = len(nums) - 1
        first = -1 

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first = mid 
                right = mid - 1       # left side search
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if first == -1:
            return []
        
        # last ocuurance

        left = 0
        right = len(nums) - 1
        last = -1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                last = mid 
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        ans = []

        for i in range(first, last+1):
            ans.append(i)
        
        return ans