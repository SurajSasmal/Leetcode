class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # return list(set(nums1) & set(nums2))

        # set1 = set(nums1)
        # ans = set()

        # for num in nums2:
        #     if num in set1:
        #         ans.add(num)

        # return list(ans)

        nums1.sort()
        nums2.sort()
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        ans = []
        while i < n and j < m:
            if nums1[i] == nums2[j]:

                if not ans or ans[-1] != nums1[i]:
                    ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans
