class Solution2:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()

        def twoSum(nums, target, ignore_index):
            pairs = set()
            mp = {}

            for i, x in enumerate(nums):
                if i == ignore_index: continue
                complement = target - x
                if complement in mp:
                    pairs.add(
                        (mp[complement], i)
                    )
                mp[x] = i

            return pairs

        for i, target in enumerate(nums):
            for pair in twoSum(nums, -target, i):
                triplet = [nums[i], nums[pair[0]], nums[pair[1]]]
                triplet.sort()
                ans.add(tuple(triplet))

        return [list(x) for x in ans]


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            # because we are interested in unique triplets
            # escape duplicates for first number in triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # incase sum is already positive, and rest following numbers
            # will be bigger, total can never be 0 now, so break
            if nums[i] > 0:
                break

            lo, hi = i + 1, n - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]

                if total == 0:
                    ans.append([nums[i], nums[lo], nums[hi]])

                    # escape duplicates for second number in triplet
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1

                    # escape duplicates for third number in triplet
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1

                    lo += 1
                    hi -= 1

                elif total < 0:
                    lo += 1
                else:
                    hi -= 1

        return ans


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))

nums = [0, 1, 1]
print(Solution().threeSum(nums))

nums = [0, 0, 0]
print(Solution().threeSum(nums))
