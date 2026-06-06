class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        mask = 3
        count = 0
        while mask <= n:
            # print(f"{bin(n)[2:]:>6}")
            # print(f"{bin(mask)[2:]:>6}")
            result = mask & n
            if result == mask:
                count += 1
#             print(f"{bin(result)[2:]:>6}")
#             print("======================")
            if count > 1:
                return False
            mask = mask << 1

        return count == 1

nums = 96
print(Solution().consecutiveSetBits(nums))

nums = 5
print(Solution().consecutiveSetBits(nums))
