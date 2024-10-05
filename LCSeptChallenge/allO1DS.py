import collections
import heapq


class AllOne:

    def __init__(self):
        self.freq = dict()

    def inc(self, key: str) -> None:
        if key not in self.freq:
            self.freq[key] = 1
        else:
            self.freq[key] += 1

    def dec(self, key: str) -> None:
        if self.freq[key] == 1:
            self.freq.pop(key)
        else:
            self.freq[key] -= 1

    def getMaxKey(self) -> str:
        if not self.freq:
            return ""
        mx = 0
        mxK = None
        for k in self.freq:
            if self.freq[k] > mx:
                mx = self.freq[k]
                mxK = k
        return mxK

    def getMinKey(self) -> str:
        if not self.freq:
            return ""
        mn = float('inf')
        mnK = None
        for k in self.freq.keys():
            if self.freq[k] < mn:
                mn = self.freq[k]
                mnK = k
        return mnK


ds = AllOne()
ds.inc("hello")
ds.inc("hello")
print(ds.getMaxKey())
print(ds.getMinKey())
ds.inc("leet")
print(ds.getMaxKey())
print(ds.getMinKey())
