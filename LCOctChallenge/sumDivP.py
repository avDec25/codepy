from typing import List

class Solution:
    def minSubarray(self, a: List[int], p: int) -> int:
        rem = sum(a) % p
        if rem == 0:
            return 0

        prefix_sum = 0

        # remove all elements
        min_len = len(a)
        
        remainder_map = {0: -1}

        for i, e in enumerate(a):
            prefix_sum = (prefix_sum + e) % p
            needed_remainder = (prefix_sum - rem) % p
            if needed_remainder in remainder_map:
                min_len = min(min_len, i-remainder_map[needed_remainder])

            remainder_map[prefix_sum] = i

        return min_len if min_len < len(a) else -1


        


a = [3,1,4,2]
p = 6
print(Solution().minSubarray(a, p))

a = [6,3,5,2]
p = 9
print(Solution().minSubarray(a, p))

a = [1,2,3]
p = 3
print(Solution().minSubarray(a, p))
