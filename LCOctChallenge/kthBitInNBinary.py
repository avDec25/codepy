class Solution:
    def rev_inv(self, param):
        ans = []
        for i in range(len(param) - 1, -1, -1):
            if param[i] == '0':
                ans.append('1')
            else:
                ans.append('0')
        return ans

    def findKthBit(self, n: int, k: int) -> str:
        prev = '0'
        for i in range(1, n):
            new_s = f"{''.join(prev)}1{''.join(self.rev_inv(prev))}"
            prev = new_s

        return prev[k - 1]


n = 3
k = 1
print(Solution().findKthBit(n, k))

n = 4
k = 11
print(Solution().findKthBit(n, k))
