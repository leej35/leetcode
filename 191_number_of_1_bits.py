class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=0
        s=bin(n)[2:]
        for c in list(s):
            r+=int(c)
        return r
