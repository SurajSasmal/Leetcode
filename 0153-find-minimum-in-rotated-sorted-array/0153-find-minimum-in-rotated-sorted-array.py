class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # smallest = float('inf')
        # left = 0

        # right = len(nums) - 1


        # while left <= right:

        #     mid = (left + right) // 2

        #     if nums[mid] < nums[left] and nums[mid] < nums[right]:
        #         smallest = min(smallest,nums[mid])
        #         left = left + 1
        #         right = right - 1

        #     elif nums[mid] > nums[right]:
        #         smallest = min(smallest,nums[mid])
        #         left = mid + 1
        #     else:
        #         smallest = min(smallest,nums[mid])
        #         right = mid - 1
        # return smallest 


# or 
        left = 0

        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        return nums[left]