class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()

        arr = []

        n = len(nums)

        for i in range(n):
            if nums[i] == target:
                arr.append(i)
        return arr
