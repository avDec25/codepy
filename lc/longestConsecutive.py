class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            if num-1 not in num_set:
                curr = num
                streak = 1

                while curr+1 in num_set:
                    curr += 1
                    streak += 1
                
                longest_streak = max(longest_streak, streak)

        return longest_streak