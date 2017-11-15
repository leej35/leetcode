class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1: return 0
        n=0
        m={c:i+1 for i,c in enumerate(list('abcdefghijklmnopqrstuvwxyz'.upper()))}
        for i,c in enumerate(list(s)):
            i=len(s)-i-1
            n+=(26**i)*m[c]
        return n
