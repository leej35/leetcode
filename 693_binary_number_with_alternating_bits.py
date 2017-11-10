class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=bin(n)[2:]
        for i in range(len(s)):
            if i == 0:
                continue
            if s[i-1] == s[i]:
                return False
        return True
            
