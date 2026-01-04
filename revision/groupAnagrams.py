from collections import defaultdict

class Solution:
    def keygen(self, s: str) -> tuple:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            group[self.keygen(s)].append(s)
        
        return list(group.values())