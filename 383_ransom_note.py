class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r,m = list(ransomNote), list(magazine)
        for c in r:
            if c in m: 
                m.remove(c)
            else:
                return False
        return True
