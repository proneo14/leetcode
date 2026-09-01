from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = defaultdict(int)
        tcount = defaultdict(int)

        if len(s) != len(t):
            return False

        for ch in s:
            scount[ch] += 1
        for c in t:
            tcount[c] += 1

        return scount == tcount 