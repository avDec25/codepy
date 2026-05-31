class Solution(object):
    # def nextGreaterElements(self, nums):
    #     return [
    #         next(
    #             (x for x in nums[i + 1:] + nums[:i] if x > nums[i]), -1
    #         ) for i in range(len(nums))
    #     ]
    def nextGreaterElements(self, nums):
        nxt_grtr = []
        for i in range(len(nums)):
            found = False
            for e in nums[i + 1:] + nums[:i]:
                if nums[i] < e:
                    nxt_grtr.append(e)
                    found = True
                    break
            if not found:
                nxt_grtr.append(-1)
        return nxt_grtr


nums = [1, 2, 1]
print(Solution().nextGreaterElements(nums))

nums = [1, 2, 3, 4, 3]
print(Solution().nextGreaterElements(nums))
