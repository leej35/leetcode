class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def str2dic(st):
            d={}
            for c in list(st):
                if not d.has_key(c): d[c]=0
                d[c]+=1
            return d
        
        return str2dic(s) == str2dic(t)
