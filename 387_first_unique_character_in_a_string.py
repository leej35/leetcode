class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c='abcdefghijklmnopqrstuvwxyz'
        sc = [s.index(l) for l in list(c) if s.count(l)==1]
        return -1 if len(sc) < 1 else min(sc)
