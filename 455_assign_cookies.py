class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g=sorted(g,reverse=True)
        s=sorted(s,reverse=True)
        sat=0
        for c in g:
            if len(s)>0 and c <= s[0]:
                s.remove(s[0])
                sat += 1
        return sat
