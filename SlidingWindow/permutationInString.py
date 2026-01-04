class Solution:
    # True when: s2 contains a permutation of s1
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        # means s2 cannot contain s1
        if s2_len < s1_len:
            return False

        s1_window = [0] * 26
        s2_window = [0] * 26

        # create first window: same size as s1
        for index in range(s1_len):
            s1_window[ord(s1[index]) - ord('a')] += 1
            s2_window[ord(s2[index]) - ord('a')] += 1

        if s1_window == s2_window:
            return True

        # slide the fixed size window
        for index in range(s2_len - s1_len):
            s2_window[ord(s2[index + s1_len]) - ord('a')] += 1
            s2_window[ord(s2[index]) - ord('a')] -= 1

            if s1_window == s2_window:
                return True

        return False


s1 = "hello"
s2 = "ooolleoooleh"
print(Solution().checkInclusion(s1, s2))

s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))

s1 = "adc"
s2 = "dcda"
print(Solution().checkInclusion(s1, s2))

s1 = "ab"
s2 = "eidboaoo"
print(Solution().checkInclusion(s1, s2))
