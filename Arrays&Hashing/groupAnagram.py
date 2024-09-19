from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for i in range(len(strs)):
            anagram[''.join(sorted(strs[i]))].append(i)

        print(anagram)

        ans = []
        for key in anagram.keys():
            temp = []
            for i in anagram[key]:
                temp.append(strs[i])
            ans.append(temp)
        return ans


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))

    strs = [""]
    print(Solution().groupAnagrams(strs))

    strs = ["a"]
    print(Solution().groupAnagrams(strs))
