class Solution:
    def dotproduct(self, a, b):
        ans = 0
        for x, y in zip(a, b):
            ans += x*y
        return ans


nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]
print(Solution().dotproduct(nums1, nums2))

nums1 = [0, 1, 0, 0, 0]
nums2 = [0, 0, 0, 0, 2]
print(Solution().dotproduct(nums1, nums2))

nums1 = [0, 1, 0, 0, 2, 0, 0]
nums2 = [1, 0, 0, 0, 3, 0, 4]
print(Solution().dotproduct(nums1, nums2))
